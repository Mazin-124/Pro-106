import plotly.express as px
import csv
import numpy as np

def plotFigure(data_path):
    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)
        fig = px.scatter(df,x="Size of TV", y="Average_Time")
        fig.show()

def getDataSource(data_path):
    size_of_tv = []
    average_time_spent = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            average_time_spent.append(float(row["Average_Time"]))
            size_of_tv.append(float(row["Size of TV"]))
            
    return {"x" : size_of_tv, "y": average_time_spent}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between Size of TV vs Average time spent watching TV in a week (hours) :-  \n--->",correlation[0,1])

def setup():
    data_path  = "\Student Marks vs Days Present.csv"

    datasource = getDataSource(data_path)
    findCorrelation(datasource)
    plotFigure(data_path)

setup()