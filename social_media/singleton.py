
class Expensive():
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("Creating new instance")
            print("Do hard work here that we want to do only once.")
            cls._instance = super().__new__(cls)
        else:
            print("Reuse instance")
        return cls._instance
    
    def __init__(self):
        print("Careful, initialization is done each time.")
    
exp1 = Expensive()
exp2 = Expensive()
exp3 = Expensive()


print("\navoid repeated initialization")
class Expensive:
    _instance = None
    _initialized = False

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not self._initialized: 
            print("Doing expensive initialization once")
            self._initialized = True

exp1 = Expensive()
exp2 = Expensive()
exp3 = Expensive()


print("\nbut maybe using a cached function is cleaner?")
from functools import cache

class Expensive:
    def __init__(self, singleton = None):
        if singleton != "overwrite":
            raise TypeError("Use get_expensive() instead of Expensive()")
        print("Doing expensive initialization once")

@cache
def get_expensive():
    return Expensive(singleton = "overwrite")

exp1 = get_expensive()
exp2 = get_expensive()
exp3 = get_expensive()
