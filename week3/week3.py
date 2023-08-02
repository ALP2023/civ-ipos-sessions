'''a_2d_list = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]  # presented as a 2D structure
print(a_2d_list[2][2])  # Output 9

# only prints each list
for elem in a_2d_list:
    print(elem)  # prints each list within the list in seperate lines

# prints each element within the list i.e. each number
for row in a_2d_list:
    for elem in row:
        # prints each number for each list in seperate lines
    #    print(elem)
        # prints each number for each list in one line
        print(elem, end=' ')'''

# list builder function

# basic coding
def make_2d(rows, cols, value=None):
    # create rows x columns 2d data structure
    b_2d_list = []
    for i in range(rows):
        row = []
        for j in range(cols):
 #           row.append((i+1)*(j+1)) # create 2d lids adds increments
            row.append(value) # create 2d lists with default value
        b_2d_list.append(row)
    return b_2d_list # list of lists of the required dimension

print(make_2d(1, 3, 55))

# using list comprehension
def make_2d_lscomp(rows, cols, value=None):
    # create rows x columns 2d data structure
    list_2d_lscomp = []

    return [[value for _ in range(cols)] for _ in range(rows)]

print(make_2d(1, 3, 55))


