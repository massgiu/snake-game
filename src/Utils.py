import pygame
import random
import tkinter as tk
from tkinter import messagebox

class Utils(object):

    @staticmethod
    def drawGrid(width, rows, surface):
        sizeBwn = width // rows

        x = 0
        y = 0
        for l in range(rows):
            x = x + sizeBwn
            y = y + sizeBwn
            # Vertical line
            pygame.draw.line(surface, (128, 128, 128), (x, 0), (x, width))
            # Horizontal line
            pygame.draw.line(surface, (128, 128, 128), (0, y), (width, y))

    # Update display
    @staticmethod
    def redrawWindow(surface, rows, width, snk, cookye):
        surface.fill((0, 0, 0))  # Fills the screen with black
        snk.draw(surface)
        cookye.draw_cube(surface)
        Utils.drawGrid(width, rows, surface)  # Will draw our grid lines
        pygame.display.update()  # Updates the screen

    # This function generates the coordinates x,y for a random cube to eat
    @staticmethod
    def randomSnack(rows, snk):
        while True:  # Keep generating random positions until we get a valid one
            x = random.randrange(rows)
            y = random.randrange(rows)
            # get a list with all position of snake's cube
            position_list = list(map(lambda z: z.pos, snk.body_list))
            if (x, y) in position_list:  # This wll check if the position we generated is occupied by the snake
                continue
            else:
                break

        return (x, y)

    @staticmethod
    def message_box(subject, content):
        root = tk.Tk()
        root.attributes("-topmost", True)
        root.withdraw()
        messagebox.showinfo(subject, content)
        try:
            root.destroy()
        except:
            pass

    @staticmethod
    def checkCrossing(snake):
        for x in range(len(snake.body_list)):
            # Check if snake head overlaps with its body
            if snake.body_list[0].pos in list(map(lambda z: z.pos, snake.body_list[1:])):
                print('Score: ', len(snake.body_list))
                self.message_box('You Lost!', 'Play again...')
                self.reset((10, 10))
                True

