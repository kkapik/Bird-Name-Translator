#!/usr/bin/env python3

def get_all_taxonomy(locale):
    import requests

    url = "https://api.ebird.org/v2/ref/taxonomy/ebird?fmt=json&locale="+locale

    payload={}
    headers = {
      'X-eBirdApiToken': 'webAPIToken'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    return response.text
if __name__ == '__main__':
    print('Language?')
    locale = input()
    name = 'taxonomy_'+locale+'.json'
    with open(name, 'w') as f:
        f.write(get_all_taxonomy(locale))
