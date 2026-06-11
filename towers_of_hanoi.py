
ivt_tree.hide_calls.add('print_state')

def towers_of_hanoi_with_state(n: int) -> None:
    if n <= 0:
        raise ValueError("n must be a positive integer")

    towers = {
        "A": list(range(n, 0, -1)),
        "B": [],
        "C": [],
    }

    def print_state() -> None:
        print(f"A: {towers['A']}    B: {towers['B']}    C: {towers['C']}")

    def move(num_disks: int, source: str, target: str, auxiliary: str) -> None:
        if num_disks == 1:
            disk = towers[source].pop()
            towers[target].append(disk)
            print(f"Move disk {disk} from {source} to {target}")
            print_state()
            return

        move(num_disks - 1, source, auxiliary, target)

        disk = towers[source].pop()
        towers[target].append(disk)
        print(f"Move disk {disk} from {source} to {target}")
        print_state()

        move(num_disks - 1, auxiliary, target, source)

    print("Initial state:")
    print_state()
    print()

    move(n, "A", "C", "B")


# Example
towers_of_hanoi_with_state(4)
