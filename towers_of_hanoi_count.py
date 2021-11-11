"""
    Towers of Hanoi rules
    1. You can't place a larger disk onto a smaller disk.
    2. Only 1 disk can be moved at a time.

    Towers of Hanoi moves is:
    2^n - 1
    OR
    2 * previous + 1

    example with 3 disks
    3 towers: A. B. C.

Starting point:
    1
    2
    3
    A   B   C

Move1
    2
    3       1
    A   B   C

Move2
    3   2   1
    A   B   C

Move3
        1
    3   2
    A   B   C

Move4
        1
        2   3
    A   B   C

Move5
    1   2   3
    A   B   C

Move6
            2
    1       3
    A   B   C

Move7
            1
            2
            3
    A   B   C
"""

"""
    Iterative approach:
    for one disk it will take 1 move
    for two disks minimum number of moves is 3
    ...
    n - 1 disks = p
    2p + 1 = minimum number of moves for n disks
    
    number of disks         minimum number of moves
    1                       1
    2                       3
    3                       (2 * 3) + 1 = 7
    4                       (2 * 7) + 1 = 15
    5                       (2 * 15) + 1 = 31
    6                       (2 * 31) + 1 = 63
    7                       (2 * 63) + 1 = 127
    8                       (2 * 127) + 1 = 255
    9                       (2 * 255) + 1 = 511
    n - 1                   p
    n                       2p + 1
"""

# This function will return the minimum number of moves it will take to solve TOH with n disks
def towers_of_hanoi_moves(disks):
    if disks <= 0:
        print('Number of disks must be greater than 0')
        return
    num_of_moves = 0
    for i in range(0, disks):
        num_of_moves = (2 * num_of_moves) + 1
        # Uncomment below to see the number of moves for each disk
        # print(num_of_moves)
    return num_of_moves


# print(towers_of_hanoi_moves(9))
num_of_moves = int(input("Enter the number of disks: "))
print(towers_of_hanoi_moves(num_of_moves))
