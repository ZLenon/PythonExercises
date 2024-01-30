# Crie um codigo em python que teste se o site PUDIM esta acessivel pelo computador usado.
# https://static.ragnaplace.com/db/npc/gif/${numero}.gif
import requests


def site_online(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.ConnectionError:
        return False


num = 100
url = f"https://api.ragnaplace.com/ro/list/mob?server=bro&type=server&categorie=all&order=id&sort=asc&page=1&limit=3&search="
if site_online(url):
    print("O site esta ONLINE")
else:
    print("O site esta OFFLINE")
