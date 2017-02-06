# -*- coding: UTF-8 -*-
import objects,pygame,config,random

def start_game():
    pygame.init()

    # 屏幕像素大小获取
    screen_pixel = config.get_screen_pixel()
    screen_width = screen_pixel[0]
    screen_height = screen_pixel[1]
    screen = pygame.display.set_mode((screen_width, screen_height))

    # 图片获取(背景、游戏结束、需要裁剪的混合图)
    bg_img = pygame.image.load(config.get_img_path("background")).convert()
    game_over_img = pygame.image.load(config.get_img_path("gameover"))
    plane_img = pygame.image.load(config.get_img_path("shoot"))

    # 初始化玩家对象
    # 裁剪正常情况下飞机图片
    plane_imgs = []
    plane_imgs_pos = config.get_plane_imgs_pos()
    for plane_img_pos in plane_imgs_pos:
        rect = pygame.Rect(plane_img_pos[0], plane_img_pos[1], plane_img_pos[2], plane_img_pos[3])
        plane_imgs.append(plane_img.subsurface(rect).convert_alpha())
    # 裁剪碰撞情况下飞机图片
    plane_explode_imgs = []
    plane_explode_imgs_pos = config.get_plane_explode_imgs_pos()
    for plane_explode_img_pos in plane_explode_imgs_pos:
        rect = pygame.Rect(plane_explode_img_pos[0], plane_explode_img_pos[1], plane_explode_img_pos[2], plane_explode_img_pos[3])
        plane_explode_imgs.append(plane_img.subsurface(rect).convert_alpha())
    # 创建对象
    plane_init_pos = config.get_plane_init_pos()
    plane = objects.Plane(plane_imgs, plane_explode_imgs, plane_init_pos)

    # 裁剪子弹图片
    bullet_pos = config.get_bullet_pos()
    bullet_rect = pygame.Rect(bullet_pos[0], bullet_pos[1], bullet_pos[2], bullet_pos[3])
    bullet_img = plane_img.subsurface(bullet_rect)

    # 裁剪敌机图片
    # 正常情况下
    enemy_pos = config.get_enemy_img_pos()
    enemy_rect = pygame.Rect(enemy_pos[0], enemy_pos[1], enemy_pos[2], enemy_pos[3])
    enemy_img = plane_img.subsurface(enemy_rect).convert_alpha()
    # 被击落后
    enemy_explode_imgs = []
    enemy_explode_imgs_pos = config.get_enemy_explode_imgs_pos()
    for explode_img_pos in enemy_explode_imgs_pos:
        rect = pygame.Rect(explode_img_pos[0], explode_img_pos[1], explode_img_pos[2], explode_img_pos[3])
        explode_img = plane_img.subsurface(rect)
        enemy_explode_imgs.append(explode_img)

    # 精灵分组
    enemies = pygame.sprite.Group()
    enemies_explode = pygame.sprite.Group()

    # 各种游戏数据
    score = 0
    bullet_frequency = 0
    enemy_frequency = 0
    plane_explode_frequency = 32
    running = True

    # 时钟设置
    clock = pygame.time.Clock()

    # 游戏主逻辑
    while running:
        clock.tick(60)

        if not plane.is_hit:
            # 射击子弹
            bullet_frequency += 1
            if bullet_frequency == 30:
                plane.shoot(bullet_img)
                bullet_frequency = 0

            # 添加敌机
            enemy_frequency += 1
            if enemy_frequency % 50 == 0:
                enemy_pos = [random.randint(0, screen_width - enemy_rect.width), 0]
                enemy = objects.Enemy(enemy_img, enemy_explode_imgs, enemy_pos)
                enemies.add(enemy)
                enemy_frequency = 0

        # 子弹移动
        for bullet in plane.bullets:
            bullet.move()
            if bullet.rect.bottom < 0:
                plane.bullets.remove(bullet)

        # 判断被子弹击中的敌机
        enemies_explode_by_bullet = pygame.sprite.groupcollide(enemies, plane.bullets, 1, 1)
        for enemy_explode_by_bullet in enemies_explode_by_bullet:
            enemies_explode.add(enemy_explode_by_bullet)

        # 判断玩家是否与敌机相撞
        for enemy in enemies:
            enemy.move()
            if pygame.sprite.collide_circle(enemy, plane):
                enemies_explode.add(enemy)
                enemies.remove(enemy)
                plane.is_hit = True
            if enemy.rect.top > screen_height:
                enemies.remove(enemy)

        screen.fill(0)
        screen.blit(bg_img, (0, 0))

        # 更新玩家飞机照片，产生动态效果
        # 未发生碰撞
        if not plane.is_hit:
            plane.image_index = bullet_frequency / 16
            screen.blit(plane.image[plane.image_index], plane.rect)
        # 撞上敌机
        else:
            plane.image_index = plane_explode_frequency / 16
            screen.blit(plane.image[plane.image_index], plane.rect)
            plane_explode_frequency += 1
            if plane_explode_frequency == 96:
                running = False

        # 更新被击毁敌机的图片，产生爆炸效果
        for enemy_explode in enemies_explode:
            if enemy_explode.explode_index >= 16:
                score += 100
                enemies_explode.remove(enemies_explode)
                continue
            else:
                enemy_explode_index = enemy_explode.explode_index / 4
                screen.blit(enemy_explode_imgs[enemy_explode_index], enemy_explode.rect)
                enemy_explode.explode_index += 1

        plane.bullets.draw(screen)
        enemies.draw(screen)
        # 屏幕显示分数
        score_font = pygame.font.Font(None, 36)
        score_text = score_font.render(str(score), True, (128, 128, 128))
        text_rect = score_text.get_rect()
        text_rect.topleft = [10, 10]
        screen.blit(score_text, text_rect)

        # 刷新屏幕
        pygame.display.update()

        # 监听玩家控制飞机
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    plane.moveLeft()
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    plane.moveRight()
                elif event.key == pygame.K_w or event.key == pygame.K_UP:
                    plane.moveUp()
                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    plane.moveDown()

    # 游戏结束，显示用户所得分数
    font = pygame.font.Font(None, 48)
    text = font.render('Score: ' + str(score), True, (255, 0, 0))
    text_rect = text.get_rect()
    text_rect.centerx = screen.get_rect().centerx
    text_rect.centery = screen.get_rect().centery + 24
    screen.blit(game_over_img, (0, 0))
    screen.blit(text, text_rect)

start_game()