import plotly.express as px
import csv
import numpy as np

def plotFigure(data_path):
    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)
        fig = px.scatter(df,x="Size of TV", y="Time")
        fig.show()

def getDataSource(data_path):
    sizeoftv = []
    avgtime = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            sizeoftv.append(float(row["Size of TV"]))
            avgtime.append(float(row["Time"]))

    return {"x" : sizeoftv, "y": avgtime}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between Size of TV vs Time :-  \n--->",correlation[0,1])

def setup():
    data_path  = "./data/Size of TV,_Average time spent watching TV in a week (hours).csv"

    datasource = getDataSource(data_path)
    findCorrelation(datasource)
    plotFigure(data_path)

setup()

#correlation- -1 to 1. -1 is inversely correlated, 1 is highly correlated, 0-no correlation