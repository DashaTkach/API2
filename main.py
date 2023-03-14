from pprint import pprint
import requests
import json

hero_list = ['Hulk', 'Captain America', 'Thanos']
intelligence = {'Hulk': 0, 'Captain America': 0, 'Thanos': 0}
url = 'https://akabab.github.io/superhero-api/api/all.json'
object_list = json.loads(requests.get(url).text)
for i in object_list:
    for hero in hero_list:
        if hero == i["name"]:
            intelligence[hero] = int(i["powerstats"]['intelligence'])
pprint(intelligence)


#  ==================================================================

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def link_for_upload(self, file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        return response.json()

    def upload(self, file_path, name_of_file):
        href = self.link_for_upload(file_path=file_path).get("href", "")
        requests.put(href, data=open(name_of_file, 'rb'))


if __name__ == 'main':
    file = r'for_file/2.txt'
    token =
    uploader = YaUploader(token)
    pprint(uploader.upload(file, '2.txt'))
