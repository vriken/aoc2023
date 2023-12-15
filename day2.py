#part 1
def is_game_possible(game_record, red_limit, green_limit, blue_limit):
    subsets = game_record.strip().split('; ')
    for subset in subsets:
        red_count = sum(int(num.split()[0]) for num in subset.split(',') if 'red' in num)
        green_count = sum(int(num.split()[0]) for num in subset.split(',') if 'green' in num)
        blue_count = sum(int(num.split()[0]) for num in subset.split(',') if 'blue' in num)
        
        if red_count > red_limit or green_count > green_limit or blue_count > blue_limit:
            return False
    return True

sum_of_possible_game_ids = 0
for game in game_data:
    game_id, game_record = game.split(': ')
    game_id = int(game_id.split()[1])
    
    if is_game_possible(game_record, red_limit, green_limit, blue_limit):
        sum_of_possible_game_ids += game_id

sum_of_possible_game_ids
#2632

#part 2
def minimum_cubes_per_game(game_record):
    max_red, max_green, max_blue = 0, 0, 0
    subsets = game_record.strip().split('; ')
    for subset in subsets:
        red_count = sum(int(num.split()[0]) for num in subset.split(',') if 'red' in num)
        green_count = sum(int(num.split()[0]) for num in subset.split(',') if 'green' in num)
        blue_count = sum(int(num.split()[0]) for num in subset.split(',') if 'blue' in num)
        
        max_red = max(max_red, red_count)
        max_green = max(max_green, green_count)
        max_blue = max(max_blue, blue_count)

    return max_red, max_green, max_blue

total_power = 0
for game in game_data:
    _, game_record = game.split(': ')
    min_red, min_green, min_blue = minimum_cubes_per_game(game_record)
    game_power = min_red * min_green * min_blue
    total_power += game_power

total_power

#69629