from bs4 import BeautifulSoup


class RenameTags:
    def __init__(self, file):
        self.file = file
        # self.html = ''
        with open(self.file, 'r') as file:
            self.html = file.read()
        self.soup = BeautifulSoup(self.html, 'lxml')
        self.static = '{% static "'
        self.static_end = '" %}'

    def img_tag(self):
        for tag in self.soup.find_all('img'):
            if (r'http://' and r'https://') not in tag['src']:
                tag['src'] = f'{self.static + tag["src"] + self.static_end}'

    def script_tag(self):
        for tag in self.soup.find_all('script'):
            if (r'http://' and r'https://') not in tag['src']:
                tag['src'] = f'{self.static + tag["src"] + self.static_end}'

    def link_tag(self):
        for tag in self.soup.find_all('link'):
            if (r'http://' and r'https://') not in tag['href']:
                tag['href'] = f'{self.static + tag["href"] + self.static_end}'

    def rewrite_file(self):
        with open('ex.html', 'w') as file:
            file.write('{% load static %}\n' + str(self.soup.prettify()))


file = RenameTags('index1.html')
file.img_tag()
file.script_tag()
file.link_tag()
file.rewrite_file()