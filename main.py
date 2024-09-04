# main.py

from job_scrap import JobScrap
from csv_handler import CSVHandler

def main():
    url = ''  # Replace with the actual job listing URL
    scraper = JobScraper(url)
    jobs = scraper.scrape_jobs()

    csv_handler = CSVHandler("jobs.csv")
    csv_handler.save_to_csv(jobs)

    print(f"Scraped {len(jobs)} jobs and saved to jobs.csv")

if __name__ == "__main__":
    main()
