import requests
from bs4 import BeautifulSoup

# Make a request to the website
url = "https://www.formula1.com/en/drivers.html"
response = requests.get(url)

# Create a BeautifulSoup object from the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Find and extract specific data from the HTML
title = soup.title.text
paragraphs = soup.find_all("div")

# Print the extracted data
print("Title:", title)
print("Paragraphs:")
for paragraph in paragraphs:
    print(paragraph.text)
