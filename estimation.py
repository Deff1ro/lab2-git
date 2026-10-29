"""Estimation module: starting point for the release exercise."""


def estimate(values):
    """Return the number of supplied observations."""
    return len(values)


def mean(values):
    """Return the arithmetic mean; reject an empty collection."""
    if not values:
        raise ValueError("Cannot estimate the mean of an empty collection")
    return sum(values) / len(values)
