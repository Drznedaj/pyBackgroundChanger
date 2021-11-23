import os
import urllib.request as ur
from urllib.error import HTTPError
from html.parser import HTMLParser
from bs4 import BeautifulSoup
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

u = ur.urlopen('https://apod.nasa.gov/apod/astropix.html')  # opens the nasa pic of the day page
soup = BeautifulSoup(u.read().decode(encoding='utf-8'), 'html.parser')

explanation = soup.find_all('p')[2].get_text()

picture_suffix = ''

for link in soup.find_all('a'):
    lnk = link.get('href')
    if 'image' in lnk:
        picture_suffix = lnk
        break

picture_prefix = 'https://apod.nasa.gov/apod/'  # prefix to the url of the picture
picture_url = f'{picture_prefix}{picture_suffix}'
print(picture_url)

explntn_path = os.path.join(os.path.join(os.environ["USERPROFILE"], "Desktop"), 'Explanation.txt')

# saves the explanation of the picture to a file on the desktop
with open(explntn_path, 'w') as outF:
    outF.write(explanation)

# this is a url of a picture of lower quality if we get an error
# downloading the first one we can try this one
pic1 = picture_url[:-4]+'1024.jpg'

try:
    # this part gets the actual picture and saves it to a file
    ur.urlretrieve(picture_url, 'Pic_of_the_day.png')

except HTTPError as e:
    print(f'There was an error: {e.reason} trying to download picture of a lower quality...')
    ur.urlretrieve(pic1, 'Pic_of_the_day.png')
