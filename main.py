
# coding: utf-8

# In[122]:


import pandas
import math

get_grade= [[] for i in range(8)]
get_credit= [[] for i in range(8)]
get_subject= [[]for i in range(8)]
def get_data():
    data = pandas.read_csv("gpa.csv", skip_blank_lines=True)
    count_term = 0
    count_rows = 0
    data_credit = data["Unnamed: 2"]
    data_grade = data["Unnamed: 5"]
    data_subject = data["ปีการศึกษา 2558 ภาคการศึกษาที่ 1"]
    for grade in data_grade:
        if grade == "grade":
            count_term +=1
        elif not(math.isnan(float(grade))):
            get_grade[count_term - 1].append(grade)
            get_credit[count_term - 1].append(data_credit[count_rows])
            get_subject[count_term - 1].append(data_subject[count_rows])
        count_rows +=1 
    show_data()
        
def show_data():    
    sum_grade = 0
    sum_credit = 0
    for i in range(len(get_grade)):
        print("Term" , i + 1 )
        sum_grade_term = 0
        sum_credit_term = 0
        for j in range(len(get_grade[i])):
            print(get_subject[i][j],"------>" ,get_grade[i][j])
            sum_grade_term += float(get_grade[i][j]) * float(get_credit[i][j])
            sum_credit_term += float(get_credit[i][j])
        if sum_credit_term != 0:
            print("GPA :",(round(sum_grade_term / sum_credit_term, 2)))
        else:
            print("Not Result")
        sum_grade += sum_grade_term
        sum_credit += sum_credit_term
        print("--------------------------------------------------------------")
    print("Result All Term(GPAX)  : ", round(sum_grade / sum_credit, 2))

get_data()


# In[3]:


data[:5]

