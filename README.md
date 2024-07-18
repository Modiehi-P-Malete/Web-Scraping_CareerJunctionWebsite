# Web-Scraping_CareerJunctionWebsite
 This Python application scrapes job listings from CareerJunction for software engineering positions based on user-defined search terms. It extracts job title, recruiter names, salary, position, location, and date posted from the first page of search results and saves the data into a CSV file.

Requirements:
Python 3.x
Requests library
BeautifulSoup4 library
Pandas library

Features:
Dynamically constructs URLs based on user input for job title searching.
Uses BeautifulSoup for HTML parsing and extraction of job data.
Handles multiple pages of search results by iterating over page numbers.
Saves scraped data into a structured CSV format for easy analysis, sharing and usage(yes, you can use it to search for jobs you might be interested in if you wish to).


Example:
If you search for "Software Engineer", the script will scrape the first page of CareerJunction's search results for software engineering jobs and save the data into a CSV file named Software_Engineer_job-results.csv.

Notes:
Ensure that you have a stable internet connection while running the script to fetch data from CareerJunction.
The CSV file will be created or overwritten each time you run the script, so ensure you save or rename it with the correct page number if needed.
