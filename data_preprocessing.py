#Data preprocessing
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df= pd.read_excel("C:/Users/gokul/OneDrive/Desktop/capstone_module1/ABC Company.xlsx")
print(df.head(450))
print(df.columns)
print(df.dtypes)
print(df['Height'].head())
np.random.seed(0)
df['Height']=np.random.randint(150,181,size=len(df))
print(df['Height'].head(458))
print(df.dtypes)
#checking for missing values
print(df.isnull().sum())
#found the missing values in the columns, College   has 84  and Salary  has   11, so replacing it with other values
#df['College'].fillna('Not filled',inplace=True)
df.fillna({'College':'NotFilled'},inplace=True)
print(df.info())
print(df.isnull().sum())
df['Salary'] = df['Salary'].fillna(df['Salary'].mean())
print(df.isnull().sum())
#checking the duplicates
#print(df.duplicated().sum())
print(df[df.duplicated(subset=['Name', 'Team'])])


#Determine the distribution of employees across each team and calculate
#the percentage split relative to the total number of employees.

#print(df['Team'].unique())
#Displaying the team names from the column team
#for teams in df['Team'].unique():
    #print(teams)

#the distribution of employees across each team
employees_each_team=df['Team'].value_counts()
print(employees_each_team)

"""Visualizing of Determine the distribution of employees across each team and calculate
the percentage split relative to the total number of employees, using pie chart """

pie_chart_rep=np.array(employees_each_team)
plt.pie(pie_chart_rep)
plt.title("Distribution of Employees across each team")
plt.show()
plt.legend()


#percentage of employees in each team, relative to the total number of employees.

employee_team_percentage=df['Team'].value_counts(normalize=True).round(2) * 100
employee_team_percentage = employee_team_percentage.astype(str) + '%'
print(employee_team_percentage)

#Segregate employees based on their positions within the company

employees_positions_team=df['Position'].value_counts()
print(employees_positions_team)
employees_positions_team=df['Position'].value_counts(normalize=True).round(2) * 2
employees_positions_team=employees_positions_team.astype(str) +'%'
print(employees_positions_team)

sns.countplot(data=df, y='Position', order=df['Position'].value_counts().index)
plt.title("Employee Count by Position")
plt.xlabel("Number of Employees")
plt.ylabel("Position")
plt.show()


#Identify the predominant age group among employees.

bins=[20,30,40,50,60,100]
labels=['20-30','31-40','41-50','51-60','60+']
df['age group'] = pd.cut(df['Age'],bins=bins,labels=labels,right=False)
age_group_counts=df['age group'].value_counts()
print(age_group_counts)

sns.barplot(x=age_group_counts.index, y=age_group_counts.values)
plt.title("Employee Count by Age Group")
plt.xlabel("Age Group")
plt.ylabel("Count")
plt.show()

#Discover which team and position have the highest salary expenditure
team_highest_salary=df.groupby('Team')['Salary'].sum().sort_values(ascending=False)
print(team_highest_salary)
print(team_highest_salary.head(1))

highest_salary_position=df.groupby(['Team','Salary'])['Position'].sum().sort_values(ascending=False)
print(highest_salary_position)
print(highest_salary_position.head(1))

# Investigate if there's any correlation between age and salary
correlation=df['Age'].corr(df['Salary'])
print("The correlation between age and salary is ", correlation)

#Visual representation of the correlation
sns.scatterplot(data=df, x='Age', y='Salary')
sns.regplot(data=df, x='Age', y='Salary', line_kws={"color": "red"})
plt.title('Age vs Salary')
plt.show()

