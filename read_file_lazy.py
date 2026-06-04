N = 5

def write_file(filename, N):
    with open(filename, 'w') as f:
        for i in range(1, N):
            f.write(f'line_{i}\n')
            
def read_file(filename):
    with open(filename) as file:
        for line in file:
            yield line.strip()  # using lazy evaluation

# create test file          
write_file('test.txt', N)

# read whole file, BAD when file is too big for memory (N = 999999999999...)
whole_file = open('test.txt').read().splitlines()
print(whole_file)

# read file line by line, GOOD
for i in read_file('test.txt'):
    print(i)
