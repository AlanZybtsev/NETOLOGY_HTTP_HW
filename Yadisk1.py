from pprint import pprint

import requests


class YandexDisk:

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def get_files_list(self):
        files_url = 'https://cloud-api.yandex.net/v1/disk/resources/files'
        headers = self.get_headers()
        response = requests.get(files_url, headers=headers)
        return response.json()

    def _get_upload_link(self, disk_file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        data = response.json()
        url_to_load = data.get('href')
        return url_to_load

    def upload_file_to_disk(self, disk_file_path: str, filename: str):
        url_to_load = self._get_upload_link(disk_file_path = disk_file_path)
        # href = self._get_upload_link(disk_file_path=disk_file_path).get("href", "")
        response = requests.put(url_to_load, data=open(filename, 'rb'))
        # response.raise_for_status()
        if response.status_code == 201:
            print("Success")

if __name__ == '__main__':
    path_to_file = 'netology1.txt'
    TOKEN = 'y0_AgAAAABEcq1FAADLWwAAAADg_37hQKz7gvNVTq2Ex5Unn3F3pj39q0g'
    ya = YandexDisk(token=TOKEN)
    ya.upload_file_to_disk(path_to_file, 'text.txt')