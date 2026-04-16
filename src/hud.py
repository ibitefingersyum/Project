#hud
import pygame
import map
import health

class HUD:
    def __init__(self, player):
        self.player = player

    def draw(self, surface):
        # Draw health bar
        health.draw_health_bar(surface, self.player.health)