## 1
def sumThreeFive(x):
    sum = 0
    for i in range(0, x):
        if i % 3 == 0 or i % 5 == 0:
           sum = sum + i
    return sum

sumThreeFive(10000) # = 23331668

#%%
## 2

dfib = {}
def  fibo(n):
    if n == 1:
        dfib[n] = 1
        return dfib[n]
    elif n == 2:
        dfib[n] = 2
        return dfib[n]
    else:
        first = 0
        second = 0
        if n - 2 in dfib.keys():
            first = first + dfib[n - 2]
        else:
            first = first + fibo(n - 2)
            dfib[n - 2] = first
        if n - 1 in dfib.keys():
            second = second + dfib[n - 1]
        else:
            second = second + fibo(n - 1)
            dfib[n - 1] = second
        return first + second
fibo(200) # = 453973694165307953197296969697410619233826
#%%
##3
import pandas
def anagrams(name):
    def concat(smth):
        ind = ''
        for i in sorted(smth):
            ind = ind + i
        return(ind)
    
    df = (pandas.read_table(name, header = None))[0].tolist()
    anag_dict = []
    anag_dict.append([concat(df[0]), df[0]])
    for word in df[1:]:
        word1 = concat(word)
        if word1 in [record[0] for record in anag_dict]:
            index = [record[0] for record in anag_dict].index(word1)
            anag_dict[index].append(word)
        else:
            anag_dict.append([word1, word])
    for record in anag_dict:
        if len(record) > 4:
            print(record[1:])
#%%
## 4
import pandas
def typesetter(name, headword):
    df = (pandas.read_table(name, header = None))[0].tolist()
    subwords = []
    for word in df:
        leck = sorted(headword)
        subword = sorted(word)
        flag = True
        while len(subword) > 0 and flag:
            if subword[0] in leck:
                del leck[leck.index(subword[0])]
                del subword[0]
            else:
                flag = False
        if flag:
            subwords.append(word)
    print(subwords)
    print('Всего', len(subwords), 'cлов')
#всего 147 слов

#%%
## 5
import pandas
import random
def game_tamada(name):
    #name = 'words-list-russian.txt'
    df = (pandas.read_table(name, header = None))[0].tolist()
    print('Игра началась')
    valid_words = []
    guesses = 0
    for word in df:
        if len(word) == 5 and len(set(sorted(word))) == 5:
            valid_words.append(word)
            #print(word)
    word = random.choice(valid_words)
    print('hint:', word)
    
    playing = True
    
    while playing:
        guesses = guesses + 1
        user_guess = input('Ваше слово:\n')
        if user_guess == 'exit':
            print('Вы вышли из игры')
            break
        elif user_guess == word:
            playing = False
            print('!')
            print('Угадали с попытки номер %s' % (guesses))
        elif len(user_guess) != 5:
            print('Необходимо слово в 5 букв')
        elif user_guess not in df:
            print ('Неизвестное слово')
        else:
            print(len(set(sorted(word)) & set(sorted(user_guess))))
#%%
## 6
import pandas
import random
def game_ne_tamada(name):
    #name = 'words-list-russian.txt'
    myword = input('Мое слово:\n')
    print('Начинаю угадывать!')
    df = (pandas.read_table(name, header = None))[0].tolist()
    valid_words = []
    guesses = 0
    number = 0
    for word in df:
        if len(word) == 5 and len(set(sorted(word))) == 5:
            valid_words.append(word)
    playing = True
    while playing:
        guesses = guesses + 1
        word = random.choice(valid_words)
        del valid_words[valid_words.index(word)]
        print(word)
        if myword == word:
            print('(hint: !)')
        else:
            print('(hint: ', len(set(sorted(myword)) & set(sorted(word))), ')')
        newnumber = input('Количество совпадений: ')
        if newnumber == 'exit':
            print('Вы вышли из игры')
            playing = False
        elif newnumber == '!':
            print('Я угадала с попытки номер %s ' % (guesses))
            playing = False
        elif len(set(valid_words)) == 0:
            print('Я не знаю такого слова')
            playing = False
        else:
            temp = []
            for words in valid_words:
                if len(set(sorted(words)) & set(sorted(word))) == int(newnumber):
                    temp.append(words)
                    valid_words = temp
            number = newnumber

#%%
##7
import pandas as pd
import re
import urllib.request
from bs4 import BeautifulSoup
def parser():
    url = 'http://www.belstat.gov.by/ofitsialnaya-statistika/makroekonomika-i-okruzhayushchaya-sreda/natsionalnye-scheta/godovye-dannye_11/proizvodstvo-valovogo-vnutrennego-produkta/'
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    data = []
    rownum = 0
    for rows in soup.find_all('table', border='1', cellpadding='0', cellspacing='0')[0].find_all('tr'):
        data.append([])
        for cells in rows.find_all('p'):
            cell = cells.text.replace('\n', '').replace('\t', '').replace('\xa0', '')
            if any(c.isalpha() for c in cell):
                data[rownum].append(cell)
            else:
                data[rownum].append(cell.replace(' ','').replace(',','.'))
        rownum = rownum + 1

    #Вывод
    for row in data:
        first = True
        for cell in row:
            if first:
                print('%76s' % cell, end = '')
            else:
                print('%7s' % cell, end = '')
            first = False
        print('\n')