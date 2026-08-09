# Insert your permutation() function here, along with any subroutines that you need.
from exercises.combination.combination import combination

def factorial(n: int) -> int:
    result = 1
    for value in range(2, n + 1):
        result *= value
    return result

def permutation(n: int, k: int) -> int:
    """
    Compute the permutation statistic P(n, k) = n · (n-1) · ... · (n-k+1) = n! / (n-k)!.
    Args:
        n: Total number of distinct objects (non-negative).
        k: Number of positions to fill (non-negative).
    Returns:
        The number of ways to choose and order k items from n, i.e., P(n, k).
    """
    result = 1
    for i in range(k):
        result *= n - i
    
    return combination(n, k) * factorial(k)