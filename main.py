import requests
import json

headers = {
        "Accept-Encoding" : "gzip"

        }

host_api = 'https://apieasycall.ptl.ru'
url_api = '/api/ver1.0/'
url_zaprosa = host_api+url_api

print(url_zaprosa)
url = 'https://hostname/api/ver1.0/client/@me/extension/?extension_group_id=1&type=phone'
url2 = 'https://hostname/api/ver1.0/client/@me/extension/2'
#result = requests.get(url, headers = headers, params = params)
