import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sea

#The following program deals with situations when you have to take weighted mean.It will also show other things such as mode, median.

#MEAN IS ADDING ALL THE NUMBERS AND DIVIDING BY HOW MANY NUMBERS THERE ARE.
#Example, people of different age, to get their average we add all the ages in the dataset,
#and divide by toal number of ages.
#But if we we have a case where a certain age has more amount of people, eg most people
#in our dataset are 20 years old then it we multiple each age by their correspinding population,
#to get a more balanced weighted average based on amount rather than age.

#FORMULA FOR WEIGHTED MEAN = x*w/w x=pupil sum, w=amount of people, 
df=pd.read_csv("CompleteDataset.csv",dtype={"Free kick accuracy": str, "Penalties": str})
#print(df["Age"].value_counts())



#Before we had the outliers.Our dataset was mean was skewed little.But after removing it, the mean is not so skewed.
'''

overall_mean=df["Overall"].mean()# We get original mean

weight=df["Overall"].value_counts().reset_index()#Now we get weights from this.the amount of times each rating occurs
weight.columns = ['overall', 'amount']#We change the columns to something we can easily use

weighted_mean=(weight["overall"]*weight["amount"]).sum()/weight["amount"].sum()#This is the forumla to work out weighted mean

diff=weighted_mean-overall_mean#This find the difference between original mean and wieghted. We can see that it is zero.which means our oringal was good mean
#print(weight)



median=df["Overall"].median() #This finds the middle point or the 50% point. best used for ordinal data
mode=df["Overall"].mode()#This find the most freqeunt value.Best used for ordinal,interval and ratio.not
standard=df["Overall"].std()#This measures how sprad out our data is from the mean. 
#print(df["Overall"].mean())
#print(standard)

sea.kdeplot(df["Overall"])
plt.axvline(df["Overall"].mean(),color="Red",label="mean")
plt.axvline(median,color="Blue")
print(median,df["Overall"].mean())
plt.legend()



#The follwoing will take z-scores of one of the columns in the dataset
df["age_zscore"] = df["Age"].apply(
                          lambda x: (x - df["Age"].mean()) / df["Age"].std()
                          )
print("The mean age is=",df["Age"].mean())
print(df[["Name","Age","age_zscore"]].head(20))


'''




