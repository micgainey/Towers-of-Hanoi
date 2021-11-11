# Towers of Hanoi Recursive
# from towers_of_hanoi_count import towers_of_hanoi_moves

def tower_of_hanoi_recursive(num_of_disks, src, dest, aux):
    if num_of_disks == 1:
        print("Move disk 1 from", src, "to", dest)
        return

    tower_of_hanoi_recursive(num_of_disks - 1, src, aux, dest)
    print("Move disk", num_of_disks, "from", src, "to", dest)
    tower_of_hanoi_recursive(num_of_disks - 1, aux, dest, src)

num_of_disks = int(input("Enter number of disks: "))


tower_of_hanoi_recursive(num_of_disks, 'A', 'B', 'C')

num_of_moves = 2 ** num_of_disks - 1
# num_of_moves = towers_of_hanoi_moves(num_of_disks)
print('It took', num_of_moves, 'moves for', num_of_disks, 'disks')
