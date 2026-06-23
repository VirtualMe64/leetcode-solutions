# Problem: https://leetcode.com/problems/sudoku-solver
# Runtime: 2139 ms

ALL_OPTIONS = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        horizontals = [set() for i in range(9)]
        verticals = [set() for i in range(9)]
        squares = [set() for i in range(9)]

        def get_square(row, col):
            return 3 * (row // 3) + col // 3

        fill_list = []

        for row in range(9):
            for col in range(9):
                v = board[row][col]
                if v != '.':
                    horizontals[row].add(v)
                    verticals[col].add(v)
                    squares[get_square(row, col)].add(v)
                else:
                    fill_list.append((row, col))
        
        def options(row, col):
            hori_used = horizontals[row]
            vert_used = verticals[col]
            sqar_used = squares[get_square(row, col)]
            
            all_used = hori_used.union(vert_used).union(sqar_used)
            return [x for x in ALL_OPTIONS if x not in all_used]

        fill_list.sort(key = lambda x : len(options(*x)))
        action_log = [0 for i in range(81)]
        action_ptr = 0

        while 0 <= action_ptr < len(fill_list):
            curr_box = fill_list[action_ptr]
            curr_num = board[curr_box[0]][curr_box[1]]
        
            # clean up if back tracking
            if curr_num != '.':
                board[curr_box[0]][curr_box[1]] = '.'
                horizontals[curr_box[0]].remove(curr_num)
                verticals[curr_box[1]].remove(curr_num)
                squares[get_square(curr_box[0], curr_box[1])].remove(curr_num)

            curr_action = action_log[action_ptr]
            curr_options = options(*curr_box)

            if curr_action + 1 > len(curr_options): # we need to backtrack!
                action_log[action_ptr] = 0
                action_ptr -= 1
            else: # try it
                new_number = curr_options[curr_action]

                horizontals[curr_box[0]].add(new_number)
                verticals[curr_box[1]].add(new_number)
                squares[get_square(curr_box[0], curr_box[1])].add(new_number)

                board[curr_box[0]][curr_box[1]] = new_number                
                action_log[action_ptr] += 1
                action_ptr += 1