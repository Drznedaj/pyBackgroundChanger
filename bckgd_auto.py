import ctypes
import os
import urllib.request
from html.parser import HTMLParser

u = urllib.request.urlopen('https://apod.nasa.gov/apod/astropix.html')  # opens the nasa pic of the day page

f = open("Url_to_parse.txt", "w")  # saving the html to text and decoding
f.write(u.read().decode("utf-8", errors='ignore'))
f.close()

picture = 'https://apod.nasa.gov/apod/'  # prefix to the url of the picture

outs = ""

explntn = 'Explanation.txt'
pic_ = 'background changer\\Pic_of_the_day.png'
explntn_path = os.path.join(os.path.join(os.environ["USERPROFILE"], "Desktop"), explntn)
pic_path = os.path.join(os.path.join(os.environ["USERPROFILE"], "Desktop"), pic_)


class MyHTMLParser(HTMLParser):
    def handle_data(self, data):
        global outs
        outs += data


parser = MyHTMLParser()

with open('Url_to_parse.txt', 'r') as inF:  # finding the rest of the url of the picture in the file
    for line in inF:  # and feeds lines to a html parser to get the explanation
        parser.feed(line)  # of the picture
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
            print('Today there is a video on: {}'.format(yt_link))

print(outs)

# saves the explanation of the picture to a file on the desktop
with open(explntn_path, 'w') as outF:
    outF.write(outs[51:-326])

# this part gets the actual picture and saves it to a file
pic1 = picture[:-4]+'1024.jpg'

try:
    urllib.request.urlretrieve(picture, 'Pic_of_the_day.png')

except urllib.error.HTTPError as e:
    print('Doslo je do greske: '+e.reason+' Skidam sliku manjeg kvaliteta...')
    urllib.request.urlretrieve(pic1, 'Pic_of_the_day.png')
