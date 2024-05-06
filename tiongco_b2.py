import pandas as pd
import numpy as np


df=pd.read_csv('C:\\Users\\ennai\\OneDrive\\Desktop\\work\\BIO-191_Python-Drills\\mock_exam\\Dianne Rei Tiongco - Exam_Table.csv',dtype = object,sep=' *, *').dropna(how='all')

#Extract element from each component at specified position or with specified key.
Series.str.get(i)