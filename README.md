# Quotes_Scraper
"Scraping Quotes from Website: [Quotes](https://quotes.toscrape.com/) with Python and Beautiful Soup"

This Git repository contains a Python script that utilizes the `requests` library and the `BeautifulSoup` library to scrape quotes from a website. The script is structured as a class called `QuotesScrape` and demonstrates web scraping techniques using the Model-View-Controller (MVC) architectural pattern.

The `start_request` method initiates the scraping process by making a GET request to the specified website URL. The `extract_data` method then extracts the desired data from the HTML content using `BeautifulSoup`. It retrieves the quotes, authors, and associated tags from the website and stores the extracted data in a list.

The script makes use of recursive calls to scrape multiple pages of quotes. It looks for a link to the next page using CSS selectors and constructs the URL for the next page. This process continues until all the available quotes have been extracted.

The extracted data is then written to a text file, where each quote is formatted with its corresponding author, tags, and page number.

This project serves as an example of how to scrape data from websites using Python and demonstrates the usage of libraries such as `requests` and `BeautifulSoup`. It can be a useful starting point for anyone interested in web scraping or working with similar data extraction scenarios.
