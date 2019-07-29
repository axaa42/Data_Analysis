import pandas as pd

df=pd.read_csv("CompleteDataset.csv",low_memory=False)

#The follwoing will see what is the probaltiy of getting people aged 21 in our dataset

total=df["Age"].shape[0]#This find the total. as formula is events/total_amount
condition=df[df["Age"]==18].shape[0]#Our condition 
condition1=df[df["Age"]==19].shape[0]

prob_of_21=(condition/total) +(condition1/total)#Now we divide.We wuold minus by the  two conditons having same thing at once.but here they do not as they are exlcusive
print(total)
print(condition)
print(prob_of_21*100)
d=condition1/total
print(d*100)


