import os
import urllib.request as ur
from urllib.error import HTTPError
from html.parser import HTMLParser
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

u = ur.urlopen('https://apod.nasa.gov/apod/astropix.html')  # opens the nasa pic of the day page
decoded_str = u.read().decode(encoding='utf-8').split('\n')

picture = 'https://apod.nasa.gov/apod/'  # prefix to the url of the picture

outs = ""

explntn_path = os.path.join(os.path.join(os.environ["USERPROFILE"], "Desktop"), 'Explanation.txt')


class MyHTMLParser(HTMLParser):
    def handle_data(self, data):
        global outs
        outs += data + '\n'


parser = MyHTMLParser()
for line in decoded_str:    # feed lines to a html parser to get the explanation
    parser.feed(line)       # of the picture
    if (picture != 'https://apod.nasa.gov/apod/'):
        continue
    elif '.png' in line or '.jpg' in line:
        x = line.split('\"')[1]  # this just gets the url without the html tags
        picture += x
        print(picture)
    elif 'youtube' in line:
        yt_link = 'Not Found'
        for l in line.split(' '):
            if 'youtube' in l:
                yt_link = l.split('\"')[1]
        print(f'Today there is a video on: {yt_link}')

# saves the explanation of the picture to a file on the desktop
with open(explntn_path, 'w') as outF:
    outF.write(outs[51:-326])

# this is a url of a picture of lower quality if we get an error
# downloading the first one we can try this one
pic1 = picture[:-4]+'1024.jpg'

try:
    # this part gets the actual picture and saves it to a file
    ur.urlretrieve(picture, 'Pic_of_the_day.png')

except HTTPError as e:
    print(f'There was an error: {e.reason} trying to download picture of a lower quality...')
    ur.urlretrieve(pic1, 'Pic_of_the_day.png')
