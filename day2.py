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