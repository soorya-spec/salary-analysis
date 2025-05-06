# Introduction
The dataset from ABC company, consisting of 458 rows and 9 columns ,The project requires a comprehensive
report detailing information about their employees across various teams.

## Project Objective
To perform a comprehensive salary analysis and build a compelling data story using data visualization and statistical insights.

##Dataset
real-world data ,consisting of 458 rows and 9 columns

##Features:**
#NAME
TEAM
AGE
POSITION
HEIGHT
WEIGHT
SALARY
##  Tools

- Python (Pandas, NumPy, Matplotlib, Seaborn, Plotly)

#Methods
preprocessing the dataset, analyzing the data, and presenting your
findings graphically.

##Key Insights
as in the stage of data pre-processing , I have checked the data types of all columns and found that height is missing, then I checked the height column and replace it with random integers.

while checking the values found that 
College    84 missing values
Salary     11 missing values, I have replaced the missing values - College =notfilled and salary with mean

no duplicated values found in all columns

analysis shows , equal employee representation, likely because the dataset is balanced (same number of players per team).

Found that the  Team, Cleveland Cavaliers  has the highest salary  1.118227e+08 
Team  ,Brooklyn Nets  1500000.0   has the highest sal and the position is  SGPG

Correlation Value: ≈ 0.21
This is a weak positive correlation.
It means: as age increases, salary tends to increase — but the relationship is not very strong.
There is some connection between age and salary — possibly because more experienced (older) employees earn slightly more.
But since the value is close to 0, age doesn't strongly predict salary.

##Visualization
Using pie chart and bar charts , scatterplots for representing the data

##CONCLUSION

The data is showing the team spends significantly by position not as age , we can suggest consider performance as a metrics.


