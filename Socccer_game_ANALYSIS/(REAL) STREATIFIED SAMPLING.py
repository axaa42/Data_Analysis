import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sea
#This proeject will demonstate how to take a stratefied sample(Less Bias) from a dataset to get more accurate results.


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


#TAKE A STRATFIED SAMPLE BAED ON TYPE COLUMN.THEN TAKE THE MEAN OF THE ACCELERATION TO SEE IF ACCELEATION IS AFFECTED BY AGE
#then take mean of whole population and campare the other catagorical age groups to it

#x=data["Sprint speed"].sample(n=10,random_state=1).mean()
#print(x)
#THE FOLLOWING TAKES A SRATIFIED SAMPLNIG OF SPRINT SPEED PER AGE

#The follwoing gives us a propeortion of the amount of samples we should include from each group in our final stratified sample
u=round(len(data[data["type"]=="under 20"])/len(data)*100)
v=round(len(data[data["type"]=="20-25"])/len(data)*100)
y=round(len(data[data["type"]=="26-30"])/len(data)*100)
x1=round(len(data[data["type"]=="31-35"])/len(data)*100)
z=round(len(data[data["type"]=="over 36"])/len(data)*100)

print(data["type"].value_counts(normalize=True)*100)# THIS WILL TELL US HOW MUCH PROPORTION YOU NEED FOR EACH SAMPLE

#The following splits the df into the age gaps, so we can use it in the for loop to get sample from each group
g=data[data["type"]=="under 20"]
h=data[data["type"]=="20-25"]
i=data[data["type"]=="26-30"]
j=data[data["type"]=="31-35"]

'''
#the following is just some data we need for our for loop
t=["g","h","i","j","k"]
f=[u,v,y,x1,z]
l=["under 20","20-25","26-30","31-35","over 36"]
'''
#The o willing will get mean of each sample
o=[]

#TThis for loop will loop 100 times, and get the proportion amount of sample from each group based on 
#The amount of lenth of each group.Whic we worked out from value counts above.
#Reason we are going over 100 times, is cuz we want 100 samples, which we will then concatenate.
#Each time the loop runs.the ranodm_state will change the value of the sample so new values replace strateified
for x in range(100):
     a1=g.sample(n=1,random_state=x)
     a2=h.sample(n=34,random_state=x)
     a3=i.sample(n=45,random_state=x)
     a4=j.sample(n=18,random_state=x)
     a5=k.sample(n=2,random_state=x)
     
     stratified=pd.concat([a1,a2,a3,a4,a5])#This will make a stratified dataframe.which will only include 100 samples, with each group getting proportion based 
                                            #on data we worked out above.now if we work our the mean of our stratieid it will give more accurate representaion
     aa=round(stratified["Sprint speed"].mean())#This will get the mean of random_state=1,2,3 seperate means
                                                #AND WE WANT SPRINT SPEED
     o.append(aa)#Now we will append the means of all our stratfied samples so we can make scatter plot and campare how all of the did

print(o)
plt.scatter(range(1,101), o)#This will plot all the sample of the stratfied sample
plt.axhline(data['Sprint speed'].mean())#This will get the mean of population

#What we learnt from this is that our stratfied representiaon is very accruate agasint the average.
#With 67 and 72 the most values.
#This also shows that stratfeid sampling will give you the most accruate represnetation of a population
















'''
evi=stratified["type"].value_counts()#This shows the amount we have of each proportion in group
aa=round(data["Sprint speed"].mean())#This is the population mean
bb=stratified["Sprint speed"].mean()#This is our stratified sanple mean.which is same.
'''    



#print(g)     
     
    #THE ABOVE CALCLUTES THE MEAN OF SPRINT SPEED PER AGE GROUP.AND AS WE CAN SEE
    #THAT AS YOU GET OLDER, THE MORE YOUR SPEED DECREASES AND THE YOUNGER YOU ARE THE MORE FASTER
#THE FOLLWING GETS DIFFERENT SAMPLE FROM THE SPRINT SPPED
'''



d=[]
for x in range(40):
    t5=data["Sprint speed"].sample(n=10,random_state=x).mean()
    d.append(t5)
print(d)
f2=data["Sprint speed"].mean()
plt.scatter(range(1,41), d)
plt.axhline(f2)
#wE NOTICE ONE THING.THAT THE HIGEER THE N IS(SAMPLE SIZE) THEN THE MORE REPRESENTAIVE THE SCATTER PLOT IS OF MEAN ACTAUL PIPULATION 

    


print(u,v,y,x,z)
print(o)
'''


