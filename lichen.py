from PIL import Image
import numpy as np

lichen_im = Image.open("Lichen.jpg")
# lichen_im.show()
lichen_converted = lichen_im.convert('L')
# lichen_converted.show()

original_ndarr = np.array(lichen_converted, dtype = float)

ndarr = np.array(lichen_converted, dtype = float)

print ndarr

threshold = 150
ndarr[ndarr<threshold] = 0
ndarr[ndarr > 175] = 0
ndarr[ndarr != 0] = 255


print ndarr
counter = 0
lichen_counter = 0
for li in ndarr:
    counter +=1
#     if np.allclose(li, [0, 0, 0]) :
#         lichen_counter +=1
        
print "counter: " + str(counter)
print "lichen counter: " + str(lichen_counter)

print "percentage: " + str(1.0*lichen_counter/counter)

lichen_threshold = Image.fromarray(ndarr)
# lichen_threshold.show()

nd = ndarr
nd = 0
# lichen_combined = Image.fromarray(ndarr[original_ndarr==255])
# lichen_threshold.show()

