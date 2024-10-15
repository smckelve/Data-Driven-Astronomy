import numpy as np
import pandas as pd

def mean_datasets(file_list):
    # Read all CSV files into a list of DataFrames
    dataframes = [pd.read_csv(file, header = None, skip_blank_lines = False) for file in file_list]
    
    # Ensure all DataFrames have the same shape
    shape = dataframes[0].shape
    for df in dataframes:
        if df.shape != shape:
            raise ValueError("All datasets must have the same shape.")
    
    # Stack the DataFrames along a new dimension and calculate the mean along that dimension
    mean_array = np.nanmean(np.stack([df.values for df in dataframes]), axis=0)
    
    # Round the result to one decimal place
    mean_array = np.round(mean_array, 1)
    
    return mean_array

# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
    # Run your function with the first example from the question:
    print(mean_datasets(['data1.csv', 'data2.csv', 'data3.csv']))

    # Run your function with the second example from the question:
    print(mean_datasets(['data4.csv', 'data5.csv', 'data6.csv']))
