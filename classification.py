"""Small classification example for the Git laboratory."""


def classify(value, threshold=0.5):
    """Return 1 when value reaches threshold, otherwise 0."""
    return int(value >= threshold)
