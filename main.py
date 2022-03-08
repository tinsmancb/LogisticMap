import matplotlib.pyplot as plt

def logistic_iter(x, r):
  return r*x*(1-x)

r = 3.75
x0 = 0.3
xs = [x0]
for i in range(500):
  xs.append(logistic_iter(xs[-1], r))
  
plt.plot(xs, '.')
plt.show()