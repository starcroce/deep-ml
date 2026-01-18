import numpy as np

def descriptive_statistics(data: list | np.ndarray) -> dict:
    """
    Calculate various descriptive statistics metrics for a given dataset.
    
    Args:
        data: List or numpy array of numerical values
    
    Returns:
        Dictionary containing mean, median, mode, variance, standard deviation,
        percentiles (25th, 50th, 75th), and interquartile range (IQR)
    """
    # Your code here
    mean = np.mean(data)
    median = np.median(data)

    vals, counts = np.unique(data, return_counts=True)
    max_count_index = np.argmax(counts)
    mode = vals[max_count_index]
    # print(vals, counts)
    # print(max_count_index, mode)

    variance = np.var(data)
    standard_deviation = np.std(data)

    quartiles = np.percentile(data, [25, 50, 75])

    return {
        "mean": mean,
        "median": median,
        "mode": mode,
        "variance": variance,
        "standard_deviation": standard_deviation,
        "25th_percentile": quartiles[0],
    