import pandas as pd
import numpy as np

def maxTwo(a,b,c):  
    if a > b:
        p = a
        if b > c:
            q = b
        else:
            q = c
    else:
        p = b
        if a > c:
            q = a
        else:
            q = c
    return p,q

def addTotalScore(de): 
    totalScores = []
    for index, row in de.iterrows():
        
        score = 0
        
        qmax1, qmax2 = maxTwo(row['Q1'],row['Q2'],row['Q3'])
        tmax1, tmax2 = maxTwo(row['T1'],row['T2'],row['T3'])
        score = qmax1+qmax2+tmax1+tmax2+row['Ex1']+row['Ex2']
        score = round(score)
        
        totalScores.append(score)
    de['Total Score'] = totalScores
    

def addGrade(de):
    grades = []
    
    for index,row in de.iterrows():
        x = row['Total Score']
        
        if 90 <= x <= 100:
            i = "A"
        elif 80 <= x <= 89:
            i = "B"
        elif 70 <= x <= 79:
            i = "C"
        elif 60 <= x <= 69:
            i = "D"
        else:
            i = "F"
        grades.append(i)
    de['Grade'] = grades
    

de = pd.read_csv("student_data.csv")  
addTotalScore(de)
addGrade(de)
de.to_csv("graded_data.csv") 



