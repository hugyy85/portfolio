import requests, bs4


class FindText:
    def __init__(self, url):
        self.url = url
        self.tags = ['h1', 'h2', 'h3', 'h4', 'h5', 'p', 'code']
        self.errors = [
            'Вы ввели не существующий URL-адресс',
            f'Не удалось подключиться к {self.url}, попробуйте другой адресс'
                       ]

    def find_text(self):
        result_text = []

        try:
            response = requests.get(self.url)
        except requests.exceptions.MissingSchema:
            return [self.errors[0]]
        except requests.exceptions.ConnectionError:
            return [self.errors[1]]
        except requests.exceptions.InvalidSchema:
            return [self.errors[0]]

        soup = bs4.BeautifulSoup(response.content, 'lxml')
        text = soup.findAll(self.tags)

        for line in text:
            result_text.append(line.text)

        return result_text

check = FindText(' htts://lent.e').find_text()