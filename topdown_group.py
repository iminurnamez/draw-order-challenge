import pygame as pg

class TopdownGroup(pg.sprite.Group):
    def __init__(self, *sprites):
        super(TopdownGroup, self).__init__(*sprites)
        
    def draw(self, surface):
        ordered = sorted(self.sprites(), key=lambda x: x.rect.bottom)
        for sprite in ordered:
            sprite.draw(surface)