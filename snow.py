import random

def add_top_snow(cells, chance=0.25):
    for i in range(cols):
        if random.random() < chance:
            cells[i] = '*'
    
def gravity(cells):
    for i in range((rows-1)*cols-1, -1, -1):
        if cells[i] == '*' and cells[i+cols] == ' ':
            cells[i], cells[i+cols] = cells[i+cols], cells[i] # swap 
             
def print_cells(cells):
    for r in range(rows):
        r1 = r + 1
        print( ''.join(cells[r*cols:r1*cols]))
    print('='*cols)

def is_full(cells):
    d = [cells[i]=='*' for i in range(rows * cols)]
    return all(d)

rows = 8
cols = 12
cells = [' '] * rows * cols
while not is_full(cells):
    gravity(cells)
    add_top_snow(cells)
    print_cells(cells)
print('all full of snow')
