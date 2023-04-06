import pygame
import sqlite3
from monster import Monster
from monster_2 import Monster_2
from monster_3 import Monster_3
from player import Player


# class qui represente le jeux
class Game:

    def __init__(self):
        self.is_playing = False
        self.menu = True
        self.option = False
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        self.all_monsters = pygame.sprite.Group()
        self.pressed = {}
        self.score = 0
        self.stage = 1
        self.mob_counter = 1
        self.monster = Monster(self, self.player)
        self.monster2 = Monster_2(self, self.player)
        self.monster3 = Monster_3(self, self.player)
        self.movement = True
        self.score_best = 0
        self.score_last = 0


    def start(self):
        self.is_playing = True
        self.spawn_monster_3()

    def game_over(self):
        self.all_monsters = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.is_playing = False
        self.menu = True

    def update(self, screen, arial_font, white):
        self.player.update_health_bar(screen)
        score_text = arial_font.render(f"Score: {self.score}", True, white)
        stage_text = arial_font.render(f"Stage: {self.stage}", True, white)


        # autre monstre
        self.second_mob()
        self.third_mob()
        self.four_mob()
        self.five_mob()
        self.six_mob()
        self.seven_mob()

        # récuperer les projectile
        for projectile in self.player.all_projectiles:
            if self.movement:
                projectile.move(score_text)

        for monster in self.all_monsters:
            monster.update_health_bar(screen)
            if self.movement:
                monster.forward()

        # applique l'ensemble des image
        self.player.all_projectiles.draw(screen)

        self.all_monsters.draw(screen)

        screen.blit(self.player.image, self.player.rect)
        screen.blit(score_text, [10, 10])
        screen.blit(stage_text, [1150, 15])

        # mettre a jour l'ecran

        # verifier la direction pour touche
        if self.pressed.get(pygame.K_q) and self.player.rect.x > 0 and self.movement:
            self.player.move_left()
        elif self.pressed.get(pygame.K_d) and self.player.rect.x + self.player.rect.width < screen.get_width() and self.movement:
            self.player.move_right()

    def second_mob(self):
        if self.score >= 300 and self.mob_counter < 2:
            self.spawn_monster_3()
            self.mob_counter += 1
            self.stage += 1

    def third_mob(self):
        if self.score >= 1000 and self.mob_counter < 3:
            self.spawn_monster_3()
            self.mob_counter += 1
            self.stage += 1

    def four_mob(self):
        if self.score >= 1500 and self.mob_counter < 4:
            self.spawn_monster_2()
            self.mob_counter += 1
            self.stage += 1

    def five_mob(self):
        if self.score >= 3000 and self.mob_counter < 5:
            self.spawn_monster_2()
            self.mob_counter += 1
            self.stage += 1

    def six_mob(self):
        if self.score >= 4000 and self.mob_counter < 6:
            self.spawn_monster()
            self.mob_counter += 1
            self.stage += 1

    def seven_mob(self):
        if self.score >= 5000 and self.mob_counter < 7:
            self.spawn_monster()
            self.mob_counter += 1
            self.stage += 1

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monster(self):
        monster = Monster(self, self.player)
        self.all_monsters.add(monster)

    def spawn_monster_2(self):
        monster = Monster_2(self, self.player)
        self.all_monsters.add(monster)

    def spawn_monster_3(self):
        monster = Monster_3(self, self.player)
        self.all_monsters.add(monster)

    def text_best_score(self, screen, arial_font, white):
        text_best_score = arial_font.render("Le meilleur score:", True, white)
        screen.blit(text_best_score, [100, 400])

    def best_score(self, screen, arial_font, white):
        best_score = arial_font.render(f"{self.score_best}", True, white)
        screen.blit(best_score, [160, 450])

    def text_last_score(self, screen, arial_font, white):
        text_last_score = arial_font.render("Le dernier score:", True, white)
        screen.blit(text_last_score, [940, 400])

    def test_last_score(self, screen, arial_font, white):
        last_score = arial_font.render(f"{self.score_last}", True, white)
        screen.blit(last_score, [1000, 450])

    def new_score_add(self):
        connection = sqlite3.connect("base.db")
        cursor = connection.cursor()
        new_score = (cursor.lastrowid, self.score)
        if self.score == 0:
            print("Score nul, pas ajouté à la base de donnée")
            pass
        else:
            cursor.execute("INSERT INTO player_score VALUES(?, ?)", new_score)
            print("Score ajouté à la base de donnée")
        connection.commit()

    def max_score(self):
        connection2 = sqlite3.connect("base.db")
        cursor2 = connection2.cursor()
        cursor2.execute("SELECT MAX(score) FROM player_score")
        max = cursor2.fetchone()
        self.score_best = max[0]

    def last_score(self):
        connection3 = sqlite3.connect("base.db")
        cursor3 = connection3.cursor()
        cursor3.execute("SELECT * FROM player_score WHERE score = ?", (cursor3.lastrowid,))
        self.score_last = cursor3.fetchone()
