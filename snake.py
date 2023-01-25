import pygame
import time
import random

# Setup
pygame.init()
pygame.font.init()
font = pygame.font.SysFont('Comic Sans MS', 30)
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
dis = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('PySnake')
snake_color = (173, 255, 47) # green
fruit_color = (255, 255, 0)
BLOCK_SIZE = 40 # 600 / 40 means there are 15 blocks per row / column
AMOUNT_BLOCK = 14
snake_body = [[10,10], [11, 10], [12, 10]]
fruits = [[random.randint(0, AMOUNT_BLOCK), random.randint(0, AMOUNT_BLOCK)], [random.randint(0, AMOUNT_BLOCK), random.randint(0, AMOUNT_BLOCK)]]
player_key = ""
last_move = ""
score = 0
not_collision = True

def main():
        # Game Loop
        game_over=False
        while not game_over:
                # Check game over
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                game_over = True
                        if event.type == pygame.KEYDOWN:
                                global player_key
                                if event.key == pygame.K_ESCAPE:
                                    game_over = True
                                elif event.key == pygame.K_DOWN:
                                    player_key = "DOWN"
                                elif event.key == pygame.K_UP:
                                    player_key = "UP"
                                elif event.key == pygame.K_RIGHT:
                                    player_key = "RIGHT"
                                elif event.key == pygame.K_LEFT:
                                    player_key = "LEFT"
                global not_collision
                if (not_collision):
                    # Update game logic
                    global score
                    moveSnake(player_key)
                    if (not (snake_body[0][0] > -1 and snake_body [0][0] < AMOUNT_BLOCK + 1 and snake_body[0][1] > -1 and snake_body [0][1] < AMOUNT_BLOCK + 1)):
                        not_collision = False
                    if (checkEatFruit()):
                        find_free_square = True
                        while find_free_square:
                            temp_square = [random.randint(0, AMOUNT_BLOCK), random.randint(0, AMOUNT_BLOCK)]
                            if (temp_square not in snake_body) and (temp_snake_body not in fruits):
                                fruits.append(temp_square)
                                find_free_square = False
                        score += 100
                        new_body = snake_body[0].copy()
                        if player_key == "UP":
                            new_body[1] -= 1
                        elif player_key == "RIGHT":
                            new_body[0] += 1
                        elif player_key == "LEFT":
                            new_body[0] -= 1
                        elif player_key == "DOWN":
                            new_body[1] += 1
                        snake_body.append(new_body)
                    temp_snake_body = []
                    for element in range(len(snake_body)):
                        temp_snake_body.append(tuple(snake_body[element].copy()))
                    if len(set(temp_snake_body)) < len(temp_snake_body): #check collision
                        not_collision = False
                    
                # Draw Frame
                dis.fill((211,211,211)) # Grey
                drawGrid()
                drawFruits()
                drawSnake()
                score_text = font.render("Score " + str(score), False, (0, 0, 0))
                dis.blit(score_text, (10,0))
                if not not_collision:
                    gameover_text = font.render("Gameover", False, (0, 0, 0))
                    dis.blit(gameover_text, (WINDOW_HEIGHT / 2.5, WINDOW_WIDTH / 2.5))
                pygame.display.update()
                
                #wait
                if score == 0:
                    snake_speed = 0.5
                else:
                    snake_speed = 1 / ((score / 50) ** 0.6) # the higher the score, the higher the speed
                time.sleep(snake_speed)

        # De-Initialize
        pygame.display.quit()
        pygame.quit()
        quit()

def moveSnake(player_key):
    global last_move
    move_from = snake_body[0].copy()
    has_moved = False
    if player_key == "UP" and not last_move == "DOWN":
        last_move = "UP"
        snake_body[0][1] -= 1
        has_moved = True
    elif player_key == "DOWN" and not last_move == "UP":
        last_move = "DOWN"
        snake_body[0][1] += 1
        has_moved = True
    elif player_key == "LEFT" and not last_move == "RIGHT":
        last_move = "LEFT"
        snake_body[0][0] -= 1
        has_moved = True
    elif player_key == "RIGHT" and not last_move == "LEFT":
        last_move = "RIGHT"
        snake_body[0][0] += 1
        has_moved = True
    if(has_moved):
        for parts in range(1, len(snake_body)):
            temp_move_from = snake_body[parts].copy()
            snake_body[parts] = move_from.copy()
            move_from = temp_move_from

def checkEatFruit():
    for square in snake_body:
        if square in fruits:
            fruits.remove(square)
            return True
    return False

def drawFruits():
    for pos in fruits:
        x_position = pos[0] * BLOCK_SIZE
        y_position = pos[1] * BLOCK_SIZE
        rectangle = pygame.Rect(x_position, y_position, BLOCK_SIZE, BLOCK_SIZE)
        pygame.draw.rect(dis, fruit_color, rectangle)

def drawGrid():
    # draw vertical lines
    for x in range(0, WINDOW_WIDTH, BLOCK_SIZE):
        pygame.draw.line(dis, (0, 0, 0), (x, 0), (x, WINDOW_HEIGHT), 1)

    # draw horizontal lines
    for y in range(0, WINDOW_WIDTH, BLOCK_SIZE):
        pygame.draw.line(dis, (0, 0, 0), (0, y), (WINDOW_WIDTH, y), 1)

def drawSnake():
    for pos in snake_body:
        x_position = pos[0] * BLOCK_SIZE
        y_position = pos[1] * BLOCK_SIZE
        rectangle = pygame.Rect(x_position, y_position, BLOCK_SIZE, BLOCK_SIZE)
        pygame.draw.rect(dis, snake_color, rectangle)

if __name__ == '__main__':
        main()