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
run_single(user_image, lower_th, upper_th) -> csv
run_directory(user_directory, lower_th, upper_th) -> csv

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
    import numpy as np
except:
    exit('Lichen requires numpy. Please install it using pip install numpy')
# DEFAULTS.py contains all the defaults for the analysis.

try:
    from docopt import docopt
except ImportError:
    exit('Lichen requires docopt. Please install it using pip install docopt')

# DEFAULTS.py contains all the defaults for the analysis.
from DEFAULTS import *
try:
    from lichen_analyze import run_single, run_directory
except:
    exit('Lichen main module - lichen_analyze.py is missing...')

if __name__ == '__main__':
    args = docopt(__doc__, version='0.1.0')
#     print(args)
    if args['defaults']:
        if args['single'] or args['s']:
            run_single(DEFAULT_IMAGE, DEFAULT_LOW, DEFAULT_HIGH)
        if args['directory'] or args['d']:
            run_directory(DEFAULT_DIRECTORY, DEFAULT_LOW, DEFAULT_HIGH)
    else:
        if args['--single'] <> None:
            run_single(args['--single'], args['--lower'], args['--upper'])
        if args['--directory'] <> None:
            run_directory(args['--directory'], args['--lower'], args['--upper'])
