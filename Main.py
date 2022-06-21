import pygame
import math
from game import Game
pygame.init()
#définier une clock
clock = pygame.time.Clock()
FPS  = 450


#generer la fenetre de notre jeu
pygame.display.set_caption("Comet fall Game")
screen = pygame.display.set_mode((1080,720))

#importer de charger l'arrierre plan de notre jeu
background = pygame.image.load('assets/bg.jpg')

#import changer notre bannire
banner = pygame.image.load('assets/banner.png')
banner = pygame.transform.scale(banner,(500,500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width()/4)
# import charger notre bouton pour lancer la partie
play_button = pygame.image.load('assets/button.png')
play_button = pygame.transform.scale(play_button,(400,150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width()/3.33)
play_button_rect.y = math.ceil(screen.get_height()/2)

#charger notre jou
game = Game()
running = True
while running:


    #appliquer l'arrierre plan de notre jeu
    screen.blit(background,(0,-200))
    #vérifier  si notre jeu a commencé ou non
    if game.is_playing:
        game.update(screen)
    # vérifier si notre  jeu n'a pas commencé

    else :
        #ajouté mon ecran de biebvenue

       screen.blit(play_button,(play_button_rect))
       screen.blit(banner, banner_rect)

    #mettre  àn jeur k'ecran
    pygame.display.flip()
    #si le joueur ferme cette fenetre
    for event in pygame.event.get():
        # que l'evenelent est fermeture de fenetre
     if event.type == pygame.QUIT:
        running=False
        pygame.quit()
        print("Fermeture du jeu")
     #detecter si un joueur lache une touche du clavier
     elif event.type==pygame.KEYDOWN:
         game.pressed[event.key] = True
         #detecter si la touche espace est enclenchée pour lancer notre projectile
         if event.key==pygame.K_SPACE:
             if game.is_playing:
                game.player.launch_projectile()
             else:
                 game.start()
                 game.sound_manager.play('click')
     elif event.type==pygame.KEYUP:
         game.pressed[event.key] = False
     elif event.type == pygame.MOUSEBUTTONDOWN:
         if play_button_rect.collidepoint(event.pos):
             game.start()
             game.sound_manager.play('click')
     clock.tick(FPS)