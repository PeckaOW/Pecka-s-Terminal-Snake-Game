import os
from time import sleep
import keyboard
from random import randint

def clearboard():
    board.clear()
    for a in range(size):
        board1 = []
        for b in range(size):
            board1.append(NONE)
        board.append(board1)

def drawBoard():
    print('Score : ' + str(length))
    print('Direction : ' + str(direction))
    for a in board:
        for b in a:
            print(b, end = '')
        print('')

def drawsnake():
    for n, a in enumerate(snakes):
        if n == 0:
            board[a[1]][a[0]] = HEAD
        else:
            board[a[1]][a[0]] = BODY

def generate_apple():
    global applex, appley
    while True:
        applex = randint(0, size - 1)
        appley = randint(0, size - 1)
        if (applex, appley) != NONE:pass
        else:break
    board[appley][applex] = APPLE

def generate_bomb():
    global bombs
    while True:
        bombx = randint(0, size - 1)
        bomby = randint(0, size - 1)
        if board[bomby][bombx] != NONE:pass
        else:break
    bombs.append((bombx, bomby))
    board[bomby][bombx] = BOMB

APPLE = '●'
NONE = '□'
BODY = '■'
HEAD = '▣'
BOMB = 'Χ'

UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

#Start
print('My First Snake Game...')
print('● = Apple\n□ = BLANK\n■ = Snake Body\n▣ = Snake Head\nΧ = MINE\n-------------------------------------------------\n')
size = int(input('Enter the size of the board : '))
speed = int(input('Enter the game speed(1 ~ 9) : '))
time = 0.3 - (0.03 * speed)
bombf1 = int(input('Enter how frequent the bombs appear(0 ~ 9) : '))
bombf = 10 - bombf1
print('I recommned using fullscreen for the game optimization...\nPecka')
sleep(2)

snakex, snakey = int(size / 2) - 1, int(size / 2) - 1
applex, appley = 1, 1
bombs = []
length = 1
direction = UP

board = []
clearboard()

board[snakey][snakex] = HEAD
snakes = [(int(snakex), int(snakey))]
generate_apple()

print('Starting...')
sleep(2)
os.system('cls')
drawBoard()
sleep(1)

while True:
    sleep(time)
    os.system('cls')
    valid = False
    if keyboard.is_pressed(UP):
        if direction == DOWN:print('You killed yourself!')
        else:
            direction = UP
            valid = True
            snakey -= 1
    elif keyboard.is_pressed(DOWN):
        if direction == UP:print('You killed yourself!')
        else:
            direction = DOWN
            valid = True
            snakey += 1
    elif keyboard.is_pressed(LEFT):
        if direction == RIGHT:print('You killed yourself!')
        else:
            direction = LEFT
            valid = True
            snakex -= 1
    elif keyboard.is_pressed(RIGHT):
        if direction == LEFT:print('You killed yourself!')
        else:
            direction = RIGHT
            valid = True
            snakex += 1
    else:
        valid = True
        if direction == UP:snakey -= 1
        elif direction == DOWN:snakey += 1
        elif direction == RIGHT:snakex += 1
        elif direction == LEFT:snakex -= 1

    if valid and (snakex, snakey) in snakes:
        print('You killed yourself!')
        valid = False
    elif snakex > size - 1 or snakex < 0 or snakey > size - 1 or snakey < 0:
        valid = False
        print('You ran away!')

    if valid:
        snakes.insert(0, (snakex, snakey))
        if (snakex, snakey) in bombs:
            print('Fire in the HOLE!!!')
            valid = False
        if (snakex, snakey) == (applex, appley) and valid:
            length += 1
            generate_apple()
            for a in bombs:
                board[a[1]][a[0]] = NONE
            bombs.clear()
            for b in range(int(length / bombf) + 1):
                generate_bomb()
        if len(snakes) > length and valid:
            board[snakes[length][1]][snakes[length][0]] = NONE
            del snakes[length]
        if valid:
            drawsnake()
            drawBoard()

    if not valid:
        sleep(2)
        print('Your Score Is : ' + str(length))
        again = int(input('Play Again? (1 = Yes, 2 = No)'))
        if again == 1:
            sleep(1)
            clearboard()
            snakex, snakey = int(size / 2) - 1, int(size / 2) - 1
            applex, appley = 1, 1
            bombs = []
            length = 1
            direction = UP
            board[snakey][snakex] = HEAD
            snakes = [(int(snakex), int(snakey))]
            generate_apple()
            print('Starting...')
            drawBoard()
            sleep(1)
        else:break

print('Farewell!!!')
sleep(2)
