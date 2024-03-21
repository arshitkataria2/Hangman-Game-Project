import pygame
import math
import random

#The code for the game is Developed and Tested By Arshit Kataria
#Special Thanks To Arshdeep Singh for managing this project
#pygame has been used to code this game so please install it before running or run it on replit

pygame.init()
WIDTH, HEIGHT = 800, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman Game")

mode = "game"

credits_btn_pos = (680, 450)
credits_btn_size = (80, 30)
back_btn_pos = (690, 450)
back_btn_size = (100, 50)
reset_btn_pos = (20, 450) 
reset_btn_size = (100, 30)
instructions_btn_pos = (315, 450)
instructions_btn_size = (100, 50)


RADIUS = 20
GAP = 15
letters = []
startx = round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2)
starty = 350
A = 65
for i in range(26):
    x = startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
    y = starty + ((i // 13) * (GAP + RADIUS * 2))
    letters.append([x, y, chr(A + i), True])

LETTER_FONT = pygame.font.SysFont('Helvetica', 40)
WORD_FONT = pygame.font.SysFont('Helvetica', 60)
TITLE_FONT = pygame.font.SysFont('Helvetica', 70)


hangman_status = 0
animation_frame = 0
words = ["GITHUB", "HANGMAN", "GAME", "SCM" , "COOL" , "DEVELOPER", "CODER" ,"PYTHON" , "EASY" , "WHAT" , "STICK", "NUMBER" , "SUMMER"  ]
word = random.choice(words)
guessed = []

is_animating = False
current_frame = 0

def load_image(set_number, frame_number):
    filename = f"{set_number}_{frame_number}.gif"
    return pygame.image.load(filename)

def animate_wrong_guess():
    global is_animating, current_frame
    is_animating = True
    for frame in range(5): 
        win.fill(WHITE)
        image = load_image(hangman_status, frame)
        win.blit(image, (150, 100))
        pygame.display.update()
        pygame.time.delay(200)  
    is_animating = False
    current_frame = 0

def animate_win():
    global is_animating, hangman_status
    is_animating = True

    for status in range(hangman_status, -1, -1):
        for frame in range(4, -1, -1):
            win.fill(WHITE)
            image = load_image(status, frame) 
            win.blit(image, (150, 100))
            pygame.display.update()
            pygame.time.delay(100)  
            
        
        pygame.time.delay(200)
    
    is_animating = False
    hangman_status = 0  


def reset_game():
    global hangman_status, guessed, word, is_animating, letters
    hangman_status = 0
    guessed = []
    word = random.choice(words)
    is_animating = False
    for letter in letters:
        letter[3] = True  

WHITE = (255,255,255)
BLACK = (0,0,0)


def draw():
    win.fill(WHITE)
    if mode == "game":
       
        text = TITLE_FONT.render("Hangman Game", 1, BLACK)
        win.blit(text, (WIDTH / 2 - text.get_width() / 2, 20))

        display_word = ""
        for letter in word:
            if letter in guessed:
                display_word += letter + " "
            else:
                display_word += "_ "
        text = WORD_FONT.render(display_word, 1, BLACK)
        win.blit(text, (WIDTH / 2 - text.get_width() / 2, 200))

        reset_text = LETTER_FONT.render("Reset", 1, BLACK)
        win.blit(reset_text, reset_btn_pos)
        instructions_text = LETTER_FONT.render("Instructions", 1, BLACK)
        win.blit(instructions_text, instructions_btn_pos)

        for letter in letters:
            x, y, ltr, visible = letter
            if visible:
                pygame.draw.circle(win, BLACK, (x, y), RADIUS, 3)
                text = LETTER_FONT.render(ltr, 1, BLACK)
                win.blit(text, (x - text.get_width() / 2, y - text.get_height() / 2))

        credits_text = LETTER_FONT.render("Credits", 1, BLACK)
        win.blit(credits_text, credits_btn_pos)

    elif mode == "credits":
        back_text = LETTER_FONT.render("Back", 1, BLACK)
        win.blit(back_text, back_btn_pos)

        credits_info = ["Developer and Tester: Arshit Kataria", "Product Manager: Arshdeep Singh"]
        for i, info in enumerate(credits_info):
            text = LETTER_FONT.render(info, 1, BLACK)
            win.blit(text, (100, 100 + i * 60))

    elif mode == "instructions":
        instructions = [
            "Welcome to the Hangman Game!",
            "Guess the word by clicking on the letters",
            "or typing them on your keyboard.",
            "Click 'Reset' to start over at any time.",
            "Press 'Back' to return to the game."
                       ]
        for i, line in enumerate(instructions):
            text = LETTER_FONT.render(line, 1, BLACK)
            win.blit(text, (20, 20 + i * 60))
        
        back_text = LETTER_FONT.render("Back", 1, BLACK)
        win.blit(back_text, back_btn_pos)      

    pygame.display.update()
    
def display_message(message):
    pygame.time.delay(1000)
    win.fill(WHITE)
    text = WORD_FONT.render(message, 1, BLACK)
    win.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(3000)


def main():
    global mode, hangman_status, is_animating
    run = True
    FPS = 60
    clock = pygame.time.Clock()

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN and not is_animating:
                m_x, m_y = pygame.mouse.get_pos()

      
                if mode == "instructions":
                    if back_btn_pos[0] <= m_x <= back_btn_pos[0] + back_btn_size[0] and back_btn_pos[1] <= m_y <= back_btn_pos[1] + back_btn_size[1]:
                        mode = "game"
                        continue 

                elif mode == "game":
                    if instructions_btn_pos[0] <= m_x <= instructions_btn_pos[0] + instructions_btn_size[0] and instructions_btn_pos[1] <= m_y <= instructions_btn_pos[1] + instructions_btn_size[1]:
                        mode = "instructions"
                    elif credits_btn_pos[0] <= m_x <= credits_btn_pos[0] + credits_btn_size[0] and credits_btn_pos[1] <= m_y <= credits_btn_pos[1] + credits_btn_size[1]:
                        mode = "credits"
                    elif reset_btn_pos[0] <= m_x <= reset_btn_pos[0] + reset_btn_size[0] and reset_btn_pos[1] <= m_y <= reset_btn_pos[1] + reset_btn_size[1]:
                        reset_game()
                    else:
                        for letter in letters:
                            x, y, ltr, visible = letter
                            if visible:
                                dis = math.sqrt((x - m_x) ** 2 + (y - m_y) ** 2)
                                if dis < RADIUS:
                                    letter[3] = False
                                    guessed.append(ltr)
                                    if ltr not in word:
                                        hangman_status += 1
                                        if hangman_status < 6:
                                            animate_wrong_guess()

                elif mode == "credits":
                    if back_btn_pos[0] <= m_x <= back_btn_pos[0] + back_btn_size[0] and back_btn_pos[1] <= m_y <= back_btn_pos[1] + back_btn_size[1]:
                        mode = "game"
            if event.type == pygame.KEYDOWN and mode == "game":
                if 'a' <= event.unicode <= 'z':
                    ltr = event.unicode.upper()
                    if ltr not in guessed:
                        guessed.append(ltr)
                        if ltr not in word:
                            hangman_status += 1
                            if hangman_status < 6:
                                animate_wrong_guess()
                        for letter in letters:
                            if letter[2] == ltr:
                                letter[3] = False

        if not is_animating and mode == "game":
            draw()

        if mode == "game":
            won = all(letter in guessed for letter in word)

            if won:
                animate_win()
                display_message("You WON!")
                pygame.time.delay(1000)
                reset_game()

            if hangman_status == 6:
                animate_wrong_guess()
                display_message("You LOST!")
                pygame.time.delay(1000)
                reset_game()
        else:
            draw()


while True:
 main() 
pygame.quit()