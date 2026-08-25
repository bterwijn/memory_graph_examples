import random 
import itertools as it

pr = lambda s,i: print(s,i) or i

def packages():
    while True:
        yield pr('package:', random.randrange(200))  # pounds

def pound_to_kg(p):
    return round(p * 0.453592, 2)
        
def small(p):
    if p < 50:
        return True

def fill_container(stream, max_weight):
    weight = 0
    container = []
    for p in stream:
        nw = weight + p
        if nw <= max_weight:
            container.append(p)
            weight = nw
        else:
            yield pr('container:', (container, weight))
            container = [p]
            weight = p
    
def truck_packages(stream):
    stream = (pr('pound_to_kg:', pound_to_kg(p)) for p in stream)
    stream_small, stream_large = it.tee(stream, 2)
    stream_small = (pr('small:', p) for p in stream_small if small(p))
    stream_large = (pr('large:', p) for p in stream_large if not small(p))
    containers_small = fill_container(stream_small, 50)
    containers_large = fill_container(stream_large, 200)
    while True:
        truck = (list(it.islice(containers_small, 5)), 
                 list(it.islice(containers_large, 2)))
        yield truck

stream = packages()
stream = truck_packages(stream)

for truck in it.islice(stream, 10):
    print(truck)
