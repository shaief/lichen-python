from PIL import Image
import numpy as np
import ImageFilter

print "Please write a file name to analysis: "
user_image = raw_input()

print "Plese enter thresholds: [low, high]: "
print "For example - [150, 200]"
user_thresholds = raw_input()

# lichen_im = Image.open("Lichen.jpg")

lichen_im = Image.open(user_image)

lichen_im.show()
lichen_converted = lichen_im.convert('L')
lichen_converted.show()
lichen_blurred = lichen_converted.filter(ImageFilter.BLUR)
lichen_blurred.show()

original_ndarr = np.array(lichen_converted, dtype = float)

ndarr = np.array(lichen_blurred, dtype = float)

print ndarr

threshold = 150
ndarr[ndarr<threshold] = 0
ndarr[ndarr > 200] = 0
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

print "percentage: " + str(1.0*lichen_counter/counter)

lichen_threshold = Image.fromarray(ndarr)

lichen_threshold.show()