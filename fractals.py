import numpy

def in_circle(z, radius):
  return z.real ** 2 + z.imag ** 2 < radius ** 2

def fractal_eta(func, z, limit, radius=2):
    cnt = 0
    while in_circle(z, radius):
        cnt += 1
        if cnt >= limit:
            break
        z = func(z)
    return cnt

def cqp(c):
  """ Complex quadratic polynomial, function used for Mandelbrot fractal """
  return lambda z: z ** 2 + c

def get_model(model, depth, c):
  """ Returns the fractal model function """
  if model == "julia":
    func = cqp(c)
    return lambda x, y: fractal_eta(func, x + y * 1j, depth)
  if model == "mandelbrot":
    return lambda x, y: fractal_eta(cqp(x + y * 1j), 0j, depth)
  raise ValueError("Fractal not found")

def translate_coordinates(size, center, zoom):
    width, height = size
    cx, cy = center
    side = max(width, height)
    sidem1 = side - 1
    delta_x = (side - width) / 2  # Centralize
    delta_y = (side - height) / 2

    def func(row, col):
        y = (2 * (height - row + delta_y) / sidem1 - 1) / zoom + cy
        x = (2 * (col + delta_x) / sidem1 - 1) / zoom + cx
        return x, y

    return func

def make_fractal(model, c=None, depth=256, size=(512, 512),
                 zoom=1.0, center=(0.0,0.0)):
    func = get_model(model, depth, c)
    t = translate_coordinates(size, center, zoom)

    img = numpy.empty(size)
    width, height = size
    for row in range(width):
        for col in range(height):
            img[row, col] = func(*t(row, col))

    return img