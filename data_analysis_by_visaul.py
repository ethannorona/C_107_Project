#Importing needed modules
import csv
import pandas as pd
import plotly.express as px

#Reading csv file
df = pd.read_csv("data.csv")

#Setting the mean by attempts for each student_id in every level  |  as_index = False, convert series of the data to data frames
mean = df.groupby(["student_id", "level"], as_index = False)["attempt"].mean()

#Creating graph as a scatter graphy | x is equal to the id, y is equal to the level, size and color are set to the attempt
fig = px.scatter(mean, x="student_id", y="level", size="attempt", color="attempt")

#Showing graph
fig.show()