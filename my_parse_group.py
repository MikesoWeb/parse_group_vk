import csv
import requests
import time


def take_1000_posts():
    owner_id = '-id group'
    version = 5.103
    token = 'ENTER OURS TOKEN'
    offset = 0
    count = 100
    all_posts = []
    while offset < 1000:
        response = requests.get('https://api.vk.com/method/wall.get',
                                params={
                                    'access_token': token,
                                    'v': version,
                                    'owner_id': owner_id,
                                    'count': count,
                                    'offset': offset
                                })

        data = response.json()['response']['items']
        offset += count
        all_posts.extend(data)
        time.sleep(0.2)
    return all_posts


def file_writer(data):
    with open('my_python_group_vk.csv', 'w') as file:
        a_pen = csv.writer(file)
        a_pen.writerow(('likes', 'body', 'url'))
        for post in data:
            img_url = ''
            try:
                if post['attachments'][0]['type']:
                    img_url = post['attachments'][0]['photo']['sizes'][-1]['url']

                else:
                    img_url = 'pass'

            except:
                pass

            a_pen.writerow((post['likes']['count'], post['text'], img_url))


all_posts = take_1000_posts()
file_writer(all_posts)

