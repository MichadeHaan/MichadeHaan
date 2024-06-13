import requests
import json

url = 'https://graphql.anilist.co'

query = '''
query ($name: String) {
  User(name: $name) {
    name
    statistics {
      anime {
        count
        minutesWatched
      }
      manga {
        count
      }
    }
  }
}
'''

# Variabelen voor de query
variables = {
    'name': 'michasanime'
}

# Haal gegevens op van AniList
response = requests.post(url, json={'query': query, 'variables': variables})
data = json.loads(response.text)

# Verwerk de gegevens
user = data['data']['User']
anime_count = user['statistics']['anime']['count']
anime_minutes = user['statistics']['anime']['minutesWatched']
manga_count = user['statistics']['manga']['count']

# Bereken aantal dagen gekeken
anime_days = anime_minutes / 60 / 24

# Maak README-inhoud
readme_content = f'''
# {user["name"]}'s AniList Stats

- **Anime Watched**: {anime_count}
- **Days Watched**: {anime_days:.1f}
- **Manga Read**: {manga_count}
'''

# Schrijf naar README.md
with open('README.md', 'w') as file:
    file.write(readme_content)
