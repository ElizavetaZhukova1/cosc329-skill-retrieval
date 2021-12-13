import pandas as pd
df1=pd.read_csv('all_skills_1.csv')
df2=pd.read_csv('all_skills_2.csv')
df3=pd.read_csv('all_skills_3.csv')
df=df1.append(df2)
df=df.append(df3)
df.to_csv('merged_10k_skills.csv')
print(df)