import copy
import random

# # ---------------Input File & board dimension----------------/
input_txt = open("input15.txt", "r")
board_dimension = int(input_txt.readline())
board_area = [[0 for i in range(board_dimension)] for j in range(board_dimension)]

for i in range(0, board_dimension):
    row = input_txt.readline()
    for j in range(0, board_dimension):
        board_area[i][j] = int(row[j])

input_txt.close()


# def get_converage_array(x, y, board_area):
# 	## Set Dummy Value to identify index later
# 	board_area = copy.deepcopy(board_area)
# 	board_area[x][y] = 100
# 	matrix_dim = len(board_area)
# 	row_limit = [x - 3, x + 3 + 1]
# 	col_limit = [y - 3, y + 3 + 1]
# 	if col_limit[0] < 0:
# 		col_limit[0] = 0
# 	if col_limit[1] > matrix_dim:
# 		col_limit[1] = matrix_dim

# 	if row_limit[0] < 0:
# 		row_limit[0] = 0
# 	if row_limit[1] > matrix_dim:
# 		row_limit[1] = matrix_dim
# 	subset = [l[col_limit[0]:col_limit[1]] for l in board_area[row_limit[0]:row_limit[1]]]
# 	return subset

# def get_new_x_and_y(coverage_array):
# 	new_x, new_y = None, None

# 	## Can be optimized
# 	for i in range(len(coverage_array)):
# 		for j in range(len(coverage_array[0])):
# 			if coverage_array[i][j] == 100:
# 				new_x, new_y = i, j
# 				break
# 	return new_x, new_y

# def get_transformed_array(new_x, new_y, coverage_array):
# 	valid_coverage_array = copy.deepcopy(coverage_array)
# 	## Setting value 9 to count later
# 	for i in range(len(valid_coverage_array)):
# 		for j in range(len(valid_coverage_array[0])):
# 			if i == new_x or j == new_y or (abs(new_x - i) == abs(new_y - j)):
# 				if coverage_array[i][j] == 0:
# 					valid_coverage_array[i][j] = 9
# 	return valid_coverage_array


def get_total_cells_covered_at_point_and_covered_coordinates(x, y, inp_board):
    block_row_left = False
    block_row_right = False
    block_col_up = False
    block_col_down = False
    block_diag_lr_down = False
    block_diag_lr_up = False
    block_diag_rl_down = False
    block_diag_rl_up = False
    convered_coordinates = []

    def check_condition(x, y, board_area):
        n_row = len(board_area)
        n_col = len(board_area[0])
        n_row_index = n_row - 1
        n_col_index = n_col - 1
        if x > n_row_index or y > n_col_index or x < 0 or y < 0:
            return 0
        if board_area[x][y] != 3:
            return 1
        return 0

    i = 1
    valid_coverage_cell_count = 1
    convered_coordinates.append([x, y])
    while (i <= 3):
        # Row Left
        if not block_row_left:
            if check_condition(x, y + i, inp_board):
                convered_coordinates.append([x, y + i])
                valid_coverage_cell_count += 1
            else:
                block_row_left = True
        # Row Right
        if not block_row_right:
            if check_condition(x, y - i, inp_board):
                convered_coordinates.append([x, y - i])
                valid_coverage_cell_count += 1
            else:
                block_row_right = True
        # Col Up
        if not block_col_up:
            if check_condition(x - i, y, inp_board):
                convered_coordinates.append([x - i, y])
                valid_coverage_cell_count += 1
            else:
                block_col_up = True
        # Col Down
        if not block_col_down:
            if check_condition(x + i, y, inp_board):
                convered_coordinates.append([x + i, y])
                valid_coverage_cell_count += 1
            else:
                block_col_down = True
        # Diagnol L->R Down
        if not block_diag_lr_down:
            if check_condition(x + i, y + i, inp_board):
                convered_coordinates.append([x + i, y + i])
                valid_coverage_cell_count += 1
            else:
                block_diag_lr_down = True
        # Diagnol L->R Up
        if not block_diag_lr_up:
            if check_condition(x - i, y - i, inp_board):
                convered_coordinates.append([x - i, y - i])
                valid_coverage_cell_count += 1
            else:
                block_diag_lr_up = True
        # Diagnol R->L Down
        if not block_diag_rl_down:
            if check_condition(x - i, y + i, inp_board):
                convered_coordinates.append([x - i, y + i])
                valid_coverage_cell_count += 1
            else:
                block_diag_rl_down = True
        # Diagnol R->L Up
        if not block_diag_rl_up:
            if check_condition(x + i, y - i, inp_board):
                convered_coordinates.append([x + i, y - i])
                valid_coverage_cell_count += 1
            else:
                block_diag_rl_up = True
        i += 1
    return convered_coordinates, valid_coverage_cell_count


def simulation_action(sim_board_input):
    max_value = -99
    max_value_x = None
    max_value_y = None
    max_convered_coordinates = None
    result_dict = {}
    for i in range(len(sim_board_input)):
        for j in range((len(sim_board_input))):
            if sim_board_input[i][j] != 0:
                continue
            # coverage_array = get_converage_array(i, j, sim_board_input)
            # new_x, new_y = get_new_x_and_y(coverage_array)
            # valid_coverage_array = get_transformed_array(new_x, new_y, coverage_array)
            convered_coordinates, coverage_value = get_total_cells_covered_at_point_and_covered_coordinates(i, j,
                                                                                                            sim_board_input)
            if coverage_value > max_value:
                max_value = coverage_value
                max_value_x, max_value_y = i, j
                max_convered_coordinates = convered_coordinates
    result_dict['max_value'] = max_value
    result_dict['max_value_x'] = max_value_x
    result_dict['max_value_y'] = max_value_y
    result_dict['max_convered_coordinates'] = max_convered_coordinates
    return result_dict


def calculate_score(my_board, opp_board):
    my_score = sum(x.count(10) for x in my_board)
    my_score += sum(x.count(1) for x in my_board)
    opp_score = sum(x.count(20) for x in opp_board)
    opp_score += sum(x.count(2) for x in opp_board)
    return my_score - opp_score


def simulate(i, j, board_input, print_logs=False):
    my_coverage = copy.deepcopy(board_input)
    opp_coverage = copy.deepcopy(board_input)
    board_sim_input = copy.deepcopy(board_input)
    board_sim_input[i][j] = 1
    my_coverage[i][j] = 1

    convered_coordinates, coverage_value = get_total_cells_covered_at_point_and_covered_coordinates(i, j,
                                                                                                    board_sim_input)
    for _pos in convered_coordinates:
        my_coverage[_pos[0]][_pos[1]] = 10
        board_sim_input[_pos[0]][_pos[1]] = 10
    if print_logs:
        print('I Selected : ({}, {})'.format(i, j))
    # print('({}, {}) Simulation Base Score: {}'.format(i, j, calculate_score(my_coverage, opp_coverage)))
    # n_sim = sum(x.count(0) for x in board_sim_input)
    counter = 1
    while (sum(x.count(0) for x in board_sim_input) != 0):
        res_dict = simulation_action(board_sim_input)
        if counter % 2 == 0:
            for _pos in res_dict['max_convered_coordinates']:
                my_coverage[_pos[0]][_pos[1]] = 10
                if board_sim_input[_pos[0]][_pos[1]] != 0:
                    board_sim_input[_pos[0]][_pos[1]] = 30
                else:
                    board_sim_input[_pos[0]][_pos[1]] = 10
                board_sim_input[res_dict['max_value_x']][res_dict['max_value_y']] = 1
            if print_logs:
                print('I Selected : ({}, {})'.format(res_dict['max_value_x'], res_dict['max_value_y']))
        else:
            for _pos in res_dict['max_convered_coordinates']:
                opp_coverage[_pos[0]][_pos[1]] = 20
                if board_sim_input[_pos[0]][_pos[1]] != 0:
                    board_sim_input[_pos[0]][_pos[1]] = 30
                else:
                    board_sim_input[_pos[0]][_pos[1]] = 20
                board_sim_input[res_dict['max_value_x']][res_dict['max_value_y']] = 2
            if print_logs:
                print('Opp Selected : ({}, {})'.format(res_dict['max_value_x'], res_dict['max_value_y']))
        if print_logs:
            pass
            # print(np.matrix(my_coverage))
            # print(np.matrix(opp_coverage))
            print(np.matrix(board_sim_input))
            print('({}, {}) Simulation number: {} Score: {}'.format(i, j, counter,
                                                                    calculate_score(my_coverage, opp_coverage)))
        counter += 1
    if print_logs:
        print(np.matrix(board_sim_input))
        print('({}, {}) Simlutaion, Final Score: {}'.format(i, j, calculate_score(my_coverage, opp_coverage)))
    return calculate_score(my_coverage, opp_coverage)


def main(sim_board_input, print_logs=False):
    final_res_dict = {}
    max_value = -99
    max_value_x = None
    max_value_y = None
    sim_board_input_copy = copy.deepcopy(sim_board_input)
    for i in range(len(sim_board_input)):
        for j in range((len(sim_board_input))):
            if sim_board_input_copy[i][j] == 1:
                convered_coordinates, coverage_value = get_total_cells_covered_at_point_and_covered_coordinates(i, j,
                                                                                                                sim_board_input_copy)
                for _pos in convered_coordinates:
                    sim_board_input[_pos[0]][_pos[1]] = 10

            if sim_board_input_copy[i][j] == 2:
                convered_coordinates, coverage_value = get_total_cells_covered_at_point_and_covered_coordinates(i, j,
                                                                                                                sim_board_input_copy)
                for _pos in convered_coordinates:
                    if sim_board_input[_pos[0]][_pos[1]] == 10:
                        sim_board_input[_pos[0]][_pos[1]] = 30
                    else:
                        sim_board_input[_pos[0]][_pos[1]] = 20

    for i in range(len(sim_board_input)):
        for j in range((len(sim_board_input))):
            if sim_board_input[i][j] != 0:
                continue
            coverage_score = simulate(i, j, sim_board_input, print_logs=False)
            if coverage_score > max_value:
                max_value = coverage_score
                max_value_x, max_value_y = i, j

    if print_logs:
        print("Best Location Coordinated (X, Y) = ({}, {}) and Final Score = {}".format(max_value_x, max_value_y,
                                                                                        max_value))
        print("*" * 100)
        print('Simulation: ')
        print("*" * 100)
        print('Input Matrix: ')
        print(np.matrix(sim_board_input))
        res_sim = simulate(max_value_x, max_value_y, sim_board_input, print_logs)
    final_res_dict['max_value_x'] = max_value_x
    final_res_dict['max_value_y'] = max_value_y
    final_res_dict['final_score'] = max_value

    abc = int(max_value_x)
    xyz = int(max_value_y)

    # Output Required Coordinates
    with open("output.txt", "w") as f2:
        f2.write("%d %d" % (abc, xyz))

    #print("Move coordinates: (%d, %d)" %(abc, xyz))

main(board_area)
# main(board_area, print_logs=True)