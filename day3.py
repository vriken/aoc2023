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
