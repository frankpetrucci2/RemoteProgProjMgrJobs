print ("Run the following program in *Type here to search* on a windows computer: cmd")

print ("Ask claude.ai how to install python or see the *How to install python on a windows 10 computer.txt file I have included.")

import requests
from datetime import datetime
from typing import List, Dict
import json

class AdzunaJobSearch:
    def __init__(self, app_id: str, app_key: str):
        self.app_id = app_id
        self.app_key = app_key
        self.base_url = "https://api.adzuna.com/v1/api/jobs/us/search/1"
    
    def search_jobs(self, what: str) -> List[Dict]:
        """
        Search for remote jobs using Adzuna API
        
        Args:
            what: Job title or keywords
        
        Returns:
            List of job postings
        """
        params = {
            'app_id': self.app_id,
            'app_key': self.app_key,
            'what': f"{what} remote",  # Add remote to search term
            'results_per_page': 100,
            'content-type': 'application/json'
        }
        
        try:
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()
            return response.json().get('results', [])
        except requests.exceptions.RequestException as e:
            print(f"Error fetching jobs: {e}")
            return []

    def is_remote_job(self, description: str, title: str) -> bool:
        """Check if job is truly remote by looking for keywords"""
        remote_keywords = ['remote', 'work from home', 'wfh', 'virtual', 'telework']
        text_to_check = (description + ' ' + title).lower()
        return any(keyword in text_to_check for keyword in remote_keywords)

    def format_job_details(self, jobs: List[Dict]) -> List[Dict]:
        """Format and clean job posting details"""
        formatted_jobs = []
        for job in jobs:
            description = job.get('description', '').lower()
            title = job.get('title', '').lower()
            
            # Only include jobs that are explicitly marked as remote
            if self.is_remote_job(description, title):
                formatted_job = {
                    'title': job.get('title', 'No title'),
                    'company': job.get('company', {}).get('display_name', 'Company not listed'),
                    'description': job.get('description', 'No description available'),
                    'salary': job.get('salary_max', 'Salary not specified'),
                    'url': job.get('redirect_url', ''),
                    'posted': datetime.strptime(job.get('created', ''), '%Y-%m-%dT%H:%M:%SZ').strftime('%Y-%m-%d')
                    if job.get('created') else 'Date not specified'
                }
                formatted_jobs.append(formatted_job)
        return formatted_jobs

def main():
    # Get API credentials from user input
    print ("********************************************************************")
    print ("Get this ID and Key from developer.adzuna.com")
    print ("********************************************************************")
    print ("Login to developer.adzuna.com")
    print ("Go to dashboard. You may need to create an ID and Key the first time.")
    print ("Select API Acess Details")
    print ("Copy the Application ID and Application Key to a text file in notepad")
    print ("********************************************************************")
    app_id = input("Enter your Adzuna APP_ID: ")
    app_key = input("Enter your Adzuna APP_KEY: ")
    
    # Initialize job search
    job_search = AdzunaJobSearch(app_id, app_key)
    
    # Search terms
    print (" ")
    print ("*****************************************************")
    print ("Add more or change job titles in the code in the next line below.")
    print ("*****************************************************")
    print (" ")
    search_terms = ["program manager", "project manager"]
    all_jobs = []
    
    # Search for each term
    for term in search_terms:
        print(f"\nSearching for remote {term} jobs...")
        jobs = job_search.search_jobs(term)
        formatted_jobs = job_search.format_job_details(jobs)
        all_jobs.extend(formatted_jobs)
        print(f"Found {len(formatted_jobs)} remote jobs for {term}")
    
    # Remove duplicates based on URL
    unique_jobs = {job['url']: job for job in all_jobs}.values()
    
    # Save results to JSON file
    output_file = 'remote_jobs.json'
    with open(output_file, 'w') as f:
        json.dump(list(unique_jobs), f, indent=2)
    
    print(f"\nTotal unique remote jobs found: {len(unique_jobs)}")
    print(f"Results saved to {output_file}")

if __name__ == "__main__":
    main()
