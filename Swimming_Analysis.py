import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt 
import statsmodels.formula.api as smf

df_swimming=pd.read_csv("Swim_Data.csv")
#Add the condition for when it is a person's first time swimming that event and they won't have a seed time.
df_swimming["Seed_Time_Seconds"]=df_swimming["Seed_Time_Seconds"].fillna("N/A(First Time)")

#Add the condition where date is mixed up in format.
df_swimming["Date"]=pd.to_datetime(df_swimming["Date"],format="mixed")

#Goal 1: Create helper columns that help you find in percentage and seconds how much time you dropped or increased.
#There are some string(object) values of the column Seed_Time_Seconds so i have to do the following code to get rid of that.
clean_data=df_swimming[df_swimming["Seed_Time_Seconds"]!="N/A(First Time)"].copy() #.copy() in this case stops us for getting SettingWithCopyWarning.
clean_data["Seed_Time_Seconds"]=pd.to_numeric(clean_data["Seed_Time_Seconds"],errors="coerce") #We are using .to_numeric() to get rid of any object data type in case there are any
clean_data["Final_Time_Seconds"]=pd.to_numeric(clean_data["Final_Time_Seconds"],errors="coerce")
df_swimming["Seconds_Dropped"]=clean_data["Seed_Time_Seconds"]-clean_data["Final_Time_Seconds"] #Negative means added time and positive means decreased time
df_swimming["Percentage_Improvement"]=round((df_swimming["Seconds_Dropped"]/clean_data["Seed_Time_Seconds"])*100,2) #Negative means added time and positive means decreased time. I used round function to make it more readable.
df_swimming["Seconds_Dropped"]=df_swimming["Seconds_Dropped"].fillna("N/A(First Time)")
df_swimming["Percentage_Improvement"]=df_swimming["Percentage_Improvement"].fillna("N/A(First Time)")
print(df_swimming.to_string()) #.to_string() to print the whole DataFrame at once.


#Goal 2: Create a Bar Chart and see if there is a relationship(p-value) between the Meet_Type and the Percentage_Improvement.
meet_type=dict()
clean_data=df_swimming[df_swimming["Percentage_Improvement"]!="N/A(First Time)"].copy()
clean_data["Percentage_Improvement"]=pd.to_numeric(clean_data["Percentage_Improvement"],errors="coerce")
for type in clean_data["Meet_Type"].unique():
    type_average=round(clean_data[clean_data["Meet_Type"]==type]["Percentage_Improvement"].mean(),2)
    meet_type[type]=float(type_average)
plt.bar(x=meet_type.keys(),height=meet_type.values(),color="teal",edgecolor="blue")
plt.title("Does Type Of Meet Affect Performance?")
plt.xlabel("Type of Meet")
plt.ylabel("Average Percentage Improvement") # Made a better way of representing this on the last goal
plt.show() # Even though the bar chart is showing that there is less improvement when swimming in championship meets, keep in mind that there are less championship meets in the csv compared to invitational meets.

#Running the sample t-tests including the fact that there might be more than two types of meets:
keys=list(meet_type.keys())
p_val=dict()
t_stat=dict()
for type in keys:
    baseline=clean_data[clean_data["Meet_Type"]==type]["Percentage_Improvement"]
    for helper in keys:
        if helper!=type:
            comparer=clean_data[clean_data["Meet_Type"]==helper]["Percentage_Improvement"]
            t_helper,p_helper=stats.ttest_ind(comparer,baseline,equal_var=False)
            p_val[(helper,type)]=round(float(p_helper),2)
            t_stat[(helper,type)]=round(float(t_helper),2)
    if len(keys)==0:
        break
print("This is the t-statistic for the following meets: ", t_stat) # The T-statistic measures the gap between your two meet averages, adjusted for how much your times fluctuate (the noise).
print("This is the p-value for the following meets: ", p_val) #  In statistics, you need a p-value below 0.05 (a 5% chance of luck) to claim a result is "real."


#Goal 3: Create a scatter plot that looks at Wind_Chill_F(basically how cold you actually are considering the wind and weather) and Percentage_Improvement. Also create a regression table to look at Correlation(R) and R^2.
clean_data=df_swimming[(df_swimming["Percentage_Improvement"]!="N/A(First Time)") & (df_swimming["Wind_Chill_F"]!="N/A(First Time)")].copy()
clean_data["Percentage_Improvement"]=pd.to_numeric(clean_data["Percentage_Improvement"],errors="coerce")
clean_data["Wind_Chill_F"]=pd.to_numeric(clean_data["Wind_Chill_F"],errors="coerce") #Unless we do this pandas will treat Wind_Chill_F column as object data type
plt.figure(figsize=(10,6))
plt.scatter(clean_data["Wind_Chill_F"],clean_data["Percentage_Improvement"],c=clean_data["Percentage_Improvement"],cmap="Set1")
plt.xlabel("Wind_Chill_F(basically how cold you actually are considering the wind and weather)")
plt.ylabel("Percentage_Improvement")
plt.title("Does weather affect Performance?")
plt.colorbar()
plt.show()

#Using Linear Regression to figure out relationship between Wind_Chill_F and Percentage_Improvement
model=smf.ols("Percentage_Improvement ~ Wind_Chill_F",data=clean_data)
results=model.fit()
print(results.summary())


#Goal 4: Does weather affect different Pool_Measures? (essentially seeing how much I improve based on Pool_Measure and weather)
clean_data=df_swimming[(df_swimming["Pool_Measure"]!="N/A(First Time)") & (df_swimming["Wind_Chill_F"]!="N/A(First Time)") & (df_swimming["Percentage_Improvement"]!="N/A(First Time)")].copy()
clean_data["Percentage_Improvement"]=pd.to_numeric(clean_data["Percentage_Improvement"],errors="coerce")
clean_data["Wind_Chill_F"]=pd.to_numeric(clean_data["Wind_Chill_F"],errors="coerce")
for measure in clean_data["Pool_Measure"].unique():
    poolmeasure=clean_data[clean_data["Pool_Measure"]==measure]
    model=smf.ols("Percentage_Improvement ~ Wind_Chill_F",data=poolmeasure).fit()
    print(model.summary())
    plt.figure(figsize=(10,6))
    plt.scatter(poolmeasure["Wind_Chill_F"],poolmeasure["Percentage_Improvement"],c=poolmeasure["Percentage_Improvement"],cmap="Set1")
    plt.xlabel("Wind_Chill_F(basically how cold you actually are considering the wind and weather)")
    plt.ylabel(f"Percentage_Improvement for {measure}")
    plt.title("Does weather affect the performance on each type of pool measure?")
    plt.colorbar()
    plt.show()

#Comparing all Pool_Measure
pm=dict()
for measure in clean_data["Pool_Measure"].unique():
    improved_swims=clean_data[(clean_data["Pool_Measure"]==measure) & (clean_data["Percentage_Improvement"]>0)]["Percentage_Improvement"].count()
    total_swims=clean_data[(clean_data["Pool_Measure"]==measure)]["Percentage_Improvement"].count()
    win_pct=(improved_swims/total_swims)*100
    pm[measure]=float(win_pct)
plt.bar(x=pm.keys(),height=pm.values(),color="teal",edgecolor="blue")
plt.title("Does Pool Measure Affect Performance?")
plt.xlabel("Pool Measure")
plt.ylabel("Average Percentage Improvement")
plt.show() #Keep in mind one pool measure may have more improvement because there were more rows where that had that pool measure.


#Goal 5: Checks if wind speed slows me down based on each pool measure and using percentage(Different from Goal 2) to see if i drop more type based on Meet_Type
clean_data=df_swimming[(df_swimming["Wind_Speed_MPH"]!="N/A(First Time)") & (df_swimming["Pool_Measure"]!= "N/A(First Time)") & (df_swimming["Percentage_Improvement"]!="N/A(First Time)") & (df_swimming["Meet_Type"]!="N/A(First Time)")].copy()
clean_data["Wind_Speed_MPH"]=pd.to_numeric(clean_data["Wind_Speed_MPH"],errors="coerce")
clean_data["Percentage_Improvement"]=pd.to_numeric(clean_data["Percentage_Improvement"],errors="coerce")
for measure in clean_data["Pool_Measure"].unique():
    helper_df=clean_data[clean_data["Pool_Measure"]==measure]
    plt.scatter(helper_df["Wind_Speed_MPH"],helper_df["Percentage_Improvement"],c=helper_df["Percentage_Improvement"],cmap="Set1")
    plt.title("Does Wind Speed affect Performance for specific pool measures?")
    plt.xlabel("Wind Speed(MPH)")
    plt.ylabel(f"Percentage Improvement for {measure}")
    plt.colorbar()
    plt.show()

#Using percentage to see if i drop more time based on each meet type(Using percentage so that the output isn't biased towards the meet type where i added more data)
clutch_performance=dict()
for type in clean_data["Meet_Type"].unique():
    clutch_win=clean_data[(clean_data["Meet_Type"]==type) & (clean_data["Percentage_Improvement"]>0)]["Percentage_Improvement"].count()
    total_swims=clean_data[(clean_data["Meet_Type"]==type)]["Percentage_Improvement"].count()
    clutch_pct=(clutch_win/total_swims)*100
    clutch_performance[type]=clutch_pct
plt.bar(clutch_performance.keys(),height=clutch_performance.values(),color="teal",edgecolor="blue")
plt.title("Which Type of meet are you good at?")
plt.xlabel("Meet Type")
plt.ylabel("Percentage of dropped time")
plt.show()