import pygame
from pygame.math import Vector2

class Tile:
    def __init__(self,grid_pos:Vector2, tile_images:str, checkerboard:int, size:int):
        self.grid_pos:Vector2 = grid_pos
        self.tile_images = pygame.image.load(tile_images)
        self.size:int = size
        self.image = pygame.transform.scale(self.tile_images, (self.size*13,self.size))
        self.checkerboard:int = checkerboard%2
        self.screen_pos:Vector2 = Vector2(self.size*self.grid_pos.x,self.size*self.grid_pos.y)
        self.hitbox = pygame.rect.Rect(self.screen_pos[0],self.screen_pos[1],self.size,self.size)

        self.nearby_mines:int = 0
        self.is_mine:bool = False
        self.is_clicked:bool = False
        self.flaged:bool = False
        self.cant_be_mine:bool = False
        
        

    def draw(self, screen:pygame.surface.Surface):
        offset = self.nearby_mines - 1
        if self.is_mine:
            offset = 8
        if not self.is_clicked:
            if self.checkerboard == 0:
                screen.blit(self.image,self.screen_pos,(9*self.size,0,self.size,self.size))
            else:
                screen.blit(self.image,self.screen_pos,(10*self.size,0,self.size,self.size))
        else:
            if self.checkerboard == 0:
                screen.blit(self.image,self.screen_pos,(11*self.size,0,self.size,self.size))
            else:
                screen.blit(self.image,self.screen_pos,(12*self.size,0,self.size,self.size))
            screen.blit(self.image,self.screen_pos,(offset*self.size,0,self.size,self.size))
        if self.flaged:
            screen.blit(self.image,self.screen_pos,(7*self.size,0,self.size,self.size))