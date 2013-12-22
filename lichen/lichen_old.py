#! /usr/bin/python
"""
Lichen is an image analysis module intend to calculate covering percentages of lichens on rocks.
Lichen returns a text file contains list of results.

                    Created by: Shai Efrati, 12/2013
                    http://github.com/shaief/lichen
                            http://shaief.com
                            shaief@gmail.com

Run standalone as:
python lichen.py

Functions
---------
analyze_image(user_image, low_threshold, high_threshold) -> counter, lichen_counter, percentage
user_interaction() -> null

Notes
-----
default parameters (DEFAULT_LOW, DEFAULT_HIGH, DEFAULT_DIRECTORY, DEFAULT_IMAGE) are in DEAFAULTS.py

Usage:
  lichen.py
  lichen.py defaults ([s | single] | [d | directory])
  lichen.py (-l=LOWER-TH) (-u=UPPER-TH) (-d=PATH | -s=FILE)
  lichen.py -h | --help | --version
    
Options:
  -v --version                     Show version
  -l=LOWER-TH --lower=LOWER-TH       lower threshold [default: 0-255]
  -u=UPPER-TH --upper=UPPER-TH     upper threshold [default: 0-255]
  -s=FILE --single=FILE            Single image
  -d=PATH --directory=PATH         Directory contains images for analysis
  -h --help                        Show this screen

"""

import os
import csv
try:
    from PIL import Image, ImageFilter
except:
    exit('Lichen requires Pillow. Please install it using pip install Pillow')
try:
    from docopt import docopt
except ImportError:
    exit('Lichen requires docopt. Please install it using pip install docopt')
import numpy as np
# DEFAULTS.py contains all the defaults for the analysis.
from DEFAULTS import *

#[(-l) (-u)] [-s] [-d] [-h] [-v]
# Arguments
#   low_th Low threshold
#   high_th High threshold
#   single_dir single image or direcotry
#   directory Directory
#   image Single image

def analyze_image(user_image, low_threshold, high_threshold):
    '''
    
    '''
    # open an image
    lichen_im = Image.open(user_image)
    
    # convert the image to grayscale
    lichen_converted = lichen_im.convert('L')
    
    lichen_blurred = lichen_converted.filter(ImageFilter.BLUR)
    
    
    original_ndarr = np.array(lichen_converted, dtype = float)
    
    ndarr = np.array(lichen_blurred, dtype = float)
    
    # print ndarr
    
    ndarr[ndarr<low_threshold] = 0
    ndarr[ndarr > high_threshold] = 0
    ndarr[ndarr != 0] = 255
    
#     print ndarr
    counter = 0
    lichen_counter = 0
    for li in np.nditer(ndarr):
        counter +=1
        if li == 255.:
            lichen_counter +=1
           
    percentage = 1.0*lichen_counter/counter
     
#     print "counter: " + str(counter)
#     print "lichen counter: " + str(lichen_counter)
#     print "percentage: " + str(percentage)
#     
    lichen_threshold = Image.fromarray(ndarr)
    
    # show images:
#     lichen_im.show()
#     lichen_converted.show()
#     lichen_blurred.show()
#     lichen_threshold.show()

    return counter, lichen_counter, percentage

def run_defaults(single_dir):
    ''' this function deals with user's requests'''
    low_threshold = DEFAULT_LOW
    high_threshold = DEFAULT_HIGH
    low_threshold = int(low_threshold)
    high_threshold = int(high_threshold)
    if single_dir.upper == 'SINGLE':
        print DEFAULT_IMAGE
        user_image = DEFAULT_IMAGE    
        c,l,p = analyze_image(user_image, low_threshold, high_threshold)
        # output files names and percentages to csv
        user_csv = user_image + ".csv"
        out = open(user_csv, 'w')
        out.write('Image name; Percentages\n')
        out.write('%s; %1.3f\n' % (user_image, p))
        out.close()
    
    if single_dir.upper() == 'DIRECTORY':
        image_list = []
        counter_list = []
        lichen_list = []
        percentage_list = []
        print DEFAULT_DIRECTORY
        user_directory = DEFAULT_DIRECTORY
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
                c,l,p = analyze_image(files, low_threshold, high_threshold)
                counter_list.append(c)
                lichen_list.append(l)
                percentage_list.append(p)
                image_list.append(files)
        print counter_list
        print lichen_list
        print percentage_list
        print image_list
        
        # create a list of file names and results
        data = []
        data.append(image_list)
        data.append(percentage_list)
        
        # output files names and percentages to csv
        out = open(user_csv, 'w')
        print data
        out.write('Image name; Percentages\n')
        for i,j in enumerate(data[0][:]):
            out.write('%s; %1.3f\n' % (data[0][i],data[1][i]))
        out.close()
        
def user_interaction():
    ''' this function deals with user's requests'''
    print "Plese enter thresholds (default values - ({}, {})):\n low (0-255): ".format(DEFAULT_LOW, DEFAULT_HIGH)
    low_threshold = raw_input()
    if not low_threshold:
        print "150"
        low_threshold = DEFAULT_LOW
    print "high (0-255): "
    high_threshold = raw_input()
    if not high_threshold:
        print "200"
        high_threshold = DEFAULT_HIGH
    low_threshold = int(low_threshold)
    high_threshold = int(high_threshold)
    print "Would you like to work on a (s)ingle image or on a (d)irectory?: "
    print "(default - single image)"
    single_dir = raw_input()
    if not single_dir:
        print "(s) - single image"
        single_dir = "S"
    if single_dir.upper() == 'S':
        print "Please write a file name to analyze (default {}): ".format(DEFAULT_IMAGE)
        user_image = raw_input()
        if not user_image:
            print DEFAULT_IMAGE
            user_image = DEFAULT_IMAGE    
        c,l,p = analyze_image(user_image, low_threshold, high_threshold)
        # output files names and percentages to csv
        user_csv = user_image + ".csv"
        out = open(user_csv, 'w')
        out.write('Image name; Percentages\n')
        out.write('%s; %1.3f\n' % (user_image, p))
        out.close()


        
    if single_dir.upper() == 'D':
        image_list = []
        counter_list = []
        lichen_list = []
        percentage_list = []
        print "Please write directory path to analyze: "
        print "output file will be saved there as well."
        print "(default path: {})".format(DEFAULT_DIRECTORY)
        user_directory = raw_input()
        if not user_directory:
            print DEFAULT_DIRECTORY
            user_directory = DEFAULT_DIRECTORY
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
                c,l,p = analyze_image(files, low_threshold, high_threshold)
                counter_list.append(c)
                lichen_list.append(l)
                percentage_list.append(p)
                image_list.append(files)
        print counter_list
        print lichen_list
        print percentage_list
        print image_list
        
        # create a list of file names and results
        data = []
        data.append(image_list)
        data.append(percentage_list)
        
        # output files names and percentages to csv
        out = open(user_csv, 'w')
        print data
        out.write('Image name; Percentages\n')
        for i,j in enumerate(data[0][:]):
            out.write('%s; %1.3f\n' % (data[0][i],data[1][i]))
        out.close()
        
if __name__ == '__main__':
    args = docopt(__doc__, version='0.1.0')
    print(args)
    if args['defaults']:
        if args['single'] or args['s']:
            run_defaults('S')
        if args['directory'] or args['d']:
            run_defaults('D')
