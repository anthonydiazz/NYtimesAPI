import requests


month = "10"
year = "1918"
api_key = "fpMUu0iJUoQKLd2G45V2y5yoHdb3TfNd" 

url = f"https://api.nytimes.com/svc/archive/v1/{year}/{month}.json?api-key={api_key}"

response = requests.get(url)

data = response.json()

articles = data["response"]["docs"]

with open("titles_1918.txt","w") as file:
  for article in articles: 
    headline = article["headline"]["main"]
    file.write(headline.lower() + "\n")
#reading file 
#making a request 
# this code is getting the information from the url and then placing it into a text file


#hello tony 




