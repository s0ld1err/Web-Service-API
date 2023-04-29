import sqlite3

conn = sqlite3.connect('news.db')
c = conn.cursor()

c.execute("SELECT * FROM publishers")
publishers = c.fetchall()
print("Publishers:")
for publisher in publishers:
    print(publisher)

c.execute("SELECT * FROM news_groups")
news_groups = c.fetchall()
print("\nNews Groups:")
for news_group in news_groups:
    print(news_group)

c.execute("SELECT * FROM news")
news_items = c.fetchall()
print("\nNews:")
for news_item in news_items:
    print(news_item)

conn.close()

input("Press Enter to exit...")