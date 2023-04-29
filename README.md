# Flask News Aggregator

A Flask web application that fetches news articles from an RSS feed, filters and sorts them, and saves them to a SQLite database.

## Features

- Fetch news articles from The New York Times World News RSS feed
- Filter articles based on a provided search keyword
- Sort articles according to the specified sorting order
- Save news articles, publisher, and news group information to a SQLite database
- Clear data from the SQLite database
- Determine the latest production version from a list of version strings

## Endpoints

1. `/rss`: Fetch, filter, and sort news articles from the RSS feed (GET)
2. `/save`: Save news articles, publisher, and news group information to the database (POST)
3. `/clear`: Clear all data from the SQLite database (POST)
4. `/versions`: Determine the latest production version from a list of version strings (POST)

## Usage

1. Clone the repository
2. Install the required dependencies
3. Run the Flask app (news_api.py)

## Example/Test Use Cases

### Using the provided scripts

1. **Saving filtered/unfiltered news**: Run `save_news.py` to fetch news articles, filter them by keyword (optional), sort them based on your choice (optional), and save them to the database.

2. **Printing the saved news**: Run `print_db.py` to display the saved news articles, publishers, and news groups from the database.

3. **Testing the production version**: Run `test_versions.py` to test the `/versions` endpoint with sample input and receive the latest production version from the provided list of versions.

### Using a browser or cURL

1. **Fetching news articles**: Open a browser and visit `http://localhost:5000/rss` to fetch the news articles. Optionally, you can add query parameters for filtering and sorting. For example, to fetch articles containing the keyword "Ukraine" and sort them by publication date in ascending order, visit `http://localhost:5000/rss?search=Ukraine&sort=pub_date_asc`.

2. **Saving news articles**: Use cURL to send a POST request to `http://localhost:5000/save` with JSON data containing the publisher, news group, and news articles to be saved. Replace `news_data.json` with the path to your JSON file:

curl -X POST -H "Content-Type: application/json" -d @news_data.json http://localhost:5000/save

3. **Clearing the database**: Use cURL to send a POST request to `http://localhost:5000/clear` to delete all the data from the SQLite database:

curl -X POST http://localhost:5000/clear

4. **Determining the latest production version**: Use cURL to send a POST request to `http://localhost:5000/versions` with JSON data containing a list of version strings. Replace `versions.json` with the path to your JSON file containing the list of versions:

curl -X POST -H "Content-Type: application/json" -d @versions.json http://localhost:5000/versions
