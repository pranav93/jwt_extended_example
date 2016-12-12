def non_empty_str(val):
    if isinstance(val, basestring) and val.strip():
        return val
    raise ValueError
