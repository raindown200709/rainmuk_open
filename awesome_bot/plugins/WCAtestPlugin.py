import requests
import json

url = ''
response = requests.get(url)
strhtml = response.text
