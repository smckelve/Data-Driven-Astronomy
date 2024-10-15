# Write your calc_stats function here.
import numpy as np

def calc_stats(file_name):
  data = np.loadtxt(file_name, delimiter = ',')
  mean = np.mean(data)
  median = np.median(data)
  return (round(mean, 1), round(median, 1))

# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # Run your `calc_stats` function with examples:
  mean = calc_stats('data2.csv')
  
  # Set print options globally using a context manager
  with np.printoptions(formatter={'float_kind': '{:0.1f}'.format}, suppress=True):
        print(mean)