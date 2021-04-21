import pandas as pa
import plotly.express as pe

df = pa.read_csv("data1.csv")
figure = pe.scatter(df, x = "Student Number", y = "Marks")
figure.update_layout(shapes = [dict(type = "line", y0 = 75, x0 = 0, y1 = 75, x1 = 30)])

df2 = pa.read_csv('data2.csv')
figure2 = pe.scatter(df2, x = "Student Number", y = "Marks")
figure2.update_layout(shapes = [dict(type = "line", y0 = 75, x0 = 0, y1 = 75, x1 = 30)])
figure2.update_yaxes(rangemode = "tozero")

figure.show()
figure2.show()
