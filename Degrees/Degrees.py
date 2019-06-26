import pandas as pd
import matplotlib.pyplot as plt

#This program will make a matplotlib line plot.Looking at Percent of women and man in different degrees over the years.
#We want to find what degrees has highest number of women and man
#This will let us explain things such as in what degrees are women rising in

women_degrees = pd.read_csv('percent-bachelors-degrees-women-usa.csv')
#The following are the colors for the lines on our plots.And we made sure to make the colors suitable for the color blind as the developer suffer from vision issues
cb_dark_blue = (0/255,107/255,164/255)#Colors specific for color-blind.
cb_orange = (255/255, 128/255, 14/255)


#The following will be used to point to the different majors catagories
stem_cats = ['Engineering', 'Computer Science', 'Psychology', 'Biology', 'Physical Sciences', 'Math and Statistics']#(1)Majors
lib_arts_cats = ['Foreign Languages', 'English', 'Communications and Journalism', 'Art and Performance', 'Social Sciences and History']#(2)majors
other_cats = ['Health Professions', 'Public Administration', 'Education', 'Agriculture','Business', 'Architecture']#(3)majors



figx=plt.figure(figsize=(15,10))#Will create a figure
dark_blue = (0/255,107/255,164/255)#Colors specific for color-blind.
cb_orange = (255/255, 128/255, 14/255)
for x in range(0,6):#There are 6 items in the first list.We want to put the majors in order by first column have first list and second column second and so on
    ax=figx.add_subplot(6,3,3*x+1)#This will make a 6x3=18 subplots.We will place first list in first columns[which are 1,4,7,10,13,16.
    ax.plot(women_degrees["Year"],women_degrees[stem_cats[x]],c=dark_blue,label="Women",linewidth=3)#Will get women degrees.Linewidth will be wide
    ax.plot(women_degrees["Year"],100-women_degrees[stem_cats[x]],c=cb_orange,label="Men",linewidth=3)##Take away 100 from women degree will give men pecent

    if x==0:#0 mena the first subplot, which will put men and women text on its lines.
        ax.text(2005,75,"Men")#2005(x),75(y) is where we want the text men to be.This will make it more astehitcally pleasing
        ax.text(2005,30,"Women")#Same for women subplot.But note the x and y depends on where the subplots are whicha are different for each plot
    elif x==5:#We also want to do the same to the last subplot
        ax.text(2005,65,"Men")
        ax.text(2005,25,"Women")
        
    ax.set_title(stem_cats[x])#Will set the title for each subplot
    
    plt.tight_layout()#This will stop the subplots from overlapping and fix it in place
    
    ax.set_xlim(1968, 2011)#X limit will be this
    ax.set_ylim(0,100)#Y limit will be this
    
    ax.spines["right"].set_visible(False)#The spines are the lines.We want to remove all the lines.By doing the following  
    ax.spines["left"].set_visible(False)
    ax.spines["top"].set_visible(False)    
    ax.spines["bottom"].set_visible(False)
    
    ax.tick_params(bottom="off", top="off", left="off", right="off")# This will turn of ticks(where numbers goes) for all sides
    ax.set_yticks([0,100])#Will only show 0 and 100 to make it more astehically pleasaing
    ax.axhline(50, c=(171/255, 171/255, 171/255), alpha=0.3)#This will make an invisble line on 50.The color is given and alpha means how transparent.
    
for d in range(0,5):#This is for the second list. We do 5 cuz its only 5 in list. This is why we are doing three seperate loops
    ax=figx.add_subplot(6,3,3*d+2)#We want all the subplots for this list on the 2nd column.Thats the reason for the formula which is(2,4,6,8,10,12)
    ax.plot(women_degrees["Year"],women_degrees[lib_arts_cats[d]],c=dark_blue,label="Women",linewidth=3)
    ax.plot(women_degrees["Year"],100-women_degrees[lib_arts_cats[d]],c=cb_orange,label="Women",linewidth=3)
    
    plt.tight_layout()#THE INSTRUCTIONS ARE THE SAME AS FIRST FOR LOOP FOR THE REST.
    
    ax.set_title(lib_arts_cats[d])
    
    ax.set_xlim(1968, 2011)
    
    ax.set_ylim(0,100)
    
    if d==0:
        ax.text(2005,75,"Women")
        ax.text(2005,30,"Men")#Reason we only do text on first subplot is cuz the last one plots are joined in which dosent look astehthcally pleasing
        
    ax.spines["right"].set_visible(False)    
    ax.spines["left"].set_visible(False)
    ax.spines["top"].set_visible(False)    
    ax.spines["bottom"].set_visible(False)
    
    ax.tick_params(bottom="off", top="off", left="off", right="off")
    ax.set_yticks([0,100])
    
    ax.axhline(50, c=(171/255, 171/255, 171/255), alpha=0.3)
    
for d in range(0,6):#We want the 3rd list to be in the 3 column as it has 6 items
    ax=figx.add_subplot(6,3,3*d+3)#This is reason why we have 3 seperate loops cuz we want the different list to all be in one column.for this it is(3,6,9,12,15,18).
    ax.plot(women_degrees["Year"],women_degrees[other_cats[d]],c=dark_blue,label="Women",linewidth=3)
    ax.plot(women_degrees["Year"],100-women_degrees[other_cats[d]],c=cb_orange,label="Men",linewidth=3)
    
    plt.tight_layout(rect=[0, 0.003, 1, 0.95])#Will adjust the x,y,right,left.
    
    ax.set_title(other_cats[d])
    
    ax.set_xlim(1969, 2011)
    
    ax.set_ylim(0,100)
    
    if d==0:
        ax.text(2005,90,"Women")
        
        ax.text(2005,30,"Men")
    elif d==5:
        ax.text(2005,60,"Men")
        
        ax.text(2005,30,"Women")
        
    ax.spines["right"].set_visible(False)    
    ax.spines["left"].set_visible(False)
    ax.spines["top"].set_visible(False)    
    ax.spines["bottom"].set_visible(False)
    
    ax.tick_params(bottom="off", top="off", left="off", right="off")
    #plt.subplots_adjust(left=0.125 , bottom=0.00000001 , right=0.9, top=0.9 , wspace=None , hspace=None)
    ax.set_yticks([0,100])
    
    ax.axhline(50, c=(171/255, 171/255, 171/255), alpha=0.3)
    
plt.show() 






plt.get_backend()#Which version we are using
#figx.savefig("gender_degrees(real).png")#Saves thr subplots as png



# This is practise code 
'''
fig = plt.figure(figsize=(18, 3))##Creates a figure

for sp in range(0,6):
    ax = fig.add_subplot(1,6,sp+1)
    ax.plot(women_degrees['Year'], women_degrees[stem_cats[sp]], c=cb_dark_blue, label='Women', linewidth=3)
    ax.plot(women_degrees['Year'], 100-women_degrees[stem_cats[sp]], c=cb_orange, label='Men', linewidth=3)
    ax.spines["right"].set_visible(False)    
    ax.spines["left"].set_visible(False)
    ax.spines["top"].set_visible(False)    
    ax.spines["bottom"].set_visible(False)
    ax.set_xlim(1968, 2011)
    ax.set_ylim(0,100)
    ax.set_title(stem_cats[sp])
    ax.tick_params(bottom="off", top="off", left="off", right="off")
    
    if sp == 0:
        ax.text(2005, 87, 'Men')
        ax.text(2002, 8, 'Women')
    elif sp == 5:
        ax.text(2005, 62, 'Men')
        ax.text(2001, 35, 'Women')
plt.show()

'''
    




