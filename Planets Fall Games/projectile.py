import pygame


# defnir la classe projectile du joueur


class Projectile(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.velocity = 10
        self.allow_move = True
        self.player = player
        self.image = pygame.image.load('assets/player/projectile.png')
        self.image = pygame.transform.scale(self.image, (70, 70))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 25
        self.rect.y = player.rect.y - 50
        self.origin_image = self.image
        self.angle = 0


    def rotate(self):
        self.angle += 12
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def remove(self):
        self.player.all_projectiles.remove(self)

    def move(self, score_text):
        if self.allow_move:
            self.rect.y -= self.velocity
            self.rotate()

        for monster in self.player.game.check_collision(self, self.player.game.all_monsters):
            self.remove()
            # infliger des dégat
            monster.damage(self.player.attack,score_text)

        # verifier si le projectile est dans l'ecran
        if self.rect.y < -50:
            # supp le projectile
            self.remove()
