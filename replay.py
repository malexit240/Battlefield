#unit_id do unit_id


class Loger:
    def __init__(self):
        pass

    def on_hit(self,log_write: str):
        def decorator(hit_fn):
            def wrapper():
                print('try hit')
                return hit_fn()
        return wrapper
    return decorator

log = Loger()
