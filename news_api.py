from flask import Flask, request, jsonify
import feedparser
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
import re

app = Flask(__name__)

# Database setup
Base = declarative_base()
engine = create_engine('sqlite:///news.db')
Session = sessionmaker(bind=engine)

class Publisher(Base):
    __tablename__ = 'publishers'
    id = Column(Integer, primary_key=True)
    name = Column(String)

class NewsGroup(Base):
    __tablename__ = 'news_groups'
    id = Column(Integer, primary_key=True)
    name = Column(String)

class News(Base):
    __tablename__ = 'news'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    link = Column(String)
    description = Column(String)
    publication_date = Column(DateTime)
    publisher_id = Column(Integer, ForeignKey('publishers.id'))
    news_group_id = Column(Integer, ForeignKey('news_groups.id'))

    publisher = relationship("Publisher")
    news_group = relationship("NewsGroup")

Base.metadata.create_all(engine)

@app.route('/rss', methods=['GET'])
def parse_rss():
    sort = request.args.get('sort')
    search = request.args.get('search')

    rss_url = "https://rss.nytimes.com/services/xml/rss/nyt/World.xml"
    feed = feedparser.parse(rss_url)

    entries = feed.entries

    # Filter by search
    if search:
        search = search.lower()
        entries = [entry for entry in entries if search in entry.title.lower() or search in entry.description.lower()]

    # Sort
    if sort == "title_asc":
        entries.sort(key=lambda x: x.title)
    elif sort == "title_desc":
        entries.sort(key=lambda x: x.title, reverse=True)
    elif sort == "pub_date_asc":
        entries.sort(key=lambda x: x.published_parsed)
    elif sort == "pub_date_desc":
        entries.sort(key=lambda x: x.published_parsed, reverse=True)

    response = []
    for entry in entries:
        response.append({
            "title": entry.title,
            "link": entry.link,
            "description": entry.description,
            "pub_date": entry.published
        })

    return jsonify(response)

@app.route('/save', methods=['POST'])
def save_news():
    data = request.json
    session = Session()

    publisher = Publisher(name=data['publisher'])
    news_group = NewsGroup(name=data['news_group'])
    session.add(publisher)
    session.add(news_group)

    for news_item in data['news']:
        news = News(
            title=news_item['title'],
            link=news_item['link'],
            description=news_item['description'],
            publication_date=datetime.strptime(news_item['pub_date'], "%a, %d %b %Y %H:%M:%S %z"),
            publisher=publisher,
            news_group=news_group
        )
        session.add(news)

    session.commit()
    session.close()

    return {"message": "News saved successfully"}

@app.route('/clear', methods=['POST'])
def clear_data():
    session = Session()
    session.query(News).delete()
    session.query(NewsGroup).delete()
    session.query(Publisher).delete()
    session.commit()
    session.close()
    return {"message": "Database cleared successfully"}

def is_production_version(version: str) -> bool:
    return not any([c.isalpha() for c in version.split('.')[-1]])

@app.route('/versions', methods=['POST'])
def production_version():
    versions = request.json['versions']
    production_versions = [v for v in versions if not re.search(r'-\D', v)]
    production_versions.sort(reverse=True)
    return {"production_version": production_versions[0] if production_versions else None}


if __name__ == '__main__':
    app.run(debug=True)