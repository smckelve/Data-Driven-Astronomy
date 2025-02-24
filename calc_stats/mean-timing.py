import numpy as np
import statistics
import time

def time_stat(func, size, ntrials):
  total_time = 0
  for _ in range(ntrials):
    data = np.random.rand(size)
    start_time = time.time()
    func(data)
    total_time += time.time() - start_time
    
  return total_time / ntrials
  
if __name__ == '__main__':
  print('{:.6f}s for statistics.mean'.format(time_stat(statistics.mean, 10**5, 10)))
  print('{:.6f}s for np.mean'.format(time_stat(np.mean, 10**5, 1000)))