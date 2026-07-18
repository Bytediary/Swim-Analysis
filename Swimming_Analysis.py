import pandas as pandas
from scipy import stats
df_swimming=pd.read_csv("Swim_Data.csv")
#Add the condition for when it is a person's first time swimming that event and they won't have a seed time.
df_swimming["Seed_Time_Seconds"]=df_swimming["Seed_Time_Seconds"].fillna("N/A(First Time)")
