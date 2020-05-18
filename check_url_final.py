import requests
import pandas as pd

#сначала описываем функции для проверки ссылок со словами.
#instagram можно проверить с помощью status code
def get_instagram(word):
 instagram_url = "https://www.instagram.com/" + word
 result = requests.get(instagram_url)
 if result.status_code == 404:
  return instagram_url, '-'
 else:
  return instagram_url, '+'

# определяем тип для fb. т.к. на запрос статус кода fb выдает даже работающим страницам 404, воспользуемся параметром reason
def get_facebook(word):
  facebook_url="https://www.facebook.com/"+word
  result=requests.get(facebook_url)
  if result.reason=='Not Found':
    return facebook_url, '-'
  elif result.reason=='OK':
    return facebook_url, '+'
  else:
    return facebook_url, '?'

#открываем файл с словами
with open ('words.txt') as words_file:
    words_list = []
    for line in words_file:
        line = line.rstrip()
        words_list.append(line)
print(words_list)

#формируем финальную таблицу
result_table = pd.DataFrame(columns=['fb_url', 'fb_status', 'instagram_url', 'instagram_status'], index=words_list)

for word in words_list:
 result_table.loc[word] = [get_facebook(word)[0], get_facebook(word)[1], get_instagram(word)[0], get_instagram(word)[1]]

result_table.to_csv('result_table.csv')