import pandas as pd
df_1=pd.read_csv('jobs_to_merge.csv')
df_s=pd.read_csv('jobs.csv')
df_d=df_s.append(df_1)
df_l=pd.read_csv('jobs_last.csv')
df_f=df_d.append(df_l)
df_f.to_csv('jobs_merged_10k.csv')