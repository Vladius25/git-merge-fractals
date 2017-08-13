
import time

from matplotlib import pyplot as plt
from fractals import make_fractal

import argparse

parser = argparse.ArgumentParser(description='Short sample app')

parser.add_argument('--model', default="julia")
parser.add_argument('--size', type=int, default=256)
parser.add_argument('--depth', type=int, default=64)
#TODO: zoom
#TODO: center x, y
#TODO: some other? colormap?

args = parser.parse_args()

# Do main work
start = time.perf_counter()


img = make_fractal(model=args.model,
                   size=(args.size, args.size),
                   depth=args.depth)
end = time.perf_counter()

print('Elapsed time (in seconds): {}'.format(end - start))
plt.imshow(img, cmap="cubehelix")
plt.show()