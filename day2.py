def first_star():
    red_cubes = 12
    green_cubes = 13
    blue_cubes = 14
    game_ids_sum = 0
    with open("aoc_day2_input.txt", "r") as games_fh:
        for game_line in games_fh:
            possible_game = True
            game = game_line.strip()
            # print(game)
            game_id, revealed_cubes = game.split(": ")
            revealed_cubes_list = revealed_cubes.split("; ")
            # print(revealed_cubes_list)
            for reveal in revealed_cubes_list:
                # print(reveal)
                for colors in reveal.split(", "):
                    cube_count, cube_color = colors.split(" ")
                    if cube_color == "red" and int(cube_count) > 12:
                        possible_game = False
                        break
                    if cube_color == "green" and int(cube_count) > 13:
                        possible_game = False
                        break
                    if cube_color == "blue" and int(cube_count) > 14:
                        possible_game = False
                        break

            if possible_game:
                # print(game_id.split(" ")[1])
                game_ids_sum += int(game_id.split(" ")[1])

        print(game_ids_sum)


def second_star():
    sum_of_game_powers = 0
    with open("aoc_day2_input.txt", "r") as games_fh:
        for game_line in games_fh:
            red_cubes_min = 0
            green_cubes_min = 0
            blue_cubes_min = 0

            game = game_line.strip()
            # print(game)
            game_id, revealed_cubes = game.split(": ")
            revealed_cubes_list = revealed_cubes.split("; ")
            # print(revealed_cubes_list)
            for reveal in revealed_cubes_list:
                # print(reveal)
                for colors in reveal.split(", "):
                    cube_count_str, cube_color = colors.split(" ")
                    cube_count = int(cube_count_str)
                    if cube_color == "red" and cube_count > red_cubes_min:
                        red_cubes_min = cube_count
                    if cube_color == "green" and cube_count > green_cubes_min:
                        green_cubes_min = cube_count
                    if cube_color == "blue" and cube_count > blue_cubes_min:
                        blue_cubes_min = cube_count

            game_power = red_cubes_min * green_cubes_min * blue_cubes_min
            sum_of_game_powers += game_power

        print(sum_of_game_powers)


first_star()
second_star()
