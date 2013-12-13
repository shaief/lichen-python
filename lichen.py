import os
from PIL import Image
import numpy as np
import ImageFilter
from DEFAULTS import *

def analyze_image(user_image, low_threshold, high_threshold):
    # lichen_im = Image.open("Lichen.jpg")
    
    lichen_im = Image.open(user_image)
    
    lichen_im.show()
    lichen_converted = lichen_im.convert('L')
    lichen_converted.show()
    lichen_blurred = lichen_converted.filter(ImageFilter.BLUR)
    lichen_blurred.show()
    
    original_ndarr = np.array(lichen_converted, dtype = float)
    
    ndarr = np.array(lichen_blurred, dtype = float)
    
    # print ndarr
    
    ndarr[ndarr<low_threshold] = 0
    ndarr[ndarr > high_threshold] = 0
    ndarr[ndarr != 0] = 255
    
    print ndarr
    counter = 0
    lichen_counter = 0
    for li in np.nditer(ndarr):
        counter +=1
        if li == 255.:
            lichen_counter +=1
            
    print "counter: " + str(counter)
    print "lichen counter: " + str(lichen_counter)
    percentage = 1.0*lichen_counter/counter
    print "percentage: " + str(percentage)
    
    lichen_threshold = Image.fromarray(ndarr)
    lichen_threshold.show()

    return counter, lichen_counter, percentage

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
    print "Would you like to work on a (s)ingle image or on a (d)irectory?: (default - single image)"
    single_dir = raw_input()
    if not single_dir:
        print "(s) - single image"
        single_dir = "S"
    if single_dir.upper() == 'S':
        print "Please write a file name to analyze: "
        user_image = raw_input()
        if not user_image:
            print DEFAULT_IMAGE
            user_image = DEFAULT_IMAGE    
        analyze_image(user_image, low_threshold, high_threshold)
    if single_dir.upper() == 'D':
        counter_list = []
        lichen_list = []
        percentage_list = []
        print "Please write directory path to analyze: "
        user_dir = raw_input()
        os.chdir(user_dir)
        if not user_directory:
            print DEFAULT_DIRECTORY
            user_directory = DEFAULT_DIRECTORY
        for files in os.listdir(user_directory):
            if files.endswith(".jpg") or files.endswith(".JPG"):
                print files
                c,l,p = analyze_image(files, low_threshold, high_threshold)
                counter_list.append(c)
                lichen_list.append(l)
                percentage_list.append(p)
        print counter_list
        print lichen_list
        print percentage_list

user_interaction()