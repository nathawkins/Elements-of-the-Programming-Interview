'''
Write a function that takes an array of n integers, where A[i] is the maximum
number of steps you can take from that position, and return whether or not it is
possible to make it to the end starting at A[0] and moving forward.
'''

def check_board(A, dialogue = False):
    ##The index position that, if reached, signifies the end of the game and a
    ##victory
    furthest_index_reached, index_to_win = 0, len(A) - 1

    ##Wherever we are on the board is kept track of by i
    i = 0

    ##keep track of the route through the board
    route = []

    ##We look at each position on the board. The furthest we can get from that position
    ##is equal to i + A[i] (ex: starting at the beginning, i=0, the furthest we
    ##can get is i = 3 (0 + 3)). So, in each iteration, look at the position and the
    ##value there. If i + A[i] is larger that what was found previously, keep it
    ##, which is synonymous with davancing forward in the board. If it's not, continue
    ##through the board. The loop terminates if i > furthest_index_reached because
    ##that means there is no way to get past that point, or if furthest_index_reached
    ##is greater than the index_to_win because that means we made it. Returns true or false.
    while i <= furthest_index_reached and furthest_index_reached < index_to_win:
        next_move = max(furthest_index_reached, i + A[i])

        route.append(i) if next_move == (i+A[i]) else route.append("X")

        furthest_index_reached = next_move
        i += 1

    ##Clean-up the route array
    route = [x for x in route if x != "X"]

    if dialogue:
        if furthest_index_reached >= index_to_win:
            print(A)
            print("Most optimal path through the board:\n")
            for k in range(len(route)-1):
                print("Go from {} to {} ({} steps)\n".format(route[k], route[k+1], route[k+1] - route[k]))
            print("Go from {} to the end of the board ({} steps)\n".format(route[-1], len(A)-1-route[-1]))
        else:
            print(A)
            print("No solution could be found through the board.\n")


    return furthest_index_reached >= index_to_win

# print(check_board([3,3,1,0,2,0,1]))
# print(check_board([3,3,1,0,2,0,1], dialogue = True))
# print(check_board([3,2,0,0,2,0,1], dialogue = True))
check_board([3,3,1,0,2,0,1], dialogue = True)
check_board([3,2,0,0,2,0,1], dialogue = True)
check_board([3,2,0, 2, -1, 3, 0,2,0,1], dialogue = True)

import random as r
test = [r.randint(0,3) for x in range(50)]
check_board(test, dialogue = True)
