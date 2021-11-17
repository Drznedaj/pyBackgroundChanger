from PIL import Image
import os

pic_number = 0
maximum_pic_num = 0
dir_path = os.path.dirname(os.path.abspath(__file__))
base_path = os.path.split(dir_path)[0]

for _, _, files in os.walk(dir_path):
    for f in files:
        if '.png' in f or '.jpg' in f:
            pic_number = int(f.split('.')[0])
            if pic_number > maximum_pic_num:
                maximum_pic_num = pic_number

maximum_pic_num += 1
print(f'Saving favourite picture number: {maximum_pic_num}')

pic_ = 'Pic_of_the_day.png'
pic_path = os.path.join(base_path, pic_)
exp_path = os.path.join(os.path.join(os.environ["USERPROFILE"], "Desktop"), 'Explanation.txt')

im = Image.open(pic_path)
im.save(f'{maximum_pic_num}.png', 'png')

with open(exp_path, 'r') as inf:
    with open(f'{maximum_pic_num}_explanation.txt', 'w') as outf:
        for line in inf:
            outf.write(line)
