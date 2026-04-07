# Importing Libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Making Connection
url = 'https://internshala.com/jobs/ai-agent-development,artificial-intelligence-ai,data-science,machine-learning-jobs/page-1'
response = requests.get(url=url)

# Columns
Role = []
Location = []
Experience = []
Company = []
Skills = []
Description = []
Link = []
Salary = []
Posting = []
Source = []

# Scraping
for i in range(1,20):
    # Scraping over the pages
    url = 'https://internshala.com/jobs/ai-agent-development,artificial-intelligence-ai,data-science,machine-learning-jobs/page-' + str(i)
    response = requests.get(url=url)
    data = response.text
    soup = BeautifulSoup(data,'html.parser')
    # Jobs
    jobs = soup.find_all('div',class_='container-fluid individual_internship view_detail_button visibilityTrackerItem')

    for job in jobs:
        r = job.find('h2',class_='job-internship-name')
        c = job.find('p',class_='company-name')
        l = job.find('p',class_='row-1-item locations')
        e = job.find_all('div',class_='row-1-item')
        s = job.find('div',class_='job_skills')
        d = job.find('div',class_='text')
        sal = job.find('span',class_='desktop')
        p = job.find('div',class_='color-labels')
        lk = job['data-href']
        if r and l and e and c and s and sal and lk :
            Role.append(r.get_text().strip())
            Company.append(c.get_text().strip())
            Location.append(l.get_text().strip())
            Experience.append(e[1].get_text().strip())
            Skills.append(s.get_text().strip())
            Description.append(d.get_text().lstrip())
            Salary.append(sal.get_text().strip())
            Posting.append(p.find('span').get_text().strip())
            Link.append(lk.strip())
            Source.append('Internshala')

# DataFrame
raw_1 = pd.DataFrame(
    {
        'job_title':Role,
        'company_name':Company,
        'location':Location,
        'experience':Experience,
        'salary':Salary,
        'skills':Skills,
        'posted_time':Posting,
        'job_description':Description,
        'job_link':Link,
        'source':Source
    }
)

# CSV FILE
raw_1.to_csv('job_raw.csv',index=False)