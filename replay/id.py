"""this module contains decorator for adding Id attribute to any object"""

__id = 0  # id counter


def set_id(fn):
    """add '_id' attribute to class

    try attach decorator to __init__ method
    """
    def wrapper(*args, **kwargs):
        if(len(args) > 0 and isinstance(args[0], object)):
            global __id
            __id += 1
            args[0].__setattr__('_id', __id)
        fn(*args, **kwargs)
    return wrapper
