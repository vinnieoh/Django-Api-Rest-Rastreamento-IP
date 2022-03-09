import requests

IP_SEARCH_ENDPOINT = 'http://ip-api.com/json/'

def ip_search(ip_location):

    ip = ip_location.get('ip')
    r = requests.get(IP_SEARCH_ENDPOINT + ip).json()

    return r

