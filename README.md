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

## Dependencies

- Flask
- feedparser
- SQLAlchemy
- re

## Usage

1. Clone the repository
2. Install the required dependencies
3. Run the Flask app
