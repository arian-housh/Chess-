import pygame
from const import *
from board import Board
from dragger import Dragger

class Game:
    def __init__(self):
        self.board = Board()
        self.dragger = Dragger()

    # blit methods
    def show_bg(self, surface):
        for row in range(rows):
            for col in range(cols):
                if (row + col) % 2 == 0:
                    color = (240,248,255) # white
                else:
                    color = (255,64,64) # red

                rect = (col * sq, row * sq, sq, sq)
                pygame.draw.rect(surface, color, rect)
    def show_pieces(self, surface):
        for row in range(rows):
            for col in range(cols):
                #checking if a block has a  piece
                if self.board.squares[row][col].has_piece():
                    # saving that piece into a new variable
                    piece = self.board.squares[row][col].piece

                    #all pieces except dragger piece
                    if piece is not self.dragger.piece:
                        piece.set_texture(size=80)

                        #convering the texture into an image
                        img = pygame.image.load(piece.texture)
                        #centering the image
                        img_center = col * sq + sq // 2, row * sq + sq //2
                        #assigin a new value to the center image
                        piece.texture_rect = img.get_rect(center=img_center)
                        #putting a new block
                        surface.blit(img, piece.texture_rect)