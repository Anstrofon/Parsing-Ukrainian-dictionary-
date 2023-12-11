''' Парсимо окрему колонку, щоб потім записати словник зі словами стовпчик, без тлумачень, для
того, щоб потім знаходити аннаграми і т.д.'''
import requests, bs4, os
import time

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0"
}
page = 0
url ='https://sum20ua.com/Entry/index?wordid=5&page='


while not url.endswith('2381'):
    soup = bs4.BeautifulSoup(requests.get(url, headers=headers).text, 'html.parser')
    entry_block = soup.find('main').find('nav').find('div', class_="entry").find_all('li') # знаходимо колонку зі словами
    for i in range (0, 50):
        ''' проходимо по всій колонці, які має всі слова та записуємо у файл'''
        word = entry_block[i].getText().split(' ')
        word = word[16] # з 16 відступу рядка там починається слово.

        with open('ukrainian_dict(without dublicats).txt', "a", encoding="utf-8") as f:
            f.write(word + '\n')

    time.sleep(2)

    page += 1
    
    positionStr = '{0} сторінка'.format(page)
    print(positionStr, end='')
    print('\b' * len(positionStr), end='', flush=True)
    url = 'https://sum20ua.com/Entry/index?wordid=5&page={0}'.format(page)
