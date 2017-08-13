
import time
import sys

from matplotlib import pyplot as plt
from fractals import make_fractal

size = int(sys.argv[1]) if len(sys.argv) == 2 else 256

start = time.perf_counter()
img = make_fractal('mandelbrot', size=(size, size), depth=64)
end = time.perf_counter()

print('Elapsed time (in seconds): {}'.format(end - start))
plt.imshow(img, cmap="cubehelix")
plt.show()