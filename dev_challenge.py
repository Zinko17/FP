import requests
import sys
import datetime
from decouple import config

"""
https://api.github.com/repos/ryanheise/audio_service
Системные параметры (sys.argv) username repository start_date end_date
1. Вывести все коммиты в данном промежутке времени
2. Вывести все pull requests созданные в данном промежутке времени (key:created_at)
3. Вывести все issues созданные в данном промежутке времени (key:created_at)
"""

#Функция для отправления запросов
def send_request(url:str):
    """
    :param url: Ссылка на API Github пользователя ryanheise
    :return: Возвращает данные ссылки
    """
    r = requests.get(url,headers={'Authorization':f'Token {config("token")}'})
    return r.json()

#Функция преобразования строк/инт-чисел в формат даты
def to_datetime(date:str):
    """
    :param date:Дата
    :return:Переделанная дата
    """
    #Условие определяющее есть ли буква Т
    if 'T' not in date:
        result_date = datetime.datetime.strptime(date,'%Y-%m-%d')
        result_date = datetime.date(result_date.year,result_date.month,result_date.day)
    else:
        result_date = datetime.datetime.strptime(date, '%Y-%m-%dT%H:%M:%SZ')
        result_date = datetime.date(result_date.year, result_date.month, result_date.day)
    return result_date


#Функция получения всех коммитов, пользователей,которые делали коммиты, и количество коммитов каждого пользователя в указанный промежуток времени
def get_commits(url:str,start_date:str,end_date:str):
    """
    :param url: Ссылка на API Github пользователя ryanheise
    :param start_date: Дата, которая послужит началом указанного промежутка времени
    :param end_date: Дата, которая послужит концом указанного промежутка времени
    :return: Список коммитов и словарь с ключем, как имя пользователя и значением, как количество коммитов
    """
    commits = []
    author_list = []
    url = url + '/commits'
    start_date = to_datetime(start_date)
    end_date = to_datetime(end_date)
    responses = send_request(url)
    #Цикл для входа в список responses
    for response in responses:
        commit_date = to_datetime(response['commit']['author']['date'])
        commit = response['commit']['message']
        author = response['author']['login']
        #Условие, с помощью которого коммиты добавляются в список commits
        if start_date<=commit_date<=end_date:
            commits.append(commit)
            #Условие, с помощью которого в список author_list добавляются пользователи,которые коммитили в репозиторий
            if author not in author_list:
                author_list.append(author)
    author_dict = {}
    #Цикл, который позволяет зайти в список author_list
    for author in author_list:
        commits_count = 0
        #Цикл, позволяющий зайти в список responses
        for response in responses:
            r_author = response['author']['login']
            #Условие, с помощью которого работает счетчик коммито для пользователей,которые в саиске author_list
            if author == r_author:
                commits_count += 1
        author_dict[author] = commits_count

    return commits,author_dict


#Функция, которая достает названия пулл реквестов
def get_pulls(url:str,start_date:str,end_date:str):
    """

    :param url: Ссылка на API Github пользователя ryanheise
    :param start_date: Дата, которая послужит началом указанного промежутка времени
    :param end_date: Дата, которая послужит концом указанного промежутка времени
    :return: Возвращает список с названиями пулл реквестов
    """
    pulls = []
    url = url + '/pulls'
    start_date = to_datetime(start_date)
    end_date = to_datetime(end_date)
    responses = send_request(url)
    #Цикл, с помощью которого обращаемся k списку responses
    for response in responses:
        pulls_date = to_datetime(response['created_at'])
        pulls_title = response['title']
        #Условие, которое добавляет название пулл реквестов в список pulls
        if start_date<=pulls_date<=end_date:
            pulls.append(pulls_title)
    return pulls


#Функция, для возвращения названий issues созданных в указанный промежуток времени
def get_issues(url:str,start_date:str,end_date:str):
    """

    :param url: Ссылка на API Github пользователя ryanheise
    :param start_date: Дата, которая послужит началом указанного промежутка времени
    :param end_date: Дата, которая послужит концом указанного промежутка времени
    :return: Возвращает список issues, в котором названия этих issues
    """
    issues = []
    url = url + '/issues'
    start_date = to_datetime(start_date)
    end_date = to_datetime(end_date)
    responses = send_request(url)
    # Цикл, с помощью которого обращаемся k списку responses
    for response in responses:
        issues_date = to_datetime(response['created_at'])
        issues_title = response['title']
        # Условие, которое добавляет название issues в список issues
        if start_date<=issues_date<=end_date:
            issues.append(issues_title)
    return issues

#Функция, которая вызывает другие функции
def main():
    """
    :return: А его нету
    """
    github_username = sys.argv[1]
    github_repository = sys.argv[2]
    url = 'https://api.github.com/repos/{}/{}'.format(github_username,github_repository)
    start_date = sys.argv[3]
    end_date = sys.argv[4]
    print(get_commits(url, start_date,end_date))
    print(get_pulls(url, start_date, end_date))
    print(get_issues(url, start_date, end_date))
main()

