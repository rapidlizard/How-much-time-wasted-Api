import requests, json

class Steam():
    def get_user(steamid: str):
        url = "http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=2FA14ED02A1D7CCC0E4FCA80AE6AE194&steamids=" + steamid
        response = requests.get(url)

        data = response.json()

        return data['response']['players'][0]