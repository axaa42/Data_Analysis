import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sea
#In this dataset we will find out whether being at a certain age has an effect on the amount of sprint speed given

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



#WE WILL ONLY GET THE COLUMNS THAT ARE OF IMPORATNCE TO US
data=df[["Name","Age","Nationality","Overall","Club","Value","Wage","Acceleration","Sprint speed","Preferred Positions"]]
#data['Sprint speed'] = data['Sprint speed'].astype('int64')

#the following will make a new coloumn called type. which will catagories ages(if less than 20 then young etc)
data.loc[(data['Age'] < 20) & (data['Overall'] >= 75),"type"]="under 20"
data.loc[(data['Age'] >= 20) & (data['Age'] <= 25 ) & (data['Overall'] >= 75),"type"]="20-25"
data.loc[(data['Age'] >= 26) & (data['Age'] <= 30 ) & (data['Overall'] >= 75 ),"type"]="26-30"
data.loc[(data['Age'] >= 31) & (data['Age'] <= 35 ) & (data['Overall'] >= 75 ),"type"]="31-35"
data.loc[(data['Age'] >= 36) & (data['Overall'] >= 75),"type"]="over 36"

data=data[data["Overall"]>=75] #WE WILL ONLY GET PLAYERS WHO HAVE RATING HIGER THAN 75
data=data[data["Preferred Positions"]!="GK"]#WE DONT WANT KEEPS CUX THEY R SLOW

u=data["type"].value_counts().reset_index()#this will will get all the catagroical ages we have defined


player_total=u.set_index('index')['type'].to_dict() #We will convert the index and ages to dic to see their total

#find mean of accelartion and do plot


#uNDER We will make a df. we will add the age(catagorical) and the mean of each age groups sprint speed
#this will tell us what the average speed is per age group
cols = ["age", 'mean'] #
dat = pd.DataFrame(columns = cols)
        
for key,value in player_total.items():
    x=data.loc[data["type"]==key]["Sprint speed"].mean()
    dat = dat.append({'age': key, 'mean':int(x)},ignore_index=True)
print(dat)
    
#THE FOLLWOING WILL COUNT AMOUNT OF TIMES SOMETHING OCCURS
#sea.distplot(dat["mean"])
##sea.countplot(x = 'age',hue="mean", data = dat)
##plt.show()

#THE FOLLWOING WILL MAKE  BAR PLOT WHICH WILL SHOW US ALL THE MEANS OF ALL THE AGE CATOGIES
ax = dat.set_index('age').plot(kind='bar', title ="mean_OF_speed", figsize=(8, 6), legend=True, fontsize=8)

ax.set_xlabel("AGE", fontsize=12)
ax.set_ylabel("MEANS", fontsize=12)
ax.axhline(data["Sprint speed"].mean(), color='r', linestyle='--') #tHIS WILL MAKE A MEANS LINE FOR THE POPULATION DATASET SO WE CAN CAMPARE OUR INDIVIDUAL AGE GROUPS WITH THE ACTUAL MEAN OF POPULATION SPEED
plt.show()
'''
xa=(data["Age"].value_counts(normalize=True,bins=10)*100).reset_index()
print(xa)

'''
#WE CAN CLEARLY SEE FROM THE PIE CHART THAT BETWEEN AGES OF 19 TO 28 ARE WHERE MOST OF OUR PLAYERS AGES ARE


#GET SAMPLES FROM EACH CATAGORICAL DATA CUZ WE WANT HAVE LESS ITEMS IN ONE CATAGORY AND MORE IN ANOTHER
#TAKE LIKE 
