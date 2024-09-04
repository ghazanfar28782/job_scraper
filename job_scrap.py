# job_scrap.py

import requests
from bs4 import BeautifulSoup
from job import Job

class JobScrap:
    def __init__(self, url):
        self.url = url

    def scrape_jobs(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, 'html.parser')
        jobs = []
        
        for job_listing in soup.find_all('div', class_='job-listing'):
            title = job_listing.find('h2').text.strip()
            company = job_listing.find('span', class_='company').text.strip()
            location = job_listing.find('span', class_='location').text.strip()
            job = Job(title, company, location)
            jobs.append(job)
        
        return jobs
