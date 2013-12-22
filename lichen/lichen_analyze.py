import os
import csv
try:
    from PIL import Image, ImageFilter
except:
    exit('Lichen requires Pillow. Please install it using pip install Pillow')
try:
    import numpy as np
except:
    exit('Lichen requires numpy. Please install it using pip install numpy')
# DEFAULTS.py contains all the defaults for the analysis.
from DEFAULTS import *


def analyze_image(user_image, low_threshold, high_threshold):
    '''
    
    '''
    # open an image
    lichen_im = Image.open(user_image)
    # convert the image to grayscale
    lichen_converted = lichen_im.convert('L')
    lichen_blurred = lichen_converted.filter(ImageFilter.BLUR)
    ndarr = np.array(lichen_blurred, dtype = float)
    ndarr[ndarr<low_threshold] = 0
    ndarr[ndarr > high_threshold] = 0
    ndarr[ndarr != 0] = 255
    counter = 0
    lichen_counter = 0
    for li in np.nditer(ndarr):
        counter +=1
        if li == 255.:
            lichen_counter +=1
    percentage = 1.0*lichen_counter/counter
    
    lichen_threshold = Image.fromarray(ndarr)
      #show images:
    lichen_im.show()
    lichen_converted.show()
    lichen_blurred.show()
    lichen_threshold.show()

    return counter, lichen_counter, percentage

def run_single(user_image, lower_th, upper_th):
    ''' this function deals with a single image'''
    c,l,p = analyze_image(user_image, lower_th, upper_th)
    # output files names and percentages to csv
    user_csv = user_image + ".csv"
    out = open(user_csv, 'w')
    out.write('Image name; Percentages\n')
    out.write('%s; %1.3f\n' % (user_image, p))
    out.close()
    print "Done analyzing {} with thresholds {}-{}".format(user_image, lower_th, upper_th) 
    print "check out {} to see the results".format(user_csv)
       
def run_directory(user_directory, lower_th, upper_th):
    ''' this function deals with a directory of images'''
    image_list = []
    counter_list = []
    lichen_list = []
    percentage_list = []
    os.chdir(user_directory)
    
    print "Please enter file name to save (*.csv): "
    print "(default file: {})".format(DEFAULT_CSV)
    user_csv = raw_input()
    if not user_csv:
        print DEFAULT_CSV
        user_csv = DEFAULT_CSV
    
    for files in os.listdir(user_directory):
        if files.endswith(".jpg") or files.endswith(".JPG"):
            print files
            c,l,p = analyze_image(files, lower_th, upper_th)
            counter_list.append(c)
            lichen_list.append(l)
            percentage_list.append(p)
            image_list.append(files)
#     print counter_list
#     print lichen_list
#     print percentage_list
#     print image_list
    
    # create a list of file names and results
    data = []
    data.append(image_list)
    data.append(percentage_list)
    
    # output files names and percentages to csv
    out = open(user_csv, 'w')
#     print data
    out.write('Image name; Percentages\n')
    for i,j in enumerate(data[0][:]):
        out.write('%s; %1.3f\n' % (data[0][i],data[1][i]))
    out.close()
    print "Done analyzing {} with thresholds {}-{}".format(user_directory, lower_th, upper_th)
    print "check out {}{} to see the results".format(user_directory, user_csv)