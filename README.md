# Job Scraper

This is a Python application that scrapes job listings from a given website and saves them to a CSV file.

## Project Structure

The project is organized into the following files:

### 1. `job.py`

Defines the `Job` class, which represents an individual job with the following attributes:

- `title`: The title of the job.
- `company`: The company offering the job.
- `location`: The location of the job.

Getters and setters are provided for each attribute.

### 2. `job_scraper.py`

Contains the `JobScraper` class, which is responsible for scraping job listings from a provided URL.

### 3. `csv_handler.py`

Contains the `CSVHandler` class, which is responsible for saving the scraped jobs to a CSV file.

### 4. `main.py`

This script is the entry point of the application. It initializes the job scraper, scrapes the jobs, and saves them to a CSV file.

## Getting Started

### Prerequisites

- Python 3.6 or higher
- Required libraries: `requests`, `beautifulsoup4`

### Installation

1. Clone the repository:

```bash
git clone https://github.com/ghazanfar28782/job_scraper
cd job-scraper
pip install -r requirements.txt
python main.py

```
