from ast import main
from operator import imod
# it is a module in python for generating random numbers
import random
import sys  # when we want to exit the game for user then we use sys.exit
import pygame
from pygame.locals import *

# make the global variable for the random.game
FPS = 32  # rendering of the image per second of the images
SCREENWIDTH = 289
SCREENHEIGHT = 511
# this line initialise a screen for display or access the screen from the pygame module
SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
GROUNDY = SCREENHEIGHT*0.8
GAME_SPRITES = {}  # IMAGES USED IN GAME
GAME_SOUNDS = {}
PLAYER = 'gallery/sprites/greybird.png'  # PATH FOR IMAGE OF PLAYER
# MAKED THE BACKGROUND VARRIABLE
BACKGROUND = "gallery/sprites/backf.png"
PIPE = 'gallery/sprites/pipe.png'

if __name__ == "__main__":
    # this will be the main func from where the game will start
    pygame.init()  # initialise all the modules of all pygame modules
    # if we mark 40(control fps) for the clock then the program will not run excess of 40 fps
    FPSCLOCK = pygame.time.Clock()
    pygame.display.set_caption('Flappy Bird 2.O By_Amit Kumar')
    GAME_SPRITES['numbers'] = (
        pygame.image.load('gallery/sprites/0.png').convert_alpha(),
        pygame.image.load('gallery/sprites/1.png').convert_alpha(),
        pygame.image.load('gallery/sprites/2.png').convert_alpha(),
        pygame.image.load('gallery/sprites/3.png').convert_alpha(),
        pygame.image.load('gallery/sprites/4.png').convert_alpha(),
        pygame.image.load('gallery/sprites/5.png').convert_alpha(),
        pygame.image.load('gallery/sprites/6.png').convert_alpha(),
        pygame.image.load('gallery/sprites/7.png').convert_alpha(),
        pygame.image.load('gallery/sprites/8.png').convert_alpha(),
        pygame.image.load('gallery/sprites/9.png').convert_alpha(),
    )
    GAME_SPRITES['message'] = pygame.image.load(
        'gallery/sprites/mess.png').convert_alpha()
    GAME_SPRITES['base'] = pygame.image.load(
        'gallery/sprites/mess.png').convert_alpha()
    GAME_SPRITES['pipe'] = (
        # pygame.transform.rotate rotate the right image to invert by 180 degree mentioned
        pygame.transform.rotate(pygame.image.load(PIPE).convert_alpha(), 180),
        pygame.image.load(PIPE).convert_alpha()  # GIVE THE ERECT IMAGE
    )
    # audio sprites
    GAME_SOUNDS['die'] = pygame.mixer.Sound('gallery/audio/die.wav')
    GAME_SOUNDS['hit'] = pygame.mixer.Sound('gallery/audio/hit.wav')
    GAME_SOUNDS['point'] = pygame.mixer.Sound('gallery/audio/point.wav')
    GAME_SOUNDS['swoosh'] = pygame.mixer.Sound('gallery/audio/swoosh.wav')
    GAME_SOUNDS['wing'] = pygame.mixer.Sound('gallery/audio/wing.wav')

    # background
    # convert only changes the image pixel for quick bliting
    GAME_SOUNDS['background'] = pygame.image.load(BACKGROUND).convert()
    GAME_SOUNDS['player'] = pygame.image.load(PLAYER).convert_alpha()
    while True:
        welcomeScreen()  # this func we write to return welcome screen when any user press any button
        mainGame()  # after welcomescreen main game starts
