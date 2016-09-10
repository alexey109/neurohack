# I dont know why it call 'vine'. Just take it as is.

from PIL import Image
from PIL import ImageDraw
from PIL import ImageOps
import numpy as np
from sklearn import preprocessing
import os

# Procedure convert image to grayscale, put it in a circle and make several copies, 
# rotated for 45 degress.
# It takes name of directory with images, image file name, and counter of all images.
def born_new (dir_name, file_name, counter):
	background_color = 127 # color outside image
	no_transparent   = 255 # pixel transparent value 0 - transparent, 255 - no transparent

	# Load image and convert it to grayscale.
	output = im = Image.open(file_name).convert('LA')

	# Creating mask image.
	mask = Image.new('L', im.size, 0)
	draw = ImageDraw.Draw(mask) 
	draw.ellipse((1, 1) + (im.size[0]-1,im.size[1]-1), fill=255)
	#draw.ellipse((0, 0) + im.size, fill=255) 
	# you can write like this, but some black dots could appear in the image.

	# Make several rotated copies.
	for i in range(0,360,45):
		# Apply mask
		output = ImageOps.fit(output, mask.size, centering=(0.5, 0.5))
		output.putalpha(mask)

		# Fill blank space our background color.
		out_px = output.load()
		for y in xrange(output.size[1]):
		    for x in xrange(output.size[0]):
		        if out_px[x, y][1] == 0:
		            out_px[x, y] = (background_color, no_transparent)

		# Save image in a copy of the directory with adding "_fan"
		output = output.convert('RGBA')
		output.save('../'+ dir_name + '_fan/'+ dir_name + str(counter) + '_' + str(i) + '.png')
		output = im.rotate(i+45)


dir_name = 'ill' # Yep, I can do it automatically, using os module, but I'm not want.
counter = 1
# Fan all 'png' files in the directory.
for file in os.listdir('../' + dir_name):
    if file.endswith('.png'):
		born_new(dir_name, file, counter)
		print ('Image No ' + str(counter) + '\r')
		counter += 1

