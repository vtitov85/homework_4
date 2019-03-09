#!/usr/bin/env python
# coding: utf-8

# In[413]:


import pandas as pd
import numpy as np


# In[414]:


school_data_to_load = "Desktop/desktop/homework_4/homework_4/schools_complete.csv"
student_data_to_load = "Desktop/desktop/homework_4/homework_4/students_complete.csv"


# In[415]:


school_data = pd.read_csv(school_data_to_load)
student_data = pd.read_csv(student_data_to_load)


# In[416]:


school_data_complete = pd.merge(student_data, school_data, how="left", on=["school_name", "school_name"])


# In[417]:


school_data_complete.head()


# In[418]:


total_schools = school_data_complete['school_name'].nunique()


# In[419]:


total_schools


# In[420]:


student_count = school_data_complete['student_name'].count()


# In[421]:


student_count


# In[422]:


total_budget = school_data['budget'].sum()


# In[423]:


total_budget


# In[424]:


avg_math_score = school_data_complete['math_score'].mean()


# In[425]:


avg_math_score


# In[426]:


avg_reading_score = school_data_complete['reading_score'].mean()


# In[427]:


avg_reading_score


# In[428]:


overall_avg_score = (avg_math_score + avg_reading_score) / 2


# In[429]:


overall_avg_score


# In[430]:


pass_math = school_data_complete['math_score'][school_data_complete['math_score']>= 70].count()


# In[431]:


pass_math


# In[432]:


pass_math_perc = pass_math / student_count * 100


# In[433]:


pass_math_perc


# In[434]:


pass_reading = school_data_complete['reading_score'][school_data_complete['reading_score']>= 70].count()


# In[435]:


pass_reading


# In[436]:


pass_reading_perc = pass_reading / student_count * 100


# In[437]:


pass_reading_perc


# In[438]:


district_summary = pd.DataFrame ({"Total Schools": [total_schools], "Total Students": [student_count],                                   "Total Budget": [total_budget], "Average Math Score": [avg_math_score],                                   "Average Reading Score": [avg_reading_score], "% Passing Math": [pass_math_perc],                                   " % Passing Reading": [pass_reading_perc], "% Overall Passing Rate": [overall_avg_score]})


# In[439]:


district_summary


# In[440]:


school_summary = school_data[["school_name", "type", "size", "budget"]]   
school_summary = school_summary.sort_values('school_name')
school_summary.head()


# In[441]:


per_student_budget = school_summary["budget"] / school_summary["size"]
school_summary["Per Student Budget"] = per_student_budget
school_summary.info()


# In[442]:


grouped_student_data = school_data_complete.groupby(['school_name'])
grouped_student_data.head()


# In[443]:


avg_math_score_1 = grouped_student_data["math_score"].mean()
avg_math_score_1.head()


# In[444]:


avg_read_score_1 = grouped_student_data["reading_score"].mean()
avg_read_score_1.head()


# In[445]:


passing_math_1 = school_data_complete[school_data_complete['math_score']>= 70].groupby("school_name")["school_name"].count()


# In[446]:


passing_math_1


# In[447]:


student_count_per_school = school_data_complete.groupby("school_name")["school_name"].count()


# In[448]:


student_count_per_school


# In[449]:


passing_math_school_summary= passing_math_1 / student_count_per_school * 100


# In[450]:


passing_math_school_summary


# In[451]:


passing_read_1 = school_data_complete[school_data_complete['reading_score']>= 70].groupby("school_name")["school_name"].count()


# In[452]:


passing_read_1


# In[453]:


reading_pass_school_summary = passing_read_1 / student_count_per_school * 100


# In[454]:


reading_pass_school_summary


# In[455]:


overall_passing_rate = (passing_math_school_summary + reading_pass_school_summary) /2


# In[456]:


overall_passing_rate


# In[457]:


school_summary.set_index(["school_name"],inplace=True)


# In[ ]:





# In[458]:


school_summary["Average Math Score"] = grouped_student_data["math_score"].mean()
school_summary["Average Reading Score"] = avg_read_score_1
school_summary["% Passing Math"] = passing_math_school_summary
school_summary["% Passing Reading"] = reading_pass_school_summary
school_summary["% Overall Passing Rate"] = overall_passing_rate
school_summary.head()


# In[459]:


top_performing = school_summary.sort_values("% Overall Passing Rate", ascending=False)


# In[460]:


top_performing.head()


# In[461]:


worst_performing = school_summary.sort_values("% Overall Passing Rate")


# In[462]:


worst_performing.head()


# In[463]:


math_9 = student_data.loc[student_data["grade"] == "9th", "grade":"math_score"]

math_9.count()


# In[464]:


math_10 = student_data.loc[student_data["grade"] == "10th", "grade":"math_score"]

math_10.count()


# In[465]:


math_11 = student_data.loc[student_data["grade"] == "11th", "grade":"math_score"]

math_11.count()


# In[466]:


math_12 = student_data.loc[student_data["grade"] == "12th", "grade":"math_score"]

math_12.count()


# In[467]:


grouped_math_9 = math_9.groupby(['school_name'])
grouped_math_9['math_score'].mean()


# In[468]:


grouped_math_10 = math_10.groupby(['school_name'])
grouped_math_10['math_score'].mean()


# In[469]:


grouped_math_11 = math_11.groupby(['school_name'])
grouped_math_11['math_score'].mean()


# In[470]:


grouped_math_12 = math_12.groupby(['school_name'])
grouped_math_12['math_score'].mean()


# In[471]:


math_by_grade = pd.DataFrame({'9th': grouped_math_9['math_score'].mean(),'10th': grouped_math_10['math_score'].mean(),'11th': grouped_math_11['math_score'].mean(),'12th': grouped_math_12['math_score'].mean()})


# In[472]:


math_by_grade


# In[473]:


read_9 = student_data.loc[student_data["grade"] == "9th", "grade":"reading_score"]
read_10 = student_data.loc[student_data["grade"] == "10th", "grade":"reading_score"]
read_11 = student_data.loc[student_data["grade"] == "11th", "grade":"reading_score"]
read_12 = student_data.loc[student_data["grade"] == "12th", "grade":"reading_score"]


# In[474]:


grouped_read_9 = read_9.groupby(['school_name'])
grouped_read_9['reading_score'].mean()


# In[475]:


grouped_read_10 = read_10.groupby(['school_name'])
grouped_read_10['reading_score'].mean()


# In[476]:


grouped_read_11 = read_11.groupby(['school_name'])
grouped_read_11['reading_score'].mean()


# In[477]:


grouped_read_12 = read_12.groupby(['school_name'])
grouped_read_12['reading_score'].mean()


# In[478]:


read_by_grade = pd.DataFrame({'9th': grouped_read_9['reading_score'].mean(),'10th':grouped_read_10['reading_score'].mean(),'11th': grouped_read_11['reading_score'].mean(),'12th':grouped_read_12['reading_score'].mean()})


# In[479]:


read_by_grade


# In[480]:


school_spending = school_summary [["Average Math Score", "Average Reading Score",                                   "% Passing Math", "% Passing Reading", "% Overall Passing Rate"]] 


# In[481]:


spending_bins = [0, 585, 615, 645, 675]
group_names = ["<$585", "$585-615", "$615-645", "$645-675"]


# In[482]:


school_spending["Spending Ranges (Per Student)"] = pd.cut(school_summary['Per Student Budget'], spending_bins,                                              labels = group_names)


# In[483]:


school_spending


# In[484]:


spending_group= school_spending.groupby("Spending Ranges (Per Student)")
spending_group.mean()


# In[485]:


size_bins = [0, 1000, 2000, 5000]
group_names_1 = ["Small (<1000)", "Medium (1000-2000)", "Large (2000-5000)"]


# In[486]:


school_spending["School Size"] = pd.cut(school_summary['size'], size_bins,                                              labels = group_names_1)


# In[487]:


school_spending


# In[488]:


size_group= school_spending.groupby("School Size")
size_group.mean()


# In[489]:


school_type = school_summary["type"]
school_spending ["School Type"] = school_summary["type"]
school_spending


# In[490]:


type_group= school_spending.groupby("School Type")
type_group.mean()


# In[ ]:





# In[ ]:




