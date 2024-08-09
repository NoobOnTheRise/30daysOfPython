# Use the NewsAPI and the requests module to fetch the daily news related to different topics.
# Go to: https://newsapi.org/ and explore the various options to build you application

import requests
import json

list = ["apple","microsoft","google","facebook","twitter","amazon","netflix","space","general"]

query = int(input("What type of news are you interested in? Please enter the number. 1. Apple 2. Microsoft 3. Google 4. Facebook 5. Twitter 6. Amazon 7. Netflix 8. Space 9. General : " ))

param = list[query - 1]
response = requests.get(f'https://newsapi.org/v2/everything?q={param}&from=2024-06-03&sortBy=publishedAt&apiKey=9f13448e140f49cdbd91f3adf45c42e3')

news = json.loads(response.text)

for article in news["articles"]:
     print("------------------------------------------------------")
     print(article["title"], "by", article["author"])
     print("------------------------------------------------------")
     print(article["description"])