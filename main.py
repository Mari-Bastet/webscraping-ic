import requests as rqs
import pandas as pd
import time

v_max_por_paginas = 10
def requisicao_api(v_indice):
    api_key = "AIzaSyDWnxfSojfVCKXemocU1E_8B6WobDDvXQ0"

    id_search_engine = "735137160db1f4152"

    pesquisa = "noticias sobre o lula 2024"

    url = "https://customsearch.googleapis.com/customsearch/v1"

    params = {
        'q': pesquisa,
        'key': api_key,
        'cx': id_search_engine,
        'cr': 'countryBR',
        'filter': 1,
        'lr': 'lang_pt',
        'num': v_max_por_paginas,
        'start': v_indice
    }

    return rqs.get(url, params=params).json()

def recupera_dados():
    dados = []
    v_qtd_dados = 100
    v_inicio = 1

    while len(dados) < v_qtd_dados:
        try:
            data = requisicao_api(v_inicio)

            if 'items' in data:
                for item in data['items']:
                    title = item.get('title', 'Título não disponível')
                    link = item.get('link', 'Link não disponível')
                    snippet = item.get('snippet', 'Descrição não disponível')
                    dados.append({
                        'titulo': title,
                        'link': link,
                        'descricao': snippet
                    })

                v_inicio += v_max_por_paginas

            else:
                print("Sem mais resultados disponíveis.")
                break

            time.sleep(1)

        except Exception as e:
            print(f"Erro ao buscar os resultados: {e}")
            break

    return dados

    # print(response.text)
    # print(response.json()["items"][6]["title"])

dados_scraped = recupera_dados()

df = pd.DataFrame(dados_scraped)

nome_arquivo_excel = r'C:\Users\maria\Projetos\resultados_busca_google.xlsx'
df.to_excel(nome_arquivo_excel, index=False)