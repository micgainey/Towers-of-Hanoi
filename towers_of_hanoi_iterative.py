# Iterative towers of hanoi
# taken from https://www.geeksforgeeks.org/iterative-tower-of-hanoi/
# by divyeshrabadiya07
# from towers_of_hanoi_count import towers_of_hanoi_moves
import sys

class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.top = -1
        self.array = [0]*capacity

def create_stack(capacity):
    stack = Stack(capacity)
    return stack

def is_full(stack):
    return (stack.top == (stack.capacity -1))

def is_empty(stack):
    return (stack.top == -1)

def push(stack, item):
    if (is_full(stack)):
        return
    stack.top += 1
    stack.array[stack.top] = item

def pop(stack):
    if is_empty(stack):
        return -sys.maxsize
    top = stack.top
    stack.top -= 1
    return stack.array[top]

def move_disk(from_peg, to_peg, disk):
    print("Move disk", disk, "from", from_peg, "to", to_peg)

def legal_move_between_poles(src, dest, s, d):
    pole_1_top_disk = pop(src)
    pole_2_top_disk = pop(dest)

    if pole_1_top_disk == -sys.maxsize:
        push(src, pole_2_top_disk)
        move_disk(d, s, pole_2_top_disk)

    elif pole_2_top_disk == -sys.maxsize:
        push(dest, pole_1_top_disk)
        move_disk(s, d, pole_1_top_disk)
    
    elif pole_1_top_disk > pole_2_top_disk:
        push(src, pole_1_top_disk)
        push(src, pole_2_top_disk)
        move_disk(d, s, pole_2_top_disk)
    
    else:
        push(dest, pole_2_top_disk)
        push(dest, pole_1_top_disk)
        move_disk(s, d, pole_1_top_disk)

def towers_of_hanoi_iterative(num_of_disks, src, aux, dest):
    s = 'A'
    d = 'B'
    a = 'C'

    if num_of_disks % 2 == 0:
        temp = d
        d = a
        a = temp

    total_number_of_moves = (2 ** num_of_disks) - 1

    for i in range(num_of_disks, 0, -1):
        push(src, i)

    for i in range(1, total_number_of_moves + 1):
        if i % 3 == 1:
            legal_move_between_poles(src, dest, s, d)
        
        elif i % 3 == 2:
            legal_move_between_poles(src, aux, s, a)
        
        elif i % 3 == 0:
            legal_move_between_poles(aux, dest, a, d)

'''
CHANGE THESE OUTPUTS FOR DIFFERENT RESULTS
'''

# This is the number of disks you want to test
num_of_disks = (int(input("Enter the number of disks: ")))

# Create three stacks of size 'num_of_disks'
src = create_stack(num_of_disks)
dest = create_stack(num_of_disks)
aux = create_stack(num_of_disks)

# Call function
towers_of_hanoi_iterative(num_of_disks, src, aux, dest)

# print number of moves at the end
num_of_moves = 2 ** num_of_disks - 1
# num_of_moves = towers_of_hanoi_moves(num_of_disks)
print('It took', num_of_moves, 'moves for', num_of_disks, 'disks')
