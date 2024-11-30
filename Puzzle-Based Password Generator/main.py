# Author: Cass Burleson
# Creation Date: 2024-09-16
# Program: puzzle-based password generator (File I/O, matrix manipulation, transformation logic)
# Programed two ways of completing this project. First is through row and column manipulation, the second 
# is through matrix index substitutions. (beginning at rotate_outer_layer)

import csv

#---IO FUNCTIONS---
def read_file(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file, delimiter=',')
        puzzle = [list(map(int, row)) for row in reader]
    return puzzle

def write_file(filename, puzzle):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerows(puzzle)

#---BASE FUNCTIONS---
# pad rows to length of 9
def add_padding(puzzle, length=9):
    padded_puzzle = []
    for row in puzzle:
        row_length = len(row)
        if row_length < length:
            padding_needed = length - row_length
            left_padding = padding_needed // 2
            right_padding = padding_needed - left_padding
           
            new_row = [0] * left_padding + row + [0] * right_padding
        else:
            new_row = row
        padded_puzzle.append(new_row)
    
    return padded_puzzle

# get middle indices
def get_middle_index(puzzle):
    num_rows = len(puzzle)
    num_cols = len(puzzle[0]) if num_rows > 0 else 0
    middle_row_index = num_rows // 2
    middle_col_index = num_cols // 2
    return middle_row_index, middle_col_index

# rotate quadrant 90 degrees clockwise
def rotate_90_clockwise(quadrant):
    return list(zip(*quadrant[::-1]))

# rotate quadrant 90 degrees counterclockwise
def rotate_90_counterclockwise(quadrant):
    return list(zip(*quadrant))

# extract first and last non-zero elements from matrix
def extract_outer_elements(puzzle):
    middle_row_index, middle_col_index = get_middle_index(puzzle)

    top_left_first_nonzero = []
    bottom_left_first_nonzero = []
    top_right_last_nonzero = []
    bottom_right_last_nonzero = []

    # top-left
    for row in puzzle[:middle_row_index]:
        for col in range(middle_col_index):
            if row[col] != 0:
                top_left_first_nonzero.append(row[col])
                break
    
    # bottom-left
    for row in puzzle[middle_row_index + 1:]:
        for col in range(middle_col_index):
            if row[col] != 0:
                bottom_left_first_nonzero.append(row[col])
                break

    # top-right
    for row in puzzle[:middle_row_index]:
        for col in reversed(range(middle_col_index + 1, len(row))):
            if row[col] != 0:
                top_right_last_nonzero.append(row[col])
                break

    # bottom-right
    for row in puzzle[middle_row_index + 1:]:
        for col in reversed(range(middle_col_index + 1, len(row))):
            if row[col] != 0:
                bottom_right_last_nonzero.append(row[col])
                break
    #debug
    # print("TOP LEFT: ",top_left_first_nonzero)
    # print("BOTTOM LEFT: ",bottom_left_first_nonzero)
    # print("TOP RIGHT: ",top_right_last_nonzero)
    # print("BOTTOM RIGHT: ",bottom_right_last_nonzero)
    
    return top_left_first_nonzero, bottom_left_first_nonzero, top_right_last_nonzero, bottom_right_last_nonzero

# rotate first non-zero integer clockwise
def rotate_first_nonzero(quadrant):
    rotated_rows = []
    for row in quadrant:
        # find first non-zero element
        first_nonzero_index = next((i for i, x in enumerate(row) if x != 0), None)
        if first_nonzero_index is not None:
            # move element to end of row
            new_row = row[first_nonzero_index + 1:] + [row[first_nonzero_index]] + row[:first_nonzero_index]
        else:
            new_row = row
        rotated_rows.append(new_row)
    return rotated_rows

# rotate last non-zero integer clockwise
def rotate_last_nonzero(quadrant):
    rotated_rows = []
    for row in quadrant:
        # find first non-zero element
        last_nonzero_index = next((i for i, x in reversed(list(enumerate(row))) if x != 0), None)
        if last_nonzero_index is not None:
            # move last element to the start of the row
            new_row = [row[last_nonzero_index]] + [row[:last_nonzero_index]] + row[last_nonzero_index + 1:]
        else:
            new_row = row
        rotated_rows.append(new_row)
    return rotated_rows

# comma delimiter for agentID
def comma_delimited(last_four, delimiter=","):
    nmbr_str = last_four.split(delimiter)
    commas = ','.join(nmbr_str)
    return commas

#---TRANSFORMING FUNCTIONS---
# 0
def reverse_top(puzzle):
    
    middle_row_index, middle_col_index = get_middle_index(puzzle)
    
    #establish which rows are transformed and which are static
    transforming_rows = puzzle[:middle_row_index]
    static_rows = puzzle[middle_row_index:]
    
    # reverse rows above middle index
    transformed_rows = []
    for row in transforming_rows:
            # reverse data excluding middle column index
            transformed_row = row[::-1]
            transformed_rows.append(transformed_row)
            
    # combine reversed and remaining rows
    new_puzzle = transformed_rows + static_rows

    return new_puzzle

#1 
def reverse_bottom(puzzle):
    middle_row_index, middle_col_index = get_middle_index(puzzle)

    #establish which rows are transformed and which are static
    transforming_rows = puzzle[middle_row_index + 1:]
    static_rows = puzzle[:middle_row_index + 1]
    
    # reverse rows below middle index
    transformed_rows = []
    for row in transforming_rows:
            # reverse data excluding middle column index
            transformed_row = row[::-1]
            transformed_rows.append(transformed_row)
    
    # concat reversed and remaining rows
    new_puzzle = static_rows + transformed_rows

    return new_puzzle

#2
def reverse_left(puzzle):
    middle_row_index, middle_col_index = get_middle_index(puzzle)
    
    # establish columns to the left
    left_columns = []
    for col in range(middle_col_index):
        column = [row[col] for row in puzzle]
        # reverse column vertically
        left_columns.append(column[::-1])

    # create new puzzle with reversed columns
    new_puzzle = []
    for row in range(len(puzzle)):
        new_row = []
        #add reversed columns
        for col in range(middle_col_index):
            new_row.append(left_columns[col][row])
        #add middle column
        new_row.append(puzzle[row][middle_col_index])
        #add right column
        new_row.extend(puzzle[row][middle_col_index + 1:])
        new_puzzle.append(new_row)
    
    return new_puzzle

#3 
def reverse_right(puzzle):
    middle_row_index, middle_col_index = get_middle_index(puzzle)
    
    # establish columns to the right of the middle column
    right_columns = []
    for col in range(middle_col_index + 1, len(puzzle[0])):
        column = [row[col] for row in puzzle]
        #reverse column vertically
        right_columns.append(column[::-1])

    # create new puzzle
    new_puzzle = []
    for row in range(len(puzzle)):
        new_row = []
        # add left columns
        new_row.extend(puzzle[row][:middle_col_index + 1])
        # add transformed right columns
        for col in range(len(puzzle[0]) - (middle_col_index + 1)):
            new_row.append(right_columns[col][row])
        
        new_puzzle.append(new_row)
    
    return new_puzzle

#4 
def mirror_bottom_left_top_right(puzzle):
    middle_row_index, middle_col_index = get_middle_index(puzzle)

    # establish bottom-left quadrant
    bottom_left_quadrant = []
    for row in range(middle_row_index + 1, len(puzzle)):
        bottom_left_quadrant.append(puzzle[row][:middle_col_index])

    # establish top-right quadrant
    top_right_quadrant = []
    for row in range(middle_row_index):
        top_right_quadrant.append(puzzle[row][middle_col_index + 1:])
    
    # rotate bottom-left quadrant 90 degrees clockwise
    rotated_bottom_left_quadrant = rotate_90_clockwise(bottom_left_quadrant)
    # rotate top-left quadrant 90 degrees counterclockwise
    rotated_top_right_quadrant = rotate_90_counterclockwise(top_right_quadrant)
    
    # reverse the rows of the rotated quadrants
    reversed_bottom_left_quadrant = [list(reversed(row)) for row in rotated_bottom_left_quadrant]   
    #reversed_top_right_quadrant = [list(reversed(row)) for row in rotated_top_right_quadrant]

    # create new puzzle
    new_puzzle = [row[:] for row in puzzle]
    # Preversed bottom left to top right
    for i in range(len(reversed_bottom_left_quadrant)):
        if i < len(new_puzzle) and len(reversed_bottom_left_quadrant[i]) > 0:
            new_puzzle[i][middle_col_index + 1:] = reversed_bottom_left_quadrant[i]
    # reversed top right to bottom left
    for i in range(len(rotated_top_right_quadrant)):
        if i < len(new_puzzle):
            new_puzzle[middle_row_index + 1 + i][:middle_col_index] = rotated_top_right_quadrant[i]
    
    return new_puzzle

#5
def mirror_bottom_right_top_left(puzzle):
    middle_row_index, middle_col_index = get_middle_index(puzzle)

    # establish bottom-right quadrant
    bottom_right_quadrant = []
    for row in range(middle_row_index + 1, len(puzzle)):
        bottom_right_quadrant.append(puzzle[row][middle_col_index + 1:])

    # establish top-left quadrant
    top_left_quadrant = []
    for row in range(middle_row_index):
        top_left_quadrant.append(puzzle[row][:middle_col_index])
    
    # rotate bottom-right quadrant 90 degrees clockwise
    rotated_bottom_right_quadrant = rotate_90_clockwise(bottom_right_quadrant)
    # rotate top-left quadrant 90 degrees counterclockwise
    rotated_top_left_quadrant = rotate_90_counterclockwise(top_left_quadrant)
    
    # reverse the rows of the rotated quadrants
    reversed_bottom_right_quadrant = list(reversed(rotated_bottom_right_quadrant)) 
    reversed_top_left_quadrant = [list(reversed(row)) for row in reversed(rotated_top_left_quadrant)]

    # create new puzzle
    new_puzzle = [row[:] for row in puzzle]
    
    # eversed bottom right to top left
    for i in range(len(reversed_bottom_right_quadrant)):
        if i < middle_row_index:
            new_puzzle[i][:middle_col_index] = reversed_bottom_right_quadrant[i]
    # reversed top left to bottom right
    for i in range(len(reversed_top_left_quadrant)):
        if i + middle_row_index + 1 < len(new_puzzle):
            new_puzzle[middle_row_index + 1 + i][middle_col_index + 1:] = reversed_top_left_quadrant[i]
    
    return new_puzzle

#6
def rotate_outer_layer(puzzle):
    middle_row_index, middle_col_index = get_middle_index(puzzle)
    top_left_first_nonzero, bottom_left_first_nonzero, top_right_last_nonzero, bottom_right_last_nonzero = extract_outer_elements(puzzle)
    
    new_puzzle = [row[:] for row in puzzle]

    # top left to top right
    for i, row in enumerate(puzzle[:middle_row_index]):
        relevant_columns = row[:middle_col_index] + row[middle_col_index + 1:]
        last_nonzero_index = next((i for i, x in reversed(list(enumerate(relevant_columns))) if x != 0), None)
        if last_nonzero_index is not None:
            new_puzzle[i][last_nonzero_index if last_nonzero_index < middle_col_index else last_nonzero_index + 1] = top_left_first_nonzero[middle_row_index - 1 - i]

    # top right to bottom right
    for i, row in enumerate(puzzle[middle_row_index + 1:]):
        relevant_columns = row[middle_col_index + 1:]
        last_nonzero_index = next((i for i, x in reversed(list(enumerate(relevant_columns))) if x != 0), None)
        if last_nonzero_index is not None:
            new_puzzle[middle_row_index + 1 + i][middle_col_index + 1 + last_nonzero_index] = top_right_last_nonzero[i]

    ## BEGINING OF MATRIX INDEX SUBSTITUTIONS
    new_puzzle[5][1] = puzzle[7][5]

    new_puzzle[6][2] = puzzle[6][6]
    new_puzzle[7][3] = puzzle[5][7]

    new_puzzle[1][3] = puzzle[5][1]
    new_puzzle[2][2] = puzzle[6][2]
    new_puzzle[3][1] = puzzle[7][3]

    return new_puzzle

#7
def rotate_middle_layer(puzzle):
    new_puzzle = [row[:] for row in puzzle]

    new_puzzle[2][3] = puzzle[5][2]
    new_puzzle[3][2] = puzzle[6][3]
    new_puzzle[2][5] = puzzle[3][2]
    new_puzzle[3][6] = puzzle[2][3]
    new_puzzle[5][2] = puzzle[6][5]
    new_puzzle[6][3] = puzzle[5][6]
    new_puzzle[5][6] = puzzle[2][5]
    new_puzzle[6][5] = puzzle[3][6]
    
    return new_puzzle

#8 
def rotate_inner_layer(puzzle):
    new_puzzle = [row[:] for row in puzzle]

    new_puzzle[3][3] = puzzle[5][3]
    new_puzzle[3][5] = puzzle[3][3]
    new_puzzle[5][3] = puzzle[5][5]
    new_puzzle[5][5] = puzzle[3][5]

    return new_puzzle

#9
def inverted_layers(puzzle):
    new_puzzle = [row[:] for row in puzzle]

    new_puzzle[2][2] = puzzle[6][6]
    new_puzzle[3][3] = puzzle[5][5]
    new_puzzle[3][5] = puzzle[5][3]
    new_puzzle[2][6] = puzzle[6][2]
    new_puzzle[6][2] = puzzle[2][6]
    new_puzzle[5][3] = puzzle[3][5]
    new_puzzle[5][5] = puzzle[3][3]
    new_puzzle[6][6] = puzzle[2][2]

    return new_puzzle

#puzzle manipulation
def manipulate_puzzle(commas, puzzle, FILENAME):
    numbers = list(map(int, commas))
    
    digits = {
        0: reverse_top,
        1: reverse_bottom,
        2: reverse_left,
        3: reverse_right,
        4: mirror_bottom_left_top_right,
        5: mirror_bottom_right_top_left,
        6: rotate_outer_layer,
        7: rotate_middle_layer,
        8: rotate_inner_layer,
        9: inverted_layers
    }
    
    for i in numbers:
        if i in digits:
            puzzle = digits[i](puzzle)
            write_file(FILENAME, puzzle)
    return puzzle

# sum puzzle columns
def sum_columns(puzzle):
    columns = [1, 2, 3, 5, 6, 7]
    column_sums = [0] * len(columns)
        
    for row in puzzle:
        for i, col in enumerate(columns):
            column_sums[i] += row[col]
    column_sums_str = ''.join(map(str, column_sums))
    return column_sums_str
    
# collect numbers
def collect_numbers(puzzle):
    middle_row_index, middle_col_index = get_middle_index(puzzle)
    
    first_row = []
    
    for row_index in range(middle_col_index, -1, -1):
        row = puzzle[row_index]
        non_zero_count = 0
        for element in row:
            if element !=0:
                first_row.append(element) # [31, 70, 68, 30, 49]
                break
 
    second_row = [puzzle[1][4], puzzle[2][3], puzzle[3][2], puzzle[4][1]]
    third_row = [puzzle[5][1], puzzle[4][2], puzzle[3][3], puzzle[2][4], puzzle[1][5]]
    fourth_row = [puzzle[2][5], puzzle[3][4], puzzle[4][3], puzzle[5][2]]
    fifth_row = [puzzle[6][2], puzzle[5][3], puzzle[4][4], puzzle[3][5], puzzle[2][6]]
    sixth_row = [puzzle[3][6], puzzle[4][5], puzzle[5][4], puzzle[6][3]]
    seventh_row = [puzzle[7][3], puzzle[6][4], puzzle[5][5], puzzle[4][6], puzzle[3][7]]
    eighth_row = [puzzle[4][7], puzzle[5][6], puzzle[6][5], puzzle[7][4]]
    ninth_row = [puzzle[8][4], puzzle[7][5], puzzle[6][6], puzzle[5][7], puzzle[4][8]]
    
    lists = [first_row, second_row, third_row, fourth_row, fifth_row, sixth_row, seventh_row, eighth_row, ninth_row]
    concat_list = []
    for list in lists:
        concat_list.extend(list)
    return concat_list

#decode
def decode_list(concat_list):
    binary_list = []
    for i in range(len(concat_list) - 1):
        if concat_list[i] < concat_list[i + 1]:
            binary_list.append(1)
        elif concat_list[i] > concat_list[i + 1]:
            binary_list.append(0)
        elif concat_list[i] == concat_list[i + 1]:
            binary_list.append(0)
    return binary_list

# count binary
def count_binary(binary_list):
    count_0 = binary_list.count(0)
    count_1 = binary_list.count(1)
    return count_0, count_1

#---PROGRAM----
def main():
    FILENAME = 'puzzle.txt'
    original_puzzle = read_file(FILENAME)
    
    #ensure each row has exactly 9 elements
    original_puzzle = add_padding(original_puzzle, length=9)
    
    while True:
        #deep copy
        puzzle = [row[:] for row in original_puzzle]
        
        #debug
        # print("0: ", reverse_top(puzzle))
        # print("1: ", reverse_bottom(puzzle))
        # print("2: ", reverse_left(puzzle))
        # print("3: ", reverse_right(puzzle))
        # print("4: ", mirror_bottom_left_top_right(puzzle))
        # print("5: ", mirror_bottom_right_top_left(puzzle))
        # print("6: ", rotate_outer_layer(puzzle))
        # print("7: ", rotate_middle_layer(puzzle))
        # print("8: ", rotate_inner_layer(puzzle))
        #print("9: ", inverted_layers(puzzle))
        
        agentID = input("Enter the last 7 digits of your agentID (ex. 123456): ").strip()
    
        # get apartment password
        last_four = agentID[2:]
        commas = comma_delimited(last_four)
        
        #manipulation
        puzzle = manipulate_puzzle(commas, puzzle, FILENAME)
        column_sums_str = sum_columns(puzzle)
        print("The password for the apartment is ", column_sums_str)
        
        # get safe password
        calc = agentID[:2]
    
        concat_list = collect_numbers(puzzle)
        binary_list = decode_list(concat_list)
        count_0, count_1 = count_binary(binary_list)
        safe_pass = str(count_0) + calc + str(count_1)
        print("The password to the safe is :", safe_pass)
        
        repeat = input("Do you want to enter another agentID? (Y/N): ").strip().lower()
        
        if repeat != 'y':
            break
    
if __name__ == '__main__':
    main()
