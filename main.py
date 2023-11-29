import pygame, sys
from player import Player
from word import Word


class Game:
    def __init__(self):
        # player settings
        player_sprite = Player((screen_width / 2, screen_height), screen_width, screen_height)
        self._player = pygame.sprite.GroupSingle(player_sprite)
        
        # Game Background Music
        music = pygame.mixer.Sound('python-space-invaders/audio/music.wav')
        music.set_volume(.1)
        music.play(loops = -1)
        
        # Bullet Sound Effects
        self._bullet_sound = pygame.mixer.Sound('python-space-invaders/audio/laser.wav')
        self._bullet_sound.set_volume(.4)
        
        # word settings
        self._word = pygame.sprite.Group()
        self.word_setup(["Solid", "Liquid", "Gas", "Plasma"],rows = 1, cols = 4)

        
    # update all sprite groups
    def run(self):
        # Draw player to screen
        self._player.draw(screen)
        # Update player actions
        self._player.update()
        # Draw bullet to screen
        self._player.sprite._bullet.draw(screen)
        # self._blocks.draw(screen)
        self._word.draw(screen)
        
    def word_setup(self, word_list,rows, cols, x_distance = 120, y_distance = 48, x_offset = 70, y_offset = 100):
        
        
            for row_index, row in enumerate(range(rows)):
                for col_index, col in enumerate(range(cols)):
                    x = col_index * x_distance + x_offset
                    y = row_index * y_distance + y_offset
                    for mystery_word_loop in word_list:
                        word_sprite = Word(x, y, mystery_word_loop)
                        self._word.add(word_sprite)
                
if __name__ == '__main__':
    pygame.init()
    screen_width = 600
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()
    #create instance of the game by creating variable and assigning the class Game()
    game = Game()
    run = True
    
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        # background color of the game
        screen.fill((30, 30, 30))
        game.run()
        
        pygame.display.flip()
        # limiting the game framerate
        clock.tick(60)