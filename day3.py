#part 1
def sum_part_numbers(schematic):
    height, width = len(schematic), len(schematic[0])
    sum_of_parts = 0

    def is_adjacent_to_symbol(i, j, num_length):
        directions = [ (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1) ]

        for k in range(num_length):
            for di, dj in directions:
                new_i, new_j = i + di, j + dj + k
                if 0 <= new_i < height and 0 <= new_j < width and schematic[new_i][new_j] not in '.0123456789\n':
                    return True
        return False

    for i in range(height):
        j = 0
        while j < width:
            if schematic[i][j].isdigit():
                number = schematic[i][j]
                num_length = 1
                while j + num_length < width and schematic[i][j + num_length].isdigit():
                    number += schematic[i][j + num_length]
                    num_length += 1

                if is_adjacent_to_symbol(i, j, num_length):
                    sum_of_parts += int(number)

                #Move past this number
                j += num_length
            else:
                j += 1

    return sum_of_parts

sum_part_numbers(schematic)

#525119

#part 2

with open(file_path, 'r') as file:
    input_grid = [line.strip() for line in file.readlines()]

def calculate_adjacent_values(input_grid):
    rows = len(input_grid)
    columns = len(input_grid[0])
    total_product = 0
    adjacent_values = [[] for _ in range(rows * columns)]
    
    for row_index in range(rows):
        col_index = 0
        while col_index < columns:
            if not input_grid[row_index][col_index].isdigit():
                col_index += 1
                continue

            end_index = col_index
            number = 0
            while end_index < columns and input_grid[row_index][end_index].isdigit():
                number = 10 * number + (ord(input_grid[row_index][end_index]) - ord('0'))
                end_index += 1

            for adjacent_index in range(max(0, col_index - 1), min(columns, end_index + 1)):
                if row_index - 1 >= 0 and input_grid[row_index - 1][adjacent_index] == '*':
                    adjacent_values[(row_index - 1) * columns + adjacent_index].append(number)
                if input_grid[row_index][adjacent_index] == '*':
                    adjacent_values[row_index * columns + adjacent_index].append(number)
                if row_index + 1 < rows and input_grid[row_index + 1][adjacent_index] == '*':
                    adjacent_values[(row_index + 1) * columns + adjacent_index].append(number)
            
            col_index = end_index

    for adj_values in adjacent_values:
        if len(adj_values) == 2:
            total_product += adj_values[0] * adj_values[1]

    return total_product

result = calculate_adjacent_values(input_grid)
print(result)
