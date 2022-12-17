import pygame
import random

# Initialize Pygame
pygame.init()

# Set the window size and title
window_size = (640, 480)
window_title = "Hangman"

# Create the window and set the caption
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption(window_title)

# Set the background color
bg_color = (255, 255, 255)

# Set the font and text color
font = pygame.font.Font(None, 36)
text_color = (0, 0, 0)

words = [
    "abrupt",
    "advice",
    "allow",
    "apart",
    "avoid",
    "basket",
    "believe",
    "breeze",
    "buzz",
    "cautious",
    "chaos",
    "cloth",
    "coast",
    "coffee",
    "coil",
    "commit",
    "compete",
    "concentrate",
    "conflict",
    "consume",
    "courage",
    "crumble",
    "crystal",
    "cuddle",
    "dazzle",
    "debate",
    "depart",
    "despair",
    "dew",
    "divert",
    "echo",
    "favor",
    "flaw",
    "grease",
    "groove",
    "guilt",
    "humble",
    "identify",
    "insist",
    "jerk",
    "journey",
    "judge",
    "knot",
    "lament",
    "latch",
    "lean",
    "leap",
    "loathe",
    "lone",
    "loom",
    "melt",
    "merge",
    "mourn",
    "muddle",
    "mutter",
    "nerve",
    "nest",
    "nudge",
    "obey",
    "offer",
    "pad",
    "pant",
    "pause",
    "peel",
    "peep",
    "perish",
    "pester",
    "poke",
    "ponder",
    "possess",
    "pout",
    "protest",
    "puzzle",
    "quake",
    "quiver",
    "rattle",
    "rebel",
    "resist",
    "savor",
    "scold",
    "screech",
    "sigh",
    "sink",
    "sneak",
    "sprint",
    "sulk",
    "sustain",
    "tempt",
    "thrive",
    "tremble"
]



# Select a random word from the list of words
secret_word = random.choice(words)

# Set the number of allowed misses
misses_allowed = 6

# Initialize variables
misses = 0
guesses = []
game_over = False

# Define the main game loop
running = True
while running:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # Check if the player has guessed a letter
            if event.unicode.isalpha():
                # Add the letter to the list of guesses
                guesses.append(event.unicode)
                # Check if the letter is in the secret word
                if event.unicode not in secret_word:
                    # Increment the number of misses
                    misses += 1

    # Clear the screen
    screen.fill(bg_color)

    # Draw the secret word on the screen
    secret_word_text = "".join([c if c in guesses else "*" for c in secret_word])
    text = font.render(secret_word_text, True, text_color)
    screen.blit(text, (50, 50))

    # Draw the number of misses on the screen
    misses_text = "Misses: {}/{}".format(misses, misses_allowed)
    text = font.render(misses_text, True, text_color)
    screen.blit(text, (50, 100))

    # Check if the game is over
    if misses == misses_allowed:
        game_over = True
    if "*" not in secret_word_text:
        game_over = True

    # Draw the game over message on the screen
    # Draw the secret word on the screen
    if game_over:
        secret_word_text = secret_word
    else:
        secret_word_text = "".join([c if c in guesses else "*" for c in secret_word])
    text = font.render(secret_word_text, True, text_color)
    screen.blit(text, (50, 50))


    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
