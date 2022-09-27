import numpy as np

def basic_stats(np_array):
    print(f"Original  array:\n{np_array}\nFlattened array: {np_array.flatten()}\nIt consists of {len(np_array.flatten())} values\n" +
    f"Number of elements in the each dimension: {np_array.shape}\nMaximum value: {np.amax(np_array)}\nMinimum value: {np.amin(np_array)}\n" + 
    f"Minimum values per rows: {np_array.min(axis=1)}\nMaximum values per rows: {np_array.max(axis=1)}\nMinimum values per columns: {np_array.min(axis=0)}\n" + 
    f"Maximum values per columns: {np_array.max(axis=0)}\nSummation value: {np.sum(np_array)}\nAverage value: {np.mean(np_array)}")
basic_stats(np.array([[2, 4], [0, 7]]))