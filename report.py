import pandas as pd
df = pd.read_csv('D:\\2023\\YINTEG\\inhouse\\data.csv')
employees_unique = list(set(pd.concat([pd.Series(df[col].dropna().unique()) for col in ['Developer','TMC or TTL', 'Consultant', 'Analyst Designer', 'QA Tester', 'Documenter', 'Product Manager']])))
employees_unique =  ['Employee'] + employees_unique
output_pd = pd.DataFrame(columns=employees_unique)
output_pd['Employee'] = pd.Series(employees_unique)

from collections import Counter
# output_pd.set_index('Employee', inplace=True)
for employee in employees_unique[1:]:
    developer_df = df.loc[df['Developer'] == employee]
    employees_filter = list(pd.concat([pd.Series(developer_df[col]) for col in ['Developer', 'TMC or TTL', 'Consultant', 'Analyst Designer', 'QA Tester', 'Documenter', 'Product Manager']]))
    counter = Counter(employees_filter)
    if employee in counter:
        counter.pop(employee)
    for key, value in counter.items():
        if key in output_pd.columns:
            # update value in the output_pd row is the employee and column is the key
            output_pd.loc[output_pd['Employee'] == employee, key] = value
           
# add first column with employee name
output_pd.to_csv('D:\\2023\\YINTEG\\inhouse\\output.csv')
