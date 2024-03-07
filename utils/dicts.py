def get_val(collection, key, default='git'):
    if not isinstance(collection, dict):
        raise TypeError

    return collection.setdefault(key, default)
