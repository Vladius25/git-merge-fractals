

from matplotlib import pyplot as plt
from fractals import make_fractal

img = make_fractal('mandelbrot', size=(256, 256), depth=64)
plt.imshow(img, cmap="cubehelix")
plt.show()