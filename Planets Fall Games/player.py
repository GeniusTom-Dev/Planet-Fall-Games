import pygame
from projectile import Projectile


# cree une classe player
class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 12
        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.image.load('assets/player/jetoffv2.png')
        self.rect = self.image.get_rect()
        self.rect.x = 565
        self.rect.y = 620

    def damage(self, amount):
        # infliger des dégat
        self.health -= amount

        if self.health <= 0:
            self.game.game_over()
            self.game.new_score_add()
            print("Fin du jeu")

    def update_health_bar(self, surface):

        # dessiner la barre de vie et son arriere pan
        pygame.draw.rect(surface, (255, 0, 0), [self.rect.x, self.rect.y - 20, self.max_health, 5])

        pygame.draw.rect(surface, (66, 255, 0), [self.rect.x, self.rect.y - 20, self.health, 5])

    def launch_projectile(self):
        # cree une instance de la classe projectile
        self.all_projectiles.add(Projectile(self))


    def move_right(self):
        self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity
