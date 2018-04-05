from PIL import Image
import ctypes,os

i = 0

with open('num.txt','r') as inf:
	for chr in inf:
		if chr >= '0' and chr <= '9':
			i=int(chr)
			print(i)

i+=1

with open('num.txt','w') as outf:
	outf.write(str(i))

pic_ = 'background changer\\Pic_of_the_day.png'
pic_path = os.path.join(os.path.join(os.environ["USERPROFILE"], "Desktop"), pic_)
exp_path = os.path.join(os.path.join(os.environ["USERPROFILE"], "Desktop"), 'Explanation.txt')

im = Image.open(pic_path)
im.save(str(i)+'.png','png')

with open(exp_path,'r') as inf:
	with open(str(i)+'_explanation.txt','w') as outf:
		for line in inf:
			outf.write(line)
