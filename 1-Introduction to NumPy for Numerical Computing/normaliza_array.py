import numpy as np

def normalize_array(arr):
    """
    Normalize an array between 0 and 1.
    
    Parameters:
    arr (numpy array): Input array
    
    Returns:
    normalized_arr (numpy array): Normalized array
    """
    min_val = np.min(arr)
    max_val = np.max(arr)
    
    # Handle division by zero
    if max_val == min_val:
        return np.ones_like(arr)
    
    normalized_arr = (arr - min_val) / (max_val - min_val)
    return normalized_arr

# Example usage
arr = np.array([1, 2, 3, 4, 5])
normalized_arr = normalize_array(arr)
print(normalized_arr)