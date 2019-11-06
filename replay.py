id = 0


def set_id(fn):  # ====================== or add metaclass
    def wrapper(*args, **kwargs):
        if(len(args) > 0 and isinstance(args[0], object)):
            global id
            id += 1
            args[0].__setattr__('_id', id)
        fn(*args, **kwargs)
    return wrapper


class Loger:
    @staticmethod
    def unit_attacks(fn):
        def wrapper(*args, **kwargs):
            units = [unit
                     for unit in args
                     if(hasattr(unit, '_id') and hasattr(unit, 'damage'))
                     ]
            result = fn(*args, **kwargs)
            print(
                f'юнит {units[0]._id} наносит юниту {units[1]._id} {units[0].damage} единиц урона')
            return result
        return wrapper

    @staticmethod
    def unit_low_health(fn):
        def wrapper(unit, health):
            if(health <= 0):
                print(
                    f'юнит {unit._id} уничтожен')
            return fn(unit, health)
        return wrapper

    @staticmethod
    def division_destroy(fn):
        def wrapper(division, subj):
            if(len(division.subjects) == 1):
                if(hasattr(division, 'name')):
                    print(
                        f'армия {division.name} уничтожена')
                else:
                    print(
                        f'отряд {division._id} уничтожен')
            result = fn(division, subj)
            return result
        return wrapper


"""
События в игре:
Атака одного юнита другим юнит id наносит юниту id N единиц урона до N единиц здоровья +
Уничтожение юнита # юнит id уничтожен юнитом id +
Уничтожение отряда id+
Уничтожение армии name
Победа армии name
"""
