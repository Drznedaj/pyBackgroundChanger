from PIL import Image
import os

i = 0
dir_path = os.path.dirname(os.path.abspath(__file__))
base_path = os.path.split(dir_path)[0]

for top, _, files in os.walk(dir_path):
    for f in files:
        if '.png' in f or '.jpg' in f:
            i = int(f.split('.')[0])

print('Saving favourite picture number: {}'.format(i))

pic_ = 'Pic_of_the_day.png'
pic_path = os.path.join(base_path, pic_)
exp_path = os.path.join(os.path.join(os.environ["USERPROFILE"], "Desktop"), 'Explanation.txt')

im = Image.open(pic_path)
im.save(str(i)+'.png', 'png')

with open(exp_path, 'r') as inf:
    with open(str(i)+'_explanation.txt', 'w') as outf:
        for line in inf:
            outf.write(line)
