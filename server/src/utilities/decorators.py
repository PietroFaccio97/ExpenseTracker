
def alias(new_name):
    def decorator(func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        globals()[new_name] = func
        return wrapper

    return decorator
