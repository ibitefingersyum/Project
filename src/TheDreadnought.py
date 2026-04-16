import pygame
import random
import map
import health
import movement
import vision
import projectiles
import player
import enemies
import hud
import ui

# This class acts as a game manager

class TheDreadnought:
    def __init__(self):
        pygame.init()
        self.gameDisplay = pygame.display.set_mode((map.display_width, map.display_height))
        pygame.display.set_caption('The Dreadnought')
        self.clock = pygame.time.Clock()
        self.running = True
        self.player = player.Player()
        self.enemies = enemies.Enemies()
        self.hud = hud.HUD(self.player)
        self.ui = ui.UI(self.player)

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # Update game state
            movement.handle_movement(self.player)
            vision.handle_vision(self.player, self.enemies)
            projectiles.handle_projectiles(self.player, self.enemies)

            # Draw everything
            self.gameDisplay.fill((0, 0, 0))  # Clear screen
            self.player.draw(self.gameDisplay)
            self.enemies.draw(self.gameDisplay)
            self.hud.draw(self.gameDisplay)
            self.ui.draw(self.gameDisplay)

            pygame.display.update()
            self.clock.tick(60)  # Limit to 60 FPS

        pygame.quit()