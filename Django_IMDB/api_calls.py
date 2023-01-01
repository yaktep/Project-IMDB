import requests

url = "http://127.0.0.1:8000/Movies/movies/"

payload = {'title': 'Example',
           'genre': 'example',
           'cast': 'example',
           'director': 'example',
           'writers': 'example',
           'actors': 'example',
           'year': '2000',
           'plot': 'lorem ipsum',
           'running_time': '7',
           'user': '2',
           'slug': 'example'}
files = [
    ('poster',
     ('Example.png', open('Example.png', 'rb'), 'image/png'))
]
headers = {
    'Authorization': 'Basic eWFraXI6a3V0aTI3'
}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)
