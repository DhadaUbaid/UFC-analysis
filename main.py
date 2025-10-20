import numpy as np
import pandas as pd
from datetime import date as dt

#creating a pandas dataframe by reading the excel file data 
df = pd.read_excel("E:/Python_projects/Data Analyst/UFC analysis/ufc-master.xlsx")


# checking the favourites and underdogs 
red_underdog = df['RedOdds'].idxmax()  
red_fav = df['RedOdds'].idxmin()

blue_underdog = df['BlueOdds'].idxmax()
blue_fav = df['BlueOdds'].idxmin()

print("Biggest Fan favourite and underdog Red Fighters")
print(df.loc[red_fav],'\n')
print(df.loc[red_underdog],'\n')

print("Biggest Fan favourite and underdog Blue Fighters")
print(df.loc[blue_fav],'\n')
print(df.loc[blue_underdog],'\n')


#gives columns names
print(df.columns,'\n')


#prints information about the dataframe
print(df.info,'\n')


#checking the fighter's winning streak
sort = df.sort_values(by='BlueCurrentWinStreak', ascending=False)  
print("Blue Fighters Highgest Winnig streak")
print(sort[['BlueFighter', 'BlueCurrentWinStreak']].head(), '\n')


sort_ = df.sort_values(by='RedCurrentWinStreak', ascending=False)
print("Red Fighters Highgest Winnig streak",'\n')
print(sort[['RedFighter','RedCurrentWinStreak']].head(),'\n')


#gives the statistical infomation for Red and Blue fighters average strikes landed
print("Blue Average Strike Landed Details: ")
print(df['BlueAvgSigStrLanded'].mean())
print(df['BlueAvgSigStrLanded'].max())
print(df['BlueAvgSigStrLanded'].min())

print("Red Average Strike Landed Details: ")
print(df['RedAvgSigStrLanded'].mean())
print(df['RedAvgSigStrLanded'].max())
print(df['RedAvgSigStrLanded'].min())


#filtering the dataset to retrieve the fighters with the highest average signature strikes landed 
print("Which Fighter Has the hightest average for strikes landed: ")
print(df.loc[df['BlueAvgSigStrLanded'].idxmax()],'\n')
print(df.loc[df['RedAvgSigStrLanded'].idxmax()],'\n')


#filtering and couting the fights that were title fights
print("How Many title fights have taken place: ")
print(df[df['TitleBout'] == True].shape[0],'\n')  


# filtering the youngest fighters 
print("Finding out the youngest fighters: ")
print(df.loc[df['RedAge'].idxmin(), ['RedFighter','RedAge']],'\n')
print(df.loc[df['BlueAge'].idxmin(), ['BlueFighter','BlueAge']],'\n')
print(df.loc[df['RedAge'].idxmin()],'\n')
print(df.loc[df['BlueAge'].idxmin()],'\n')


#fight with the biggest age difference
print("Fight that had the biggest age difference: ")
print(df['AgeDif'].max(),'\n')
print(df.loc[df['AgeDif'].idxmax()],'\n')

#using query to check the fights with the title on the line where the fight was finished by a specific finish , KO/TKO, SUB, U-DEC
finish_check = "SUB"
print("Checking the fights that ended with a specific Finish(can change the Finish Type)")
print(df.query('TitleBout == True and Finish == @finish_check'),'\n')


#filtering to check the number of fights that ended with a specific finish like spinnig kick, elbows.
specific_finish = "Elbows"
print("Fights that finished with a elbow finish: ")
print(df[df['FinishDetails'] == specific_finish].count(),'\n')  


#checking the total number of fights in the division
print("Checking total fights Division Wise")
print(df['WeightClass'].value_counts(),'\n')


#checking how many times a fighter has fought in the UFC
fighter_name = "Ilia Topuria"
condition = (df['RedFighter'] == fighter_name) | (df['BlueFighter'] == fighter_name)
print(f"How Many times has {fighter_name} Fought in the UFC")
print(condition.value_counts(),'\n')


#counting how many fights happened in a specific year, which year had the most/less fights can also be found using min/max
df['Date'] = pd.to_datetime(df['Date'])
fight_per_year = (df['Date'].dt.year.value_counts().sort_index())
print("counting how many fights happened in a specific year")
print(fight_per_year,'\n')

print("maximum number of fights")
print(fight_per_year.max(),'\n')

print("Least number of fights")
print(fight_per_year.min(),'\n')

#finding the fighter with the most number of knockouts
print("Fighters With the Most KO's: ")
blue_max_KO = df.loc[df['BlueWinsByKO'].idxmax(),['BlueFighter','BlueWinsByKO','WeightClass']]
print(blue_max_KO,'\n')

red_max_KO = df.loc[df['RedWinsByKO'].idxmax(), ['RedFighter', 'RedWinsByKO', 'WeightClass']]
print(red_max_KO,'\n')


#getting all the favourites from both the fighters
favourites = df.query('RedOdds < 0 and BlueOdds < 0')
print("Getting all the favourites: ")
print(favourites,'\n')


#checking how many times underdogs won agains favoutires
df['BeatTheOdds']=((df['RedOdds'] > 0 ) & (df['Winner'] == 'Red') | (df['BlueOdds'] > 0) & (df['Winner'] == 'Blue'))
print(df.query('BeatTheOdds == True')[['RedFighter', 'BlueFighter', 'RedOdds', 'BlueOdds', 'Winner']], '\n')   
print("How many Times Underdogs won") 
print(df['BeatTheOdds'].sum(),'\n')


#counting how many from a specifc nation fought in total and in a specific year
country = "Canada"
print(f"Fighters from {country}")
print('\n',df.query('Country==@country').value_counts)


#checking to see which fighter has the most finishes
df['most_finish_red'] = df['RedWinsByKO'] + df['RedWinsBySubmission'] + df['RedWinsByTKO'] 
red_most_finish = df.loc[df['most_finish_red'].idxmax(), ['RedFighter', 'most_finish_red']]

df['most_finish_blue'] = df['BlueWinsByKO'] + df['BlueWinsBySubmission'] + df['BlueWinsByTKO'] 
blue_most_finish = df.loc[df['most_finish_blue'].idxmax(), ['BlueFighter', 'most_finish_blue']]

print("Fighters With The Most Finishes")
print('\n',red_most_finish)
print('\n',blue_most_finish)