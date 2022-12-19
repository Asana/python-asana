def merge_dicts(*objects: dict):
    """Merge one or more objects into a new object"""
    result = {}
    for obj in objects:
        result.update(obj)
    return result
