# The 'Babylonian' method
# Essentially equivalent to Newton's method
def floor_sqrt_bab(n):
  guess = 1 << ((n.bit_length() + 1) >> 1)
  while True:
    # Updated guess is the midpoint of the current guess and n divided by current guess
    newton = (guess + n // guess) >> 1
    if newton >= guess:
      return guess
    guess = newton

def floor_sqrt_bakhshali(n):
  guess = 1 << ((n.bit_length() + 1) >> 1)
  guess = ((guess ** 2) * (guess ** 2 + 6 * n) + n ** 2) // (4 * guess * (guess ** 2 + n))
  while True:
    a = (n - guess ** 2) // (2 * guess)
    xn = (guess + a) - ((a ** 2) // (2 * (guess + a)))
    if xn >= guess:
      return guess
    guess = xn

def floor_sqrt_halley(n):
  guess = 1 << ((n.bit_length() + 1) >> 1)
  while True:
    xn = (guess ** 3 + 3 * n * guess) // (3 * guess ** 2 + n)
    if xn >= guess:
      return guess
    guess = xn


