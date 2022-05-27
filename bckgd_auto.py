import os
import itertools
import threading
import time
import sys
import codecs
import urllib.request as ur
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import ssl


def save_explanation(soup: BeautifulSoup, explntn_path: str):
    explanation = soup.find_all('p')[2].get_text()

    # saves the explanation of the picture to a file on the desktop
    with open(explntn_path, 'w') as outF:
        outF.write(explanation)


def save_pictrure(soup: BeautifulSoup, picture_prefix: str):

    for link in soup.find_all('a'):
        lnk = link.get('href')
        if 'image' in lnk:
            picture_suffix = lnk
            break

    picture_suffix = picture_suffix if picture_suffix else ''

    picture_url = f'{picture_prefix}{picture_suffix}'
    print(f'\r{picture_url}')

    # this is a url of a picture of lower quality if we get an error
    # downloading the first one we can try this one
    pic1 = picture_url[:-4]+'1024.jpg'

    try:
        # this part gets the actual picture and saves it to a file
        ur.urlretrieve(picture_url, 'Pic_of_the_day.png')

    except HTTPError as e:
        print(f'There was an error: {e.reason} trying to download picture of a lower quality...')
        ur.urlretrieve(pic1, 'Pic_of_the_day.png')


done = False


def animate():
    if sys.stdout.encoding != 'UTF-8':
        sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
    for c in itertools.cycle(["⢿", "⣻", "⣽", "⣾", "⣷", "⣯", "⣟", "⡿"]):
        if done:
            break
        sys.stdout.write(f'\rloading {c}')
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\rDownload complete!')


if __name__ == '__main__':

    t = threading.Thread(target=animate)
    t.start()

    picture_prefix = 'https://apod.nasa.gov/apod/'  # prefix to the url of the picture
    explntn_path = os.path.join(os.path.join(os.environ["USERPROFILE"], "Desktop"), 'Explanation.txt')

    ssl._create_default_https_context = ssl._create_unverified_context

    u = ur.urlopen(f'{picture_prefix}/astropix.html')  # opens the nasa pic of the day page
    soup = BeautifulSoup(u.read().decode(encoding='utf-8'), 'html.parser')

    save_explanation(soup, explntn_path)

    save_pictrure(soup, picture_prefix)

    done = True
