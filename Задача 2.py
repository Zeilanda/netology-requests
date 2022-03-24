import requests

from data_info import auth_token


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        headers = {'Content-Type': 'application/json', 'Authorization': f'OAuth {self.token}'}
        path = file_path.split('\\')[-1]
        print(f"save to {path!r}")
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload?path=' + path
        json_to_download = requests.get(url, headers=headers).json()
        print(f"link got: {json_to_download}")
        with open(file_path, 'rb') as file:
            try:
                resp = requests.put(json_to_download['href'], data=file)
                print(f"upload result: {resp}")
                return True
            except KeyError:
                print(json_to_download)
                return False


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = r'F:\GIT\Безмятежность.png'
    token = auth_token
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
