import re, collections as collec
import pandas as pd

words = []
dict1 = {}


filename ='C:\\Users\\ennai\\OneDrive\\Desktop\\work\\BIO-191_Python-Drills\\mock_exam\\Dianne Rei Tiongco - Exam_Table.csv'


df=pd.read_csv('C:\\Users\\ennai\\OneDrive\\Desktop\\work\\BIO-191_Python-Drills\\mock_exam\\Dianne Rei Tiongco - Exam_Table.csv'
, dtype = object).dropna(how='all') 
intervalcol=df["Interval"]

for i in intervalcol:
    x = i.split()
    for j in x:
        words.append(j) 


output = open(f"{filename}_output.txt", "r")   
content = output.read()
print(content)
output.close()