import requests
from bs4 import BeautifulSoup


class QuotesScrape:
    data = []  # List to store extracted data
    page = 1  # Page number counter

    def start_request(self, url, filename):
        # Send a GET request to the specified URL
        request = requests.get(url)
        # Extract data from the response
        self.extract_data(request, filename)

    def extract_data(self, request, filename):
        # Create a BeautifulSoup object to parse the HTML content
        soup = BeautifulSoup(request.content, "html.parser")
        # Find all div elements with class "quote"
        quotes = soup.findAll("div", class_="quote")

        for item in quotes:
            # Extract the text of the quote
            quotes_text = item.find("span", class_="text").get_text()
            # Extract the author of the quote
            author = item.find("small", class_="author").get_text()
            # Extract the tags associated with the quote
            tags = item.findAll("a", class_="tag")
            tags = self.extract_tags(tags)
            # Create a dictionary with the extracted data
            quotes_data = {
                "Quotes": quotes_text,
                "Author": author,
                "Tags": tags,
                "Page": self.page,
            }
            print(quotes_data)
            # Append the data dictionary to the data list
            self.data.append(quotes_data)

        self.page += 1  # Increment the page counter
        print(len(self.data))
        try:
            # Find the link to the next page
            next_page = soup.select_one(".next a").get("href", "")
            if next_page:
                # Construct the URL for the next page
                url = f"https://quotes.toscrape.com/{next_page}"
                # Make a recursive call to start the request for the next page
                self.start_request(url, filename)

        except Exception:
            print("All Quotes Extracted Successfully!")
            # Write the extracted data to a file
            self.write_data_to_file(filename)

    def extract_tags(self, tag):
        # Extract the text of each tag and return as a list
        return [value.get_text() for value in tag]

    def write_data_to_file(self, filename):
        with open(filename, "w", encoding="utf-8") as file:
            for item in self.data:
                # Write the extracted data to the file
                file.write(f"Quotes: {item['Quotes']}\n")
                file.write(f"Author: {item['Author']}\n")
                file.write(f"Tags: {item['Tags']}\n")
                file.write(f"Page: {item['Page']}\n\n")


x = QuotesScrape()
# Start the scraping process by calling the start_request method
x.start_request("https://quotes.toscrape.com/", "quotes.txt")
