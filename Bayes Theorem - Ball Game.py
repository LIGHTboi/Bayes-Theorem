from random import randint, choice
from csv import writer
import time

start = time.time()

# SETTING NUMBER OF TRIALS TO BE CONDUCTED FOR EACH GIVEN NUMBER OF HINTS
trials = 10**6

# TO GENERATE RANDOM HINT BALLS
def hb_throw():
    return randint(1,100)

# TO CALCULATE RELATIVE POSITION OF ORIGINAL BALL AND HINT BALL
def relative_pos(hb):

    if og % 10 == 0:
        sign = -1
        temp_og, temp_hb = hb, og
    else:
        sign = 1
        temp_og, temp_hb = og, hb
    
    if (temp_hb % 10 == 0 and temp_og % 10 == 0) or (temp_hb % 10 != 0 and temp_og % 10 != 0):  # N-S Deviation
        y = (temp_hb // 10) - (temp_og // 10)
    else:
        y = (temp_hb // 10) - (temp_og // 10) - 1
    
    if (temp_hb % 10 == 0 and temp_og % 10 == 0) or (temp_hb % 10 != 0 and temp_og % 10 != 0):  # E-W Deivation
        x = temp_hb - (temp_og + (10 * y))
    else:
        x = temp_hb - (temp_og + (10 * (y)))
    
    return (x*sign, y*sign)


def hint(relative_coords):
    x, y = relative_coords

    x_dirn = 'W' if x < 0 else 'E'              #Determining Direction in X-axis
    y_dirn = 'N' if y < 0 else 'S'              #Determining Direction in Y-axis

    print(f'Hint: {abs(y)}-{y_dirn} and {abs(x)}-{x_dirn}')

# TO CALCULATE BEST HINTS OUT OF ALL GIVEN HINTS
def max_hints(relative_coords):
    x, y = relative_coords
    if y < 0:
        global N
        N = max(abs(y), N)
    else:
        global S
        S = max(y, S)

    if x < 0:
        global W
        W = max(abs(x), W)
    else:
        global E
        E = max(x, E)

# TO CREATE BOARD USING MAX_HINTS
def create_board():
    return ( tuple( ( tuple( (num + 10*row) for num in range(1+W, 11-E) ) for row in range(N, 10 - S)) ) )

for hints in range(1, 101):

    correct_guesses = 0

    for i in range(trials):

        # TO GENERATE THE ORIGINAL BALL
        og = randint(1,100)
        # print(f'Original Ball landed at {og}')

        # CURRENT HINTS FOR EACH DIRECTION
        N, S, E, W = 0, 0, 0, 0

        for j in range(hints):
            relative_position = relative_pos(hb_throw())
            # hint(relative_position)
            max_hints(relative_position)

        board = create_board()
        # print(board)
        guess = choice(choice(board))
        # print(f'Guess: {guess}')
        if guess == og:
            correct_guesses += 1

    pr_correct_guesses = correct_guesses/trials

    print(f'''Total Trials: {trials}
    Number of hints given per trial: {hints}
    Correct Guesses: {correct_guesses}
    Wrong Guesses: {trials - correct_guesses}
    Probability of guessing the correct position given {hints} hints: {pr_correct_guesses}
    ''')
    f = open('ballGame.csv', 'a', newline = '')
    cw = writer(f)
    cw.writerow([hints, pr_correct_guesses])
    f.close()

print(f"Time taken: {time.time()- start}")