"""
Hangman
By: Suryakiran Santhosh
"""


from word_generator import word_generator
import utils

import pygame
import math


def main():

    # Window Variables
    WIDTH, HEIGHT = 800, 500
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    # game variable
    hangman_status = 0  # var that stores the state of the game
    randomWord = word_generator().upper()
    guessed = []
    print(randomWord)

    # Button Variables
    RADIUS = 20
    GAP = 15
    letters = []  # list[list], [[x, y, letter, Visibility of button]]
    startx = round((WIDTH - ((RADIUS * 2) + GAP) * 13)/2)
    starty = 400

    A = 65  # ASCII code for capital A

    # rendering the letter buttons
    for i in range(26):
        x = (startx + (GAP * 2) + (((RADIUS * 2) + GAP) * (i % 13)))
        y = starty + ((i // 13) * (GAP + RADIUS * 2))
        letters.append([x, y, chr(A + i), True])

    pygame.init()
    window = pygame.display.set_mode((WIDTH, HEIGHT))  # size of tab
    pygame.display.set_caption("Hangman Game!")  # window name

    FONT = pygame.font.SysFont('comicsans', 40)  # font of letters
    WORD_FONT = pygame.font.SysFont('comicsans', 60)  # word font
    TITLE_FONT = pygame.font.SysFont('comicsans', 70)  # Game title

    images = utils.load_images()  # states of the game

    FPS = 60  # speed of all game, the max FPS
    clock = pygame.time.Clock()  # count the time at FPS
    run = True

    # game loop
    while run:
        clock.tick(FPS)  # to make sure the while loop runs at the speed defined

        # need to look for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # if the red X button is pressed the game will end
                run = False

            # mouse movement event and keeping track of position of mouse
            if event.type == pygame.MOUSEBUTTONDOWN:  # to check for mouse button press
                # finds the location of that the mouse pressed
                coordinateX, coordinateY = pygame.mouse.get_pos()

                # find the distance from each of the buttons to the location of the mouse press
                for letter in letters:
                    x, y, ltr, visible = letter

                    if visible:
                        distance = math.sqrt(((x - coordinateX) ** 2) + ((y - coordinateY) ** 2))

                        # if the mouse press distance is less than the radius then we know the user pressed within the
                        # bounds of the button
                        if distance < RADIUS:
                            letter[3] = False
                            guessed.append(ltr)

                            if ltr not in randomWord:
                                hangman_status += 1

        utils.draw(window, BLACK, WHITE, RADIUS, WIDTH, images, hangman_status, letters, FONT, randomWord, guessed, WORD_FONT, TITLE_FONT)  # draw the game screen

        # check wins
        won = True
        for letter in randomWord:
            if letter not in guessed:
                won = False
                break

        if won:
            message = "YOU WON"
            utils.display_winner(window, message, WORD_FONT, WHITE, BLACK, WIDTH, HEIGHT)
            break
        elif hangman_status == 6:
            message = "YOU LOST BETTER LUCK NEXT TIME"
            utils.display_winner(window, message, WORD_FONT, WHITE, BLACK, WIDTH, HEIGHT)
            break

    pygame.quit()  # close the window


if __name__ == "__main__":
    main()
