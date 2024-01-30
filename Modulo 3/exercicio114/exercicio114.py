# Crie um codigo em python que teste se o site PUDIM esta acessivel pelo computador usado.
# https://static.ragnaplace.com/db/npc/gif/${numero}.gif
import requests


def get_data_info():
    try:
        url = f"https://api.ragnaplace.com/ro/list/mob?server=bro&type=server&categorie=all&order=id&sort=desc&page=1&limit=5&search="
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
        for valor in enumerate(dict(data).values()):
            if isinstance(valor[1], list):
                for info in valor[1]:
                    show_moster(info)
            else:
                break
    except requests.ConnectionError:
        return []


def show_moster(info):
    print("Monster".center(25))
    print("ID:", f'\t{info["id"]}')
    print("Nome:", f'\t{info["name"]}')
    print("Level:", f'\t{info["lv"]}')
    print("Vida:", f'\t{info["hp"]}')
    print("Raça:", f'\t{info["race"]}')
    print("-=" * 10)


get_data_info()
