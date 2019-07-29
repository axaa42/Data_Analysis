import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sea

#This program will show the distribution of our data with data cleaning
df=pd.read_csv("CompleteDataset.csv",dtype={"Free kick accuracy": str, "Penalties": str}) #THESE TWO ARE OBJECT SO WE CONVERT TO STR FOR NOW BUT LATER WE CONVERT IT TO INT

#THE FOLLWOING WILL REMOVE VALUE THAT CONTAIN - OR + AS THIS DOES NOT ALLOW USE TO CONVERT TO INT
df = df[~df['Penalties'].apply(lambda x: '-' in x)] 
df = df[~df['Penalties'].apply(lambda x: '+' in x)]

##THE FOLLWOING WILL REMOVE VALUE THAT CONTAIN - OR + AS THIS DOES NOT ALLOW USE TO CONVERT TO INT for other column
df = df[~df['Free kick accuracy'].apply(lambda x: '-' in x)]
df = df[~df['Free kick accuracy'].apply(lambda x: '+' in x)]

##THE FOLLWOING WILL REMOVE VALUE THAT CONTAIN - OR + AS THIS DOES NOT ALLOW USE TO CONVERT TO INT for other column
df = df[~df['Sprint speed'].apply(lambda x: '-' in x)]
df = df[~df['Sprint speed'].apply(lambda x: '+' in x)]

#THE FOLLWOING WILL CONVERT THE COLUMNS TO INTERGERS
df['Penalties'] = df['Penalties'].astype('int64')
df['Free kick accuracy'] = df['Free kick accuracy'].astype('int64')
df['Sprint speed'] = df['Sprint speed'].astype('int64')


#NOTE NOT GOALKEEPS AS THEY ARE SLOW.TRY DIFFERENT POSTIONS 

#In this dataset we will find out whether being at a certain age has an effect on the amount of sprint speed given

#WE WILL ONLY GET THE COLUMNS THAT ARE OF IMPORATNCE TO US
data=df[["Name","Age","Nationality","Overall","Club","Value","Wage","Acceleration","Sprint speed","Preferred Positions"]]


data.loc[(data['Age'] < 20) & (data['Overall'] >= 75),"type"]="under 20"
data.loc[(data['Age'] >= 20) & (data['Age'] <= 25 ) & (data['Overall'] >= 75),"type"]="20-25"
data.loc[(data['Age'] >= 26) & (data['Age'] <= 30 ) & (data['Overall'] >= 75 ),"type"]="26-30"
data.loc[(data['Age'] >= 31) & (data['Age'] <= 35 ) & (data['Overall'] >= 75 ),"type"]="31-35"
data.loc[(data['Age'] >= 36) & (data['Overall'] >= 75),"type"]="over 36"

data=data[data["Overall"]>=75] #WE WILL ONLY GET PLAYERS WHO HAVE RATING HIGER THAN 75
data=data[data["Preferred Positions"]!="GK"]#WE DONT WANT KEEPS CUX THEY R SLOW
#data["Sprint speed"].plot.hist()

#WE CAN SEE FROM THE CHART ABOVE THAT THE HIST IR NEGATIVLY SKEWED AS IT IS TAIL IS POINT TO 0.
#WE CAN SEE THAT SPRINT SPEED FOR MOST IS BETWEEN 60 TO 83
#data["Age"].plot.hist()

#We can see age has a postove;y skewed as it tail is pointed to 45.
#this showes most people are ages between 20 to 30


sea.boxplot(x=data['type'],y=data["Sprint speed"])#We can see that age the median age is 25.under 25% percentile is 21.
#We can also see outliers, which does not make sense as over 38 are not allowed in footy

