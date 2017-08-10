import pyscreenshot as ImageGrab
import string
import ipdb
import matplotlib.pyplot as plt
import time
from scipy.misc import imsave
import os
from scipy.misc import imread
from scipy.misc import imresize
import numpy as np

X_LOC = [146, 212]
Y_LOC = [1232, 1308]

# make sure the terminal where this is printing is open when you call this
def screenshot_screen(letter):
	print '    ' + letter
	print '\n'
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
		if 'cropped' in im_fname or '.DS' in im_fname:
			continue
		im = imread(os.path.join(letter_dir, im_fname))
		

		cropped_im = im[Y_LOC[0]:Y_LOC[1], X_LOC[0]:X_LOC[1]]
		# plt.imshow(cropped_im)
		# plt.show()
		cropped_im = imresize(cropped_im, [28, 28])
		imsave(os.path.join(letter_dir, im_fname.split('.')[0] + '_cropped.png'), cropped_im)

def remove_full_screenshots(data_dir):
	files = os.listdir(data_dir)
	for f in files:
		if 'cropped' not in f and '.DS' not in f:
			os.remove(os.path.join(data_dir, f))

def fix_im_dimensions(data_dir):
	im_list = os.listdir(data_dir)
	for im in im_list:
		img = imread(os.path.join(data_dir, im))
		# img = img[:, :, 0]
		img = np.invert(img)
		imsave(os.path.join(data_dir, im), img)

if __name__ == '__main__':
	# save_letters()
	# crop_letters('data')
	# remove_full_screenshots('data')
	fix_im_dimensions('data/letters')
