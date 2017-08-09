import pyscreenshot as ImageGrab
import string
import ipdb
import matplotlib.pyplot as plt
import time
from scipy.misc import imsave
import os
from scipy.misc import imread

X_LOC = [3, 48]
Y_LOC = [1425, 1470]

# make sure the terminal where this is printing is open when you call this
def screenshot_screen(letter):
	print letter
	time.sleep(0.5)
	im = ImageGrab.grab()

	return im

def save_letters():
	letters_list = list(string.ascii_lowercase)
	for l in letters_list:
		im = screenshot_screen(l)
		imsave(os.path.join('data', l + '.png'), im)
		# plt.imshow(im)
		# plt.show()

def crop_letters(letter_dir):
	letter_imgs = os.listdir(letter_dir)
	for im_fname in letter_imgs:
		im = imread(os.path.join(letter_dir, im_fname))
		cropped_im = im[Y_LOC[0]:Y_LOC[1], X_LOC[0]:X_LOC[1]]
		imsave(os.path.join(letter_dir, im_fname.split('.')[0] + '_cropped.png'), cropped_im)

if __name__ == '__main__':
	# save_letters()
	crop_letters('data')

