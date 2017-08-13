
import time

from matplotlib import pyplot as plt
from fractals import make_fractal

start = time.perf_counter()
img = make_fractal(size=(256, 256), depth=64)
end = time.perf_counter()

print('Elapsed time (in seconds): {}'.format(end - start))
plt.imshow(img, cmap="cubehelix")
plt.show()