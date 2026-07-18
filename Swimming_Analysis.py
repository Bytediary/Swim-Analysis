import pandas as pd
from scipy import stats
df_swimming=pd.read_csv("Swim_Data.csv")
#Add the condition for when it is a person's first time swimming that event and they won't have a seed time.
df_swimming["Seed_Time_Seconds"]=df_swimming["Seed_Time_Seconds"].fillna("N/A(First Time)")

#Goal 1: Create helper columns that help you find in percentage and seconds how much time you dropped or increased.
#There are some string(object) values of the column Seed_Time_Seconds so i have to do the following code to get rid of that.
clean_data=df_swimming[df_swimming["Seed_Time_Seconds"]!="N/A(First Time)"].copy() #.copy() in this case stops us for getting SettingWithCopyWarning.
clean_data["Seed_Time_Seconds"]=pd.to_numeric(clean_data["Seed_Time_Seconds"],errors="coerce") #We are using .to_numeric() to get rid of any object data type in case there are any
clean_data["Final_Time_Seconds"]=pd.to_numeric(clean_data["Final_Time_Seconds"],errors="coerce")
df_swimming["Seconds_Dropped"]=clean_data["Seed_Time_Seconds"]-clean_data["Final_Time_Seconds"] #Negative means added time and positive means decreased time
df_swimming["Percentage_Improvement"]=round((df_swimming["Seconds_Dropped"]/clean_data["Seed_Time_Seconds"])*100,2) #Negative means added time and positive means decreased time. I used round function to make it more readable.
df_swimming["Seconds_Dropped"]=df_swimming["Seconds_Dropped"].fillna("N/A(First Time)")
df_swimming["Percentage_Improvement"]=df_swimming["Percentage_Improvement"].fillna("N/A(First Time)")
print(df_swimming.to_string()) #.to_String() to print the whole DataFrame at once.
