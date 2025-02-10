def tower_of_hanoi(n, source, auxiliary, target):
    if n == 0:
        return

    # Move n-1 disks from source to auxiliary
    tower_of_hanoi(n - 1, source, target, auxiliary)

    # Move the nth disk from source to target
    print(f"Move disk {n} from {source} to {target}")

    # Move n-1 disks from auxiliary to target
    tower_of_hanoi(n - 1, auxiliary, source, target)


# Number of disks
num_disks = 3  # You can change this number for different scenarios
tower_of_hanoi(num_disks, 'A', 'B', 'C')
