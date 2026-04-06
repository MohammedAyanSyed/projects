# Importing Libraries
import numpy as np
import pandas as pd

# Importing CSV File
file = pd.read_csv('C:\\Users\\Mohammed Ayan Syed\\Downloads\\Raw_1.csv')

# Null Check
null = file.isnull().sum()
# print(null)

# Handling Null Values
file.fillna({'skills':'Not Specified'},inplace=True)
null2 = file.isnull().sum()
# print(null2)

# Removing unnecessary texts
file['salary'] = file['salary'].replace(to_replace=['₹',','],value='',regex=True)
file['location'] = file['location'].replace(to_replace='work from home',value='remote',regex=True)
file['experience'] = file['experience'].replace(to_replace='year\(s\)',value='',regex=True)
file['experience'] = file['experience'].replace(to_replace='No experience required',value=0,regex=True)
file['experience'] = file['experience'].astype(int)

# Standardizing Text
cols = file.select_dtypes(exclude=int).columns.to_list()
for i in cols:
    file[i] = file[i].str.lower()

# Unique Jobs Only
file.drop_duplicates(inplace=True)

# Filtering AI/ML/DATA jobs
jobs_list = ['data','artificial intelligence','machine learning','ai','ml','data analyst',
             'nlp','llm','computer vision','deep learning','scientist']
skill = ['data','machine learning','dl','llm','nlp','sql','deep learning']
file = file[file['job_title'].str.contains('|'.join(jobs_list))
            | file['skills'].str.contains('|'.join(skill))]
print(len(file))

# Saving CSV File
file.to_csv('jobs_cleaned.csv',index=False)