from .models import Numbers, User
import re
import bs4


def how_long_month(numbers=[], details=False, id_process=1, work_time=(8, 18)):
    data_storage = {}
    # query = Numbers.objects.all().filter(id_process=id_process, number=number)

    for number in numbers:
        key = int(number.number)
        time_result = 0
        internet_result = 0
        data_storage[key] = {}

        for j in number.data:
            long = j[3].split(':')
            time = j[1].split(':')

            if work_time[0] < int(time[0]) < work_time[1]:
                var_number = 0

                if j[2][3:].isdigit():
                    # формирование отчета по звонкам, на каждый номер
                    if j[2][0:3] == '<--':
                        var_number = j[2][3:]
                    else:
                        var_number = j[2]
                    data_storage[key].setdefault(var_number, 0)
                    try:
                        data_storage[key][var_number] += (int(long[0]) * 60) + int(long[1])
                    except IndexError:
                        data_storage[key][var_number] += (int(long[0]) * 60)

                try:
                    time_result += (int(long[0]) * 60) + int(long[1])
                except IndexError:
                    pass
                except ValueError:
                    internet_result += int(j[3].split('Kb')[0])

        data_storage[key]['result'] = f'{number.number} - Проговорил {round(time_result / 3600, 2)} часа, Интернета потратил {round(internet_result / 1024, 2)} Mb \n'

    return data_storage


def parse_phones(files=[], id_process=1):
    # разбор .html файла и запись в data класса User
    numbers = []
    try:
        for file in files:
            file = file.read().decode()
            num = re.findall(r'7\d{10}', file)
            soup = bs4.BeautifulSoup(file, 'lxml')
            rows = soup.tbody
            num = User(num[0], id_process)

            for row in rows:
                res = row.contents
                num.data.append([res[1].next, res[2].next, res[4].next, res[9].next])

            numbers.append(num)
    except TypeError:
        return False
    except IndexError:
        return False
    except UnicodeDecodeError:
        return False

    return numbers


def sort_dictionary_by_value(dictionary):
    # сортировка словаря по убыванию значений
    dictionary.pop('result')
    list_of_sorted_pairs = [(k, dictionary[k]) for k in sorted(dictionary.keys(), key=dictionary.get, reverse=True)]

    return list_of_sorted_pairs


def parse_dict(dict, num):
    # разбор информации для страницы details.html
    dict = sort_dictionary_by_value(dict[num])
    result = []
    for key in dict:
        result.append(f'{key[0]} - {round(key[1]/3600, 2)} часа')

    return result







