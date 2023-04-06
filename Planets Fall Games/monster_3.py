import pygame
import random


class Monster_3(pygame.sprite.Sprite):

    def __init__(self, game, player):
        super().__init__()
        self.game = game
        self.health = 50
        self.max_health = 50
        self.attack = 25
        self.player = player
        self.image = pygame.image.load('assets/planets/planet_3.png')
        self.image = pygame.transform.scale(self.image, (230, 230))
        self.rect = self.image.get_rect()
        self.rect.y -= 250
        self.rect.x += random.randint(0, 1000)
        self.velocity = 3

    def damage(self, amount, score_text):
        # infliger des dégat
        self.health -= amount

        if self.health <= 0:
            # réaparaitre comme neuf
            self.rect.y = -512
            self.health = self.max_health
            self.rect.x = random.randint(0, 1000)
            self.game.score += 100
            score_text = f"Score: {self.game.score}"

    def update_health_bar(self, surface):

        # dessiner la barre de vie et son arriere pan
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 65, self.rect.y - 20, self.max_health * 2, 5])

        pygame.draw.rect(surface, (66, 255, 0), [self.rect.x + 65, self.rect.y - 20, self.health * 2, 5])

    def forward(self):
        self.rect.y += self.velocity
        if self.rect.y > 720:
            # supp le projectile
            self.rect.y = -1000
            self.health = self.max_health
            self.rect.x = random.randint(0, 1000)
            self.player.damage(self.attack)
            print("reset")


