import numpy as np

def angular_dist(ra1, dec1, ra2, dec2):
    # Convert all the input angles from degrees to radians    
    dec1_rad = np.radians(dec1)
    dec2_rad = np.radians(dec2)
    ra1_rad = np.radians(ra1)
    ra2_rad = np.radians(ra2)
    
    a = np.sin(dec1_rad) * np.sin(dec2_rad)
    b = np.cos(dec1_rad) * np.cos(dec2_rad) * np.cos(ra1_rad - ra2_rad)
       
    return np.degrees(np.arccos(a + b))  #return the angular distance in degrees

# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # Run your function with the first example in the question.
  print(angular_dist(21.07, 0.1, 21.15, 8.2))

  # Run your function with the second example in the question
  print(angular_dist(10.3, -3, 24.3, -29))