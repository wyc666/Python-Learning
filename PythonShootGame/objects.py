# -*- coding: utf-8 -*-
import pygame,config

class Bullet(pygame.sprite.Sprite):
    def __init__(self, bullet_img, init_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_img
        self.rect = self.image.get_rect()
        self.rect.midbottom = init_pos
        self.speed = 10

    def move(self):
        self.rect.top -= self.speed

class Plane(pygame.sprite.Sprite):
    def __init__(self, plane_img, plane_explode_img, init_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = plane_img
        self.explode_image = plane_explode_img
        self.rect = (self.image)[0].get_rect()
        self.rect.topleft = init_pos
        self.speed = 16
        self.bullets = pygame.sprite.Group()
        self.image_index = 0
        self.is_hit = False

    def moveUp(self):
        if self.rect.top <= 0:
            self.rect.top = 0
        else:
            self.rect.top -= self.speed

    def moveDown(self):
        screen_height = (config.get_screen_pixel())[1]
        if self.rect.bottom >= screen_height:
            self.rect.bottom = screen_height
        else:
            self.rect.bottom += self.speed

    def moveLeft(self):
        if self.rect.left <= 0:
            self.rect.left = 0
        else:
            self.rect.left -= self.speed

    def moveRight(self):
        screen_width = (config.get_screen_pixel())[0]
        if self.rect.right >= screen_width:
            self.rect.right = screen_width
        else:
            self.rect.right += self.speed

    def shoot(self, bullet_img):
        bullet = Bullet(bullet_img, self.rect.midtop)
        self.bullets.add(bullet)

class Enemy(pygame.sprite.Sprite):
    def __init__(self, enemy_img, enemy_explode_img, init_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = enemy_img
        self.explode_image = enemy_explode_img
        self.rect = self.image.get_rect()
        self.rect.topleft = init_pos
        self.speed = 2
        self.explode_index = 0

    def move(self):
        self.rect.top += self.speed