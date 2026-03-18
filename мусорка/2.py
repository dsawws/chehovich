import math
W = lambda v, t: (0.004 * v + math.exp(2 * t)) / math.exp(t)
print(W(1, 2))
