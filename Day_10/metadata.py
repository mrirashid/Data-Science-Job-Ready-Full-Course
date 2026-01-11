def wraps (original):
    def copy_metadata(wrapper):
        wrapper.__name__=original.__name__
        wrapper.__doc__=original.__doc__
        return wrapper
    return copy_metadata
    