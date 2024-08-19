# Player 1 operates using a, b, c, d, e, f, g, h, i
# Player 2 operates using A, B, C, D, E, F, G, H, I
# Game ends whenever one of the boards if completely filled
# Players take turn each and can decide to either place a new number on one of the spots
# Or replace one of the numbers on one of the spots
# Whoever ends up with the highest ammount of numbers wins
# This tiny project is inspired by knucklebones from the game 'Cult of the Lamb'
# This project WILL be updated and it's the very first version of this project
# ----------------------------------------------------------------------------------------
import random

# Initialization of the game
bot_choice_position = 0
bot_choice_dice = 0
a = b = c = d = e = f = g = h = i = 0
A = B = C = D = E = F = G = H = I = 0
player_turn = random.randint(1, 2)
if player_turn == 1:
    print("Player 1 starts first (abc...)")
elif player_turn == 2:
    print("Player 2 starts first (ABC...)")
player_turn += 1

# Function to empty the board and make the 'chess spots' global
def chess_board_empty():
    global a_variable, b_variable, c_variable, d_variable, e_variable, f_variable, g_variable, h_variable, i_variable, A_bot_variable, B_bot_variable, C_bot_variable, D_bot_variable, E_bot_variable, F_bot_variable, G_bot_variable, H_bot_variable, I_bot_variable
    a_variable = b_variable = c_variable = d_variable = e_variable = f_variable = g_variable = h_variable = i_variable = A_bot_variable = B_bot_variable = C_bot_variable = D_bot_variable = E_bot_variable = F_bot_variable = G_bot_variable = H_bot_variable = I_bot_variable = " "
chess_board_empty()

# Function to show two playing boards
def chess_board():
    print(f"\n {a_variable} | {b_variable} | {c_variable}           {A_bot_variable} | {B_bot_variable} | {C_bot_variable}")
    print(f" {d_variable} | {e_variable} | {f_variable}           {D_bot_variable} | {E_bot_variable} | {F_bot_variable}")
    print(f" {g_variable} | {h_variable} | {i_variable}           {G_bot_variable} | {H_bot_variable} | {I_bot_variable}")
chess_board()

# Player decides which slot to designate the number to
while True:
    player_choice_slot = input("Which slot: ")
    player_random_dice = random.randint(1, 6)
    if player_choice_slot == "a":
        a_variable = player_random_dice
    elif player_choice_slot == "b":
        b_variable = player_random_dice
    elif player_choice_slot == "c":
        c_variable = player_random_dice
    elif player_choice_slot == "d":
        d_variable = player_random_dice
    elif player_choice_slot == "e":
        e_variable = player_random_dice
    elif player_choice_slot == "f":
        f_variable = player_random_dice
    elif player_choice_slot == "g":
        g_variable = player_random_dice
    elif player_choice_slot == "h":
        h_variable = player_random_dice
    elif player_choice_slot == "i":
        i_variable = player_random_dice
    elif player_choice_slot == "A":
        A_bot_variable = player_random_dice
    elif player_choice_slot == "B":
        B_bot_variable = player_random_dice
    elif player_choice_slot == "C":
        C_bot_variable = player_random_dice
    elif player_choice_slot == "D":
        D_bot_variable = player_random_dice
    elif player_choice_slot == "E":
        E_bot_variable = player_random_dice
    elif player_choice_slot == "F":
        F_bot_variable = player_random_dice
    elif player_choice_slot == "G":
        G_bot_variable = player_random_dice
    elif player_choice_slot == "H":
        H_bot_variable = player_random_dice
    elif player_choice_slot == "I":
        I_bot_variable = player_random_dice
    else:
        print("Choose a letter from a to i for P1, or A to I for P2.")
        continue
    
    # Condition which will end the game soon as one of the boards is filled
    if (a_variable != " " and b_variable != " " and c_variable != " " and 
        d_variable != " " and e_variable != " " and f_variable != " " and 
        g_variable != " " and h_variable != " " and i_variable != " "):
        print("Over! P1 filled the board")
        chess_board()
        break
    elif (A_bot_variable != " " and B_bot_variable != " " and C_bot_variable != " " and 
        D_bot_variable != " " and E_bot_variable != " " and F_bot_variable != " " and 
        G_bot_variable != " " and H_bot_variable != " " and I_bot_variable != " "):
        print("Over! P2 filled the board")
        chess_board()
        break

    # Printing the player turns
    if player_turn % 2 == 0:
        player_turn += 1
        print("Player 2 turn")
    else:
        player_turn += 1
        print("Player 1 turn")

    chess_board()

# Making the points into integer
def safe_convert_to_int(variable):
    return int(variable) if variable != " " else 0
summed_points_p1 = (safe_convert_to_int(a_variable) + safe_convert_to_int(b_variable) + safe_convert_to_int(c_variable) + safe_convert_to_int(d_variable) + safe_convert_to_int(e_variable) + safe_convert_to_int(f_variable) + safe_convert_to_int(g_variable) + safe_convert_to_int(h_variable) + safe_convert_to_int(i_variable))
summed_points_p2 = (safe_convert_to_int(A_bot_variable) + safe_convert_to_int(B_bot_variable) + safe_convert_to_int(C_bot_variable) + safe_convert_to_int(D_bot_variable) + safe_convert_to_int(E_bot_variable) + safe_convert_to_int(F_bot_variable) + safe_convert_to_int(G_bot_variable) + safe_convert_to_int(H_bot_variable) + safe_convert_to_int(I_bot_variable))
# Total points summed up
print(f"Player 1 points are: {summed_points_p1}")
print(f"Player 2 points are: {summed_points_p2}")
#  Printing which player won based on points, or ends up on a draw
if summed_points_p1 > summed_points_p2:
    print("Player 1 wins!")
elif summed_points_p2 > summed_points_p1:
    print("Player 2 wins!")
elif summed_points_p2 == summed_points_p1:
    print("That's a draw!")