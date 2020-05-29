import matplotlib.pyplot as plt

import numpy as np
import matplotlib.pyplot as plt

import skimage
import skimage.external.tifffile

import os



#zoom call timestamp 19:00
width = 23;
height = 69;
every = 5;




#####################################################################################
#####################################################################################
#!/usr/bin/env python

from argparse import ArgumentParser
import os.path


def is_valid_file(parser, arg):
    if not os.path.exists(arg):
        parser.error("The file %s does not exist!" % arg)
    else:
        return open(arg, 'r')  # return an open file handle


parser = ArgumentParser(description="create subpictures")
parser.add_argument("-i", dest="input filename", required=True,
                    help="input file with the image", metavar="FILE",
                    type=lambda x: is_valid_file(parser, x))
parser.add_argument("-o", dest="output folder", required=True,
                    help="output folder with the image", metavar="FILE",
                    type=lambda x: is_valid_file(parser, x))
args = parser.parse_args()

A, B = read(args.filename)
C = ikjMatrixProduct(A, B)
printMatrix(C)



import argparse
parser = argparse.ArgumentParser(description='Add some integers.')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='interger list')
parser.add_argument('--sum', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')
args = parser.parse_args()
print(args.sum(args.integers))




#import mask
input_image_path = os.path.abspath(os.path.join('/Users/johannesschoeneberg/Desktop/SchoenebergLab_Cal/collaboration_daniel_Serwas/PositiveControl/FilamentProjections/TomoJune_Fil06_Projection_crop.tif'))
output_folder_path = os.path.abspath(os.path.join('/Users/johannesschoeneberg/Desktop/SchoenebergLab_Cal/collaboration_daniel_Serwas/PositiveControl/FilamentProjections/output/'))







image = skimage.external.tifffile.imread(input_image_path)
print(image.shape)
plt.imshow(image,cmap='gray')

print(np.min(image))
globalMin = np.min(image)
print(np.max(image))
globalMax = np.max(image)








import time
start_time = time.time()



totalHeight = image.shape[0]
print(totalHeight);
nSubpictures = (np.floor(((totalHeight-height)/every))).astype(int)
subpictures = []
for i in range(0,nSubpictures):
    print(i)
    subpicture = image[i*every:height+i*every,:]

    skimage.external.tifffile.imsave(output_folder_path+"/output_"+str(i).zfill(5)+".tiff", subpicture, imagej=True );

#    plt.imshow(subpicture,cmap='gray')
#    plt.show()
#    subpictures.append(subpicture)


print("--- %s seconds ---" % (time.time() - start_time))






w=10
h=90
fig=plt.figure(figsize=(w, h))
columns = 5
rows = 9
for i in range(1, columns*rows +1):
    img = np.random.randint(10, size=(h,w))
    fig.add_subplot(rows, columns, i)
    plt.imshow(subpictures[i],vmin=globalMin, vmax=globalMax,cmap='gray')
plt.show()
