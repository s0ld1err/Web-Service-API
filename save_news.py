import requests

# Take user input for sorting
print("Select sort order (optional):")
print("1. Publication date (ascending)")
print("2. Publication date (descending)")
print("3. Title (ascending)")
print("4. Title (descending)")
print("Press Enter to save all news without sorting.")
sort_choice = input("Enter the number corresponding to your choice (1-4) or press Enter: ")

sort_options = {
    "1": "pub_date_asc",
    "2": "pub_date_desc",
    "3": "title_asc",
    "4": "title_desc"
}
sort_order = sort_options.get(sort_choice)

# Take user input for keyword (optional)
use_keyword = input("Do you want to filter news by keyword? (y/n): ").lower()
keyword = ""
if use_keyword == 'y':
    keyword = input("Enter the keyword: ").lower()

# Fetch news
rss_url = "http://localhost:5000/rss"

params = {}
if sort_order:
    params["sort"] = sort_order
if keyword:
    params["search"] = keyword

response = requests.get(rss_url, params=params)
news = response.json()

# Clear existing data in the database
clear_url = "http://localhost:5000/clear"
response = requests.post(clear_url)
print(response.json())  # Prints the response message from the server

# Save filtered* news
save_url = "http://localhost:5000/save"
data = {
    "publisher": "The New York Times",
    "news_group": "World",
    "news": news
}
response = requests.post(save_url, json=data)
print(response.json())  # Prints the response message from the server
