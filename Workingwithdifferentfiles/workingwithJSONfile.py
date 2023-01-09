import json
from pathlib import Path
#Jason stands for JavaScript Object Notation and is a popular way to format data in a hu,an redable way,These days
#Its very important to know json because lot of popular websites like Facebook, Yelp, YouTube, etc provide their data
#in json format
movies = [
    {"id" : 1, "title": "Terminator","Year" : 1989 },
    {"id" : 2, "title": "Kindergarten Cop", "year": 1993 }
]
data = json.dumps(movies)
Path("movies.json").write_text(data)
print(data)
data = Path("movies.json").read_text()
movies = json.loads(data)
print(movies[0]["title"])
