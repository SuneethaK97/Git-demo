import sys

def hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    hanoi(n - 1, source, auxiliary, target)
    print(f"Move disk {n} from {source} to {target}")
    hanoi(n - 1, auxiliary, target, source)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python hanoi.py <number_of_disks>")
        sys.exit(1)
    
    try:
        num_disks = int(sys.argv[1])
        if num_disks <= 0:
            raise ValueError("Number of disks must be a positive integer.")
    except ValueError as e:
        print(e)
        sys.exit(1)

    hanoi(num_disks, 'A', 'C', 'B')
