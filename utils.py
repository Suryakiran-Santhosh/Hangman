"""
Utility Functions for Hangman
By: Suryakiran Santhosh
"""


import pygame


def load_images() -> list[object]:
    images = []  # holds all the images in chronological order of game status

    # 7 stages in the game therefore 7 images to render
    for i in range(0, 7, 1):
        # load each image from subdirectory named "images"
        image = pygame.image.load(f"./images/hangman{i}.png")
        images.append(image)

    return images


def draw(window, BLACK, WHITE, RADIUS, WIDTH, images, hangman_status, letters, FONT, randomWord, guessed, WORD_FONT, TITLE_FONT):
    # render the background color of window, pygame format: fill((red=___, green=____, blue=____))
    # range of colors: 0 to 255
    window.fill(WHITE)  # white background

    # game title
    text = TITLE_FONT.render("HANGMAN!!", 1, BLACK)
    window.blit(text, (WIDTH/2 - text.get_width()/2, 20))

    # display random word
    display_word = ""
    for letter in randomWord:
        if letter in guessed:
            display_word += (letter + " ")
        else:
            display_word += "_ "

    text = WORD_FONT.render(display_word, 1, BLACK)
    window.blit(text, (400, 200))

    # draw letters and updated letters
    for letter in letters:
        x, y, ltr, visible = letter
        if visible:
            pygame.draw.circle(surface=window, color=BLACK, center=(x, y), radius=RADIUS, width=3)
            text = FONT.render(ltr, 1, BLACK)
            window.blit(text, (x - text.get_width() / 2, y - text.get_height() / 2))

    window.blit(source=images[hangman_status], dest=(150, 100))  # draw initial state of the game

    # after drawing something in pygame you have to manually update the window to render it
    pygame.display.update()


def display_winner(window, message, WORD_FONT, WHITE, BLACK, WIDTH, HEIGHT) -> None:
    pygame.time.delay(1000)
    window.fill(WHITE)
    text = WORD_FONT.render(f"{message}!", 1, BLACK)
    window.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(2000)
