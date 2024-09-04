# csv_handler.py

import csv
from job import Job

class CSVHandler:
    def __init__(self, filename="jobs.csv"):
        self.filename = filename

    def save_to_csv(self, jobs):
        with open(self.filename, 'w', newline='') as output_file:
            dict_writer = csv.DictWriter(output_file, fieldnames=['title', 'company', 'location'])
            dict_writer.writeheader()
            for job in jobs:
                dict_writer.writerow({
                    'title': job.title,
                    'company': job.company,
                    'location': job.location
                })
