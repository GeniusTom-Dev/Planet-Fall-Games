import pygame
from game import Game
import math

pygame.init()

# generer la fenetre

pygame.display.set_caption("Planets Fall Games")
icon = pygame.image.load('assets/menu/cometoff.png')
pygame.display.set_icon(icon)
screen = pygame.display.set_mode((1280, 720))

# BackGround
BackGround = pygame.image.load('assets/menu/bgoff.png')

# charger la baniere
banner = pygame.image.load('assets/menu/banner.png')
banner = pygame.transform.scale(banner, (720, 405))

play_button = pygame.image.load('assets/button/play_button.png')
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 3) + 50
play_button_rect.y = 300

game_button = pygame.image.load('assets/button/game_button.png')
game_button_rect = game_button.get_rect()
game_button_rect.x = math.ceil(screen.get_width() / 3) + 50
game_button_rect.y = 450

quit_button = pygame.image.load('assets/button/quit_button.png')
quit_button_rect = quit_button.get_rect()
quit_button_rect.x = math.ceil(screen.get_width() / 3) + 50
quit_button_rect.y = 600

back_button = pygame.image.load('assets/button/back_button.png')
back_button_rect = back_button.get_rect()
back_button_rect.x = 20
back_button_rect.y = 20

pause_button = pygame.image.load('assets/button/pause_button.png')
pause_button_rect = pause_button.get_rect()
pause_button_rect.x = 1150
pause_button_rect.y = 90

replay_button = pygame.image.load('assets/button/replay_button.png')
replay_button_rect = replay_button.get_rect()
replay_button_rect.x = 1150
replay_button_rect.y = 50

menu_button = pygame.image.load('assets/button/menu_button.png')
menu_button_rect = menu_button.get_rect()
menu_button_rect.x = 1150
menu_button_rect.y = 130

option = pygame.image.load('assets/menu/option PFG.png')

white = (255, 255, 255)
arial_font = pygame.font.Font("assets/heros.ttf", 20)
arial_font_30 = pygame.font.Font("assets/heros.ttf", 35)

# Charger le jeu
game = Game()

running = True
pause = False

while running:
    game.max_score()

    # appliquer le bg
    screen.blit(BackGround, (0, 0))

    if game.is_playing and game.menu is False:
        game.update(screen, arial_font, white)
        screen.blit(replay_button, replay_button_rect)
        screen.blit(pause_button, pause_button_rect)
        screen.blit(menu_button, menu_button_rect)

    if game.is_playing is False and game.menu is True:
        screen.blit(banner, (280, -20))
        screen.blit(game_button, game_button_rect)
        screen.blit(play_button, play_button_rect)
        screen.blit(quit_button, quit_button_rect)
        game.best_score(screen, arial_font_30, white)
        game.text_best_score(screen, arial_font, white)
        game.text_last_score(screen, arial_font, white)
        game.test_last_score(screen, arial_font_30, white)
        game.last_score()

    if game.is_playing is False and game.menu is False and game.option is True:
        screen.blit(option, (0, 0))
        screen.blit(back_button, back_button_rect)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        # detecter si un joueur lache une touche du claveir
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            if event.key == pygame.K_SPACE:
                if game.movement:
                    game.player.launch_projectile()



        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if game.is_playing is False and game.option is False and play_button_rect.collidepoint(event.pos):
                print("Démmarage du jeu")
                game.start()
                game.score = 0
                game.movement = True
                game.stage = 1
                game.menu = False

            if game.menu is True and game.is_playing is False and game_button_rect.collidepoint(event.pos):
                print("Ouverture des options")
                game.menu = False
                game.option = True

            if game.is_playing == False and game.menu == False and back_button_rect.collidepoint(event.pos):
                print("Fermeture des option")
                game.menu = True
                game.option = False

            if game.menu == False and game.option == False and pause_button_rect.collidepoint(event.pos):
                print("Pause")
                game.movement = False
                pause = True

            if game.menu == False and game.option == False and pause == True and replay_button_rect.collidepoint(
                    event.pos):
                print("Fin de la pause")
                game.movement = True
                pause = False

            if game.menu == False and game.option == False and menu_button_rect.collidepoint(event.pos):
                print("Menu")
                game.game_over()
                game.new_score_add()

            if game.menu == True and game.option == False and game.is_playing == False and quit_button_rect.collidepoint(
                    event.pos):
                print("Fin du programme")
                pygame.quit()
                running = False
