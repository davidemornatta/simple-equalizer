import PIL
import numpy
import math
from PIL import Image
from numpy import asarray
from numpy import array
from numpy import log2
from math import floor

to_equalize = Image.open('prova2.jpg')
to_equalize = to_equalize.convert('L')
to_equalize.show()
data = asarray(to_equalize)
equalizedArray = numpy.empty_like(data);

max_value = 0;
min_value = 0;

for i in range(int(data.size/data[0].size)):
    for j in range(data[0].size):
        if data[i][j] > max_value: max_value = data[i][j]
        if data[i][j] < min_value: min_value = data[i][j]

delta_value = max_value - min_value
shift_level = 8-floor(log2(delta_value+1))

for i in range(int(data.size/data[0].size)):
    row = numpy.empty_like(data[0])
    for j in range(data[0].size):
        temp_pixel = int((data[i][j] - min_value) * math.pow(2, shift_level))
        new_pixel = min(255, temp_pixel)
        row[j] = new_pixel
    equalizedArray[i]=row

equalized = Image.fromarray(equalizedArray)
equalized.show()