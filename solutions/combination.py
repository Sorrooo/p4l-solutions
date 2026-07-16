# Insert your combination() function here, along with any subroutines that you need.
def combination(n: int, k: int) -> int:
    """
    Compute the combination statistic C(n, k) = n! / ((n - k)! * k!).
    Args:
        n: Total number of distinct objects (non-negative).
        k: Size of the subset to choose (non-negative).
    Returns:
        The number of ways to choose k items from n without order (the binomial coefficient).
    """
    if k < 0 or k > n:
        return 0

    k = min(k, n - k)
    result = 1

    for i in range(1, k + 1):
        result = result * (n - k + i) // i

    return result
    pass
