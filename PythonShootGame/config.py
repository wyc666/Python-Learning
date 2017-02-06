# -*- coding: utf-8 -*-
import ConfigParser

cp = ConfigParser.SafeConfigParser()
cp.read("resources/conf/config.conf")

def get_plane_imgs_pos():
    imgs = []
    img = []
    pos_info = cp.options("plane")
    width = cp.get("pixel", "plane_width")
    height = cp.get("pixel", "plane_height")
    img_num = len(pos_info)

    for i in range(img_num):
        if (i % 2 == 0):
            img = []
            img.append(int(cp.get("plane", pos_info[i])))
        else:
            img.append(int(cp.get("plane", pos_info[i])))
            img.append(int(width))
            img.append(int(height))
            imgs.append(img)
    return imgs

def get_plane_explode_imgs_pos():
    imgs = []
    img = []
    pos_info = cp.options("plane_explode")
    width = cp.get("pixel", "plane_width")
    height = cp.get("pixel", "plane_height")
    img_num = len(pos_info)

    for i in range(img_num):
        if(i%2 == 0):
            img = []
            img.append(int(cp.get("plane_explode", pos_info[i])))
        else:
            img.append(int(cp.get("plane_explode", pos_info[i])))
            img.append(int(width))
            img.append(int(height))
            imgs.append(img)
    return imgs

def get_enemy_img_pos():
    img = []
    pos_info = cp.options("enemy")
    width = cp.get("pixel", "enemy_width")
    height = cp.get("pixel", "enemy_height")
    img_num = len(pos_info)

    for i in range(img_num):
        if (i % 2 == 0):
            img = []
            img.append(int(cp.get("enemy", pos_info[i])))
        else:
            img.append(int(cp.get("enemy", pos_info[i])))
            img.append(int(width))
            img.append(int(height))
    return img

def get_enemy_explode_imgs_pos():
    imgs = []
    img = []
    pos_info = cp.options("enemy_explode")
    width = cp.get("pixel", "enemy_width")
    height = cp.get("pixel", "enemy_height")
    img_num = len(pos_info)

    for i in range(img_num):
        if (i % 2 == 0):
            img = []
            img.append(int(cp.get("enemy_explode", pos_info[i])))
        else:
            img.append(int(cp.get("enemy_explode", pos_info[i])))
            img.append(int(width))
            img.append(int(height))
            imgs.append(img)
    return imgs

def get_screen_pixel():
    screen = []
    screen_width = cp.get("pixel", "screen_width")
    screen_height = cp.get("pixel", "screen_height")
    screen.append(int(screen_width))
    screen.append(int(screen_height))

    return screen

def get_bullet_pos():
    bullet_pos = []
    bullet_infos = cp.options("bullet")

    for bullet_info in bullet_infos:
        bullet_pos.append(int(cp.get("bullet", bullet_info)))

    return bullet_pos

def get_plane_init_pos():
    init_pos = []
    init_pos.append(int(cp.get("plane_init_pos", "x")))
    init_pos.append(int(cp.get("plane_init_pos", "y")))

    return init_pos

def get_img_path(img_name):
    path = cp.get("img_path", img_name)
    return path