import requests
import json

# AniList API-endpoint en headers
url = 'https://graphql.anilist.co'
headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
}

# Vervang deze gegevens door je eigen Client ID en Secret
client_id = '19263'
client_secret = '3HXL5sRN66lGpaT721439uT01qOUOmNqtDnxVckh'
api_key = 'jouw_api_sleutel_hier'  # Vervang door je eigen API sleutel

# GraphQL-query om gebruikersinformatie op te halen
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

def get_anilist_data(username):
    variables = {
        'name': username
    }
    response = requests.post(url, json={'query': query, 'variables': variables})
    data = json.loads(response.text)
  
    if response.status_code == 200:
        data = response.json()
        user = data['data']['User']
        anime_count = user['statistics']['anime']['count']
        anime_minutes = user['statistics']['anime']['minutesWatched']
        manga_count = user['statistics']['manga']['count']

        # Bereken aantal dagen gekeken
        anime_days = anime_minutes / 60 / 24

        return {
            'name': user['name'],
            'anime_count': anime_count,
            'anime_days': anime_days,
            'manga_count': manga_count,
        }
    else:
        print(f'Er is een fout opgetreden bij het ophalen van de gegevens voor {username}')
        return None

# Vervang 'michasanime' door je eigen gebruikersnaam op AniList
username = 'michasanime'
user_data = get_anilist_data(username)

if user_data:
    # Maak README-inhoud
    readme_content = f'''
# {user_data["name"]}'s AniList Stats

- **Anime Watched**: {user_data["anime_count"]}
- **Days Watched**: {user_data["anime_days"]:.1f}
- **Manga Read**: {user_data["manga_count"]}
    '''

    # Schrijf naar README.md
    with open('README.md', 'w') as file:
        file.write(readme_content)
else:
    print('Er zijn geen gegevens opgehaald om naar README.md te schrijven.')
