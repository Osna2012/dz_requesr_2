import requests
from pprint import pprint
import os

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        API_BASE_URL = "https://cloud-api.yandex.net/"

        headers = {
          'accept':"application/json",
          'authorization': f"OAuth {token}"
        }

        r = requests.get(API_BASE_URL + 'v1/disk/resources/upload', 
                          params={'path':'dz/' + file_name}, headers=headers)
        pprint(r.json())
        upload_url = r.json()['href']
        r = requests.put(upload_url ,headers=headers, files={'file':open(path_to_file, 'rb')})
        pprint(r.json)

if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = '2.jpg'
    file_name = path_to_file.split('/')
    file_name = (file_name[-1])
    token = 'AQAAAABYmXBzAADLW1DhOgOhFk81lPvQGycBOtk'
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)