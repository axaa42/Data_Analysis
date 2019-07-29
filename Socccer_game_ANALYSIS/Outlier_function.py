import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sea

df=pd.read_csv("CompleteDataset.csv",dtype={"Free kick accuracy": str, "Penalties": str})
#print(df["Age"].value_counts())

sea.boxplot(x=df["Age"])#We can see that there are outliers.We will remove this with a function
plt.show()
original_mean=df["Age"].mean()
print(original_mean)
#the follwing function will remove outliers. and return the dataframe
def remove_outlier(df_in, col_name):
    q1 = df_in[col_name].quantile(0.25)
    q3 = df_in[col_name].quantile(0.75)
    iqr = q3-q1 #Interquartile range
    fence_low  = q1-1.5*iqr
    fence_high = q3+1.5*iqr
    df_out = df_in.loc[(df_in[col_name] > fence_low) & (df_in[col_name] < fence_high)]
    return df_out
new=remove_outlier(df,"Age")#This is calling the function on our dataframe
#print(f["Age"].value_counts())
sea.boxplot(x=new["Age"])#We can see that the function has removed the outliers.Now our mean of age will be accurate
plt.show()
new_mean=new["Age"].mean()
print(new_mean)
#we have removed outliers and got a more accurate mean