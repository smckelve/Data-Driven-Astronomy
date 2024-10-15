# Write your calculate_mean function here.
def calculate_mean(arr):
  mean = sum(arr)/len(arr)
  return mean

# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # Run your `calculate_mean` function with examples:
  mean = calculate_mean([1.2, 3.8, 2.2, 8.2, 7.1])
  print(mean)