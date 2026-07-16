ivt_tree.hide_calls.add('print_state')
ivt_tree.hide_calls.add('move_disk')

def print_state(towers):
    print(f"A:{towers['A']}    B:{towers['B']}    C:{towers['C']}")

def move_disk(towers, source: str, target: str):
    disk = towers[source].pop()
    print(f'move {disk} from {source} to {target}')
    towers[target].append(disk)

def move(towers, n, source, target, auxiliary):
    if n == 1:
        move_disk(towers, source, target)
        print_state(towers)
        return
    if n % 2 == 1:
        move(towers, n-1, source, auxiliary, target)
        move(towers, 1,   source, target, auxiliary)
        move(towers, n-1, auxiliary, target, source)
    else:
        move(towers, n-1, source, auxiliary, target)
        move(towers, 1,   source, target, auxiliary)
        move(towers, n-1, auxiliary, target, source)
    
def towers_of_hanoi(n: int):
    if n <= 0:
        raise ValueError("n must be a positive integer")
    towers = {
        "A": list(range(n, 0, -1)),
        "B": [],
        "C": [],
    }    
    print("Initial state:")
    print_state(towers)
    print()
    move(towers, n, "A", "C", "B")  # start recursion

# Example
towers_of_hanoi(3)
