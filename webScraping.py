#Web Scraping the CareerJuction website for Software Engineering jobs

import requests
from bs4 import BeautifulSoup
import pandas as pd

def extract(page):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
    }
    
    url = f'https://www.careerjunction.co.za/jobs/results?keywords=Software+Engineer&autosuggestEndpoint=%2Fautosuggest&location=2747&category=16&btnSubmit=+&page={page}'
    r = requests.get(url, headers=headers)
    
    if r.status_code != 200:
        print(f"Failed to retrieve data: {r.status_code}")
        return None
    
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup

def transform(soup):
    if not soup:
        print("Soup object is non-existent")
        return
    
    job_listings = soup.find_all('div', class_='module job-result')
    job_data = []
    # Extracting the Job Titles
    for job in job_listings:
        job_title = job.find('div', class_='job-result-title').find('a').text.strip() if job.find('div', class_='job-result-title') else 'N/A'
        
        # Extracting Recruiter Names 
        recruiters = job.find_all('div', class_='job-result-title')
        recruiter_names = []
        for recruiter in recruiters:
            recruiter_name = recruiter.find('h3').find('a').text.strip() if recruiter.find('h3') else 'N/A'
            recruiter_names.append(recruiter_name)
        
        # Joining multiple recruiter names into a single string for a cleaner storage & presentaion of my data (in the CSV file)
        recruiter_names_str = ', '.join(recruiter_names)
        
        # Extracting the Job Salaries
        job_salary = job.find('li', class_='salary').text.strip() if job.find('li', class_='salary') else 'N/A'
        
        #Extracting the Job Positions
        job_position = job.find('li', class_='position').text.strip() if job.find('li', class_='position') else 'N/A'
        
        # Extracting the Job Location
        job_location = job.find('li', class_='location').text.strip() if job.find('li', class_='location') else 'N/A'
        
        # Extracting the Date in which the job(s) were posted
        date_posted = job.find('li', class_='updated-time').text.strip() if job.find('li', class_='updated-time') else 'N/A'
        
        job_data.append({
            'Title': job_title,
            'Recruiter': recruiter_names_str,
            'Salary': job_salary,
            'Position': job_position,
            'Location': job_location,
            'Date Posted': date_posted
        })
    
    return job_data

# Creating the dataframe with the above information
def save_to_csv(job_data, filename):
    df = pd.DataFrame(job_data)
    df.to_csv(filename, index=False)
    print(f"Data saved to {filename}")

# You can choose whatever page number you'd like to view and save to your csv file(from number 1-9, for the Software Engineering search prompt)
page = 1
soup = extract(page)
job_data = transform(soup)

# Remember to include the 'page number' before the ".csv" in order to keep track of your pages
if job_data:
    save_to_csv(job_data, "Software_Engineer_job_results.csv")
