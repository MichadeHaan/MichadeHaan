import requests # type: ignore
import json

url = 'https://anilist.co'

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

variables = {
    'name': 'michasanime'
}

response = requests.post(url, json={'query': query, 'variables': variables})
data = json.loads(response.text)

user = data['data']['User']
anime_count = user['statistics']['anime']['count']
anime_minutes = user['statistics']['anime']['minutesWatched']
manga_count = user['statistics']['manga']['count']

anime_days = anime_minutes / 60 / 24

readme_content = f'''
# {user["name"]}'s AniList Stats

![Profile Image](https://anilist.co/img/dir/user/logo/{user["name"]}.png)

- **Anime Watched**: {anime_count}
- **Days Watched**: {anime_days:.1f}
- **Manga Read**: {manga_count}
'''

with open('README.md', 'w') as file:
    file.write(readme_content)
