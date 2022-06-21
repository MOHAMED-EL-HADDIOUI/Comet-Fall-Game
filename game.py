import pygame
from player import Playser
from monster import Mummy,Alien
from comet_event import  CometFallEvent
from sounds import SoundManager
from monster import Monster
# creer une seconde class qui va representer notre jeu
class Game:

    def __init__(self):
        self.is_playing = False
        #generer notre joueur
        self.all_players = pygame.sprite.Group()
        self.player = Playser(self)
        self.all_players.add(self.player)
        #generer l'evenement
        self.comet_event = CometFallEvent(self)
        #groupe de monsters
        self.all_monsters = pygame.sprite.Group()
        self.score = 0
        self.pressed={}
        self.font = pygame.font.Font("assets/PottaOne.ttf",25)
        self.sound_manager = SoundManager()

    def add_score(self,points =10):
        self.score += points
    def start(self):
        self.is_playing = True
        self.spawn_monster(Mummy)
        self.spawn_monster(Mummy)
        self.spawn_monster(Alien)
    def game_over(self):
        self.all_monsters = pygame.sprite.Group()
        self.comet_event.all_comets =  pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.comet_event.reset_percent()
        self.is_playing = False
        self.score = 100
        self.sound_manager.play('game_over')

    def update(self,screen):
        #afficher le score sur l'écran

        score_text = self.font.render(f"Score : {self.score}",1,(255,255,255))
        screen.blit(score_text,(20,20))
        # appliquer l'image de mon joueur
        screen.blit(self.player.image, self.player.rect)

        # ACTUALISER LA BARRE DE LA VIE DU JOUEUR

        self.player.update_health_bar(screen)

        #actualiser la barre  l'evement du jeu
        self.comet_event.update_bar(screen)


        self.player.update_animation()
        # recuperer  les projectiles du joueur
        for projectile in self.player.all_projectiles:
            projectile.move()

        # recuperer les mostres de notre jeu
        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)
            monster.update_animation()

        #recipererle comentde notre jeu
        for  comet in self.comet_event.all_comets:
            comet.fall()
        # appliquer l'ensemble des images de mon groupe de projectiles

        self.player.all_projectiles.draw(screen)

        # appliquer l'ensemble des images de mon groupe de monstre
        self.all_monsters.draw(screen)

        # appliquer l'ensemble des  images demon groupedecoments
        self.comet_event.all_comets.draw(screen)

        # vérivifier si le joueur souhaite aller à gauche ou à droite
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()


    def chek_collision(self,sprite,group):
        return pygame.sprite.spritecollide(sprite,group,False,pygame.sprite.collide_mask)
    def spawn_monster(self,monster_class_name):
        monster = Mummy(self)
        self.all_monsters.add(monster_class_name.__call__(self))
