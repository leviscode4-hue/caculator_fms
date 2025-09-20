import pygame
import random

pygame.init()

screen_width= 800
screen_height= 600
screen=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("plane figting game ")

clock= pygame.time.Clock()

player_image = pygame.image.load("shipally.png")
enemy_image=player_image.load("shipenemy.png")
bullet_image= pygame.surface((8, 20))
bullet_image.fill((255, 0, 0))

class player(pygame.sprite.Sprite):
    def __init__(self):
        super(). __init__()
        self.image = player_image
       
        self.rect =self.image.get_rect.image.get_rect()
        self.rect.conterx  = screen_width // 2
        self.rect.bottom = screen_height -  20
        self.speed= 5
        self.shoot_delay= 250
        self.last_Shot = pygame.time.get_ticks()
        self.defeated= False

    def update(self):
        if self.defeated:
            return
            
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
            

        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed     
            self.rect.x = max(0, min(self.rect.x, screen_width - self.rect.width))
            now = pygame.time.get_ticks()

            if keys[pygame.K_SPACE] and now - self.last_shot > self.    delay:
                self.last_Shot= now
                bullet = Bullet(self.rect.top)
                all_sprites.add(bullet)
                bullet.add(bullet)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = enemy_image
        self.rect = self.image.get_rect()
        
        self.rect.x = random.randint(0, screen_width - self.rect.width)
        self.rect.y = random.randint(-100, -40)
        self.speed = random.randint(1, 3)

        def update(self):
            if player.defeated:
                return
        self.rect.y += self.speed
        if self.rect.top > screen_height:
            self.reset()

        if pygame.sprite.collide_rect(self, player):
            player.defeated = True

        def reset(self):
            self.rect.x = random.randint(0, screen_width - self.rect.width)
            self.rect.y =random.randint(-100, -40)
            self.speed = random.randint(1, 3)


class Bullet(pygame.sprite.Sprite) :
    def __init__(self,x,y):
        super.__init__()
        self.image = bullet_image
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speed = -10

    def update(self):
        self.rect.y += self.speed
        if self.rect.bottom < 0 :
            self.kill()

player = player()
all_sprites = pygame.sprite.Group()
all_sprites.add(player  )

enemies = pygame.sprite.group()
for _ in range(10):
    enemy = Enemy()
    all_sprites.add(enemy)
    enemies.add(enemy)

bullet = pygame.sprite.Group()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        all_sprites.update()

        hits = pygame.sprite.groupcollide(enemies,bullets, True, True)
        for hit_enemy in hits:
            enemy = Enemy()
            all_sprites.add(enemy)

        screen.fill((0, 0, 0))
        all_sprites.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()














    