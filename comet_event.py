import pygame
from comet import Comet

#créer une classe pour gérerect evenemet
class CometFallEvent:
    #lors du chargement ->créer un comteur
    def __init__(self,game):
        self.percent = 0
        self.percent_speed = 10
        self.game = game
        self.fall_mode = False
        #definier un groupe de sprite pour stocker  nos cometes
        self.all_comets = pygame.sprite.Group()


    def add_percent(self):
        self.percent +=self.percent_speed/100
    def is_full_loaded(self):
        return self.percent >= 100


    def reset_percent(self):
        self.percent = 0


    def meteor_full(self):

        for i in range(1,10):
            self.all_comets.add(Comet(self))


    def attempt_fall(self):
        if self.is_full_loaded() and len(self.game.all_monsters)==0:
            print("Pluie de cometes ! ! ")
            self.meteor_full()
            self.fall_mode = True

    def update_bar(self,surface):
        #AJOUTE DU POURCENTAGE DE LA BAR
        self.add_percent()

        #barre noir (en arriere plan)
        pygame.draw.rect(surface,(0,0,0),[0,surface.get_height()-50,surface.get_width(),10])
        #barre rouge (jauge d'event
        pygame.draw.rect(surface,(187,11,11),[0,surface.get_height()-50,(surface.get_width()/100)*self.percent,10])
