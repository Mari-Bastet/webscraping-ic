import requests as rqs

api_key = "AIzaSyDWnxfSojfVCKXemocU1E_8B6WobDDvXQ0"

id_search_engine= "735137160db1f4152"

pesquisa = "noticias sobre o lula"

url = "https://customsearch.googleapis.com/customsearch/v1"

params = {
    'q': pesquisa,
    'key': api_key,
    'cx': id_search_engine,
    'cr': 'countryBR',
    'filter': 1,
    'lr': 'lang_pt'
}

response = rqs.get(url, params=params)

print(response.text)
