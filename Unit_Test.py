import objects
import main
import pygame
import pytest

def test_var_PlayerSpaceShip():
    """ Test des variables de la class PlayerSpaceShip : """
    my_PlayerSpaceShip = objects.PlayerSpaceShip(sprite=pygame.Surface([10, 10]), x=10, y=4)
    assert type(my_PlayerSpaceShip.sprite) is int or float
    assert type(my_PlayerSpaceShip.x) is int or float
    assert type(my_PlayerSpaceShip.y) is int or float
    assert type(my_PlayerSpaceShip.angle_inertie) is int or float
    assert type(my_PlayerSpaceShip.vitesse) is int or float
    assert type(my_PlayerSpaceShip.acceleration) is int or float
    assert type(my_PlayerSpaceShip.size) is int or float
    assert type(my_PlayerSpaceShip.life) is int or float
    assert type(my_PlayerSpaceShip.shoot_rate) is int or float
    assert type(my_PlayerSpaceShip.type) is int or float
    assert my_PlayerSpaceShip.x == 10
    assert my_PlayerSpaceShip.y == 4


def test_var_Asteroids():
    """Test des variables de la class Asteroids : """
    my_Asteroids = objects.Asteroid(sprite=pygame.Surface([10, 10]), window_size=[10,20], asteroid_type=1, x=None, y=None)
    assert type(my_Asteroids.type) is int
    assert type(my_Asteroids.vitesse) is int
    assert type(my_Asteroids.size) is int or float
    assert type(my_Asteroids.angle) is int
    """Test que le randint donne bien un nombre random entre 0 et window_size quand X=None et y=None"""
    assert my_Asteroids.x in range(11)
    assert my_Asteroids.y in range(21)
    my_Asteroids2 = objects.Asteroid(sprite=pygame.Surface([10, 10]), window_size=[100,200], asteroid_type=1, x=10, y=20)
    assert type(my_Asteroids2.type) is int
    assert type(my_Asteroids2.vitesse) is int
    assert type(my_Asteroids2.size) is int or float
    assert type(my_Asteroids2.angle) is int
    """Test que x=x et y=y quand x!=None ety!=None """
    assert my_Asteroids2.x == 10
    assert my_Asteroids2.y == 20


"""def test_var_Game():
    debut = main.Game()
    assert type (debut.score) is int
    assert type (debut.level) is int
    assert type (debut.window_size) is int
    assert type (debut.sprites_list) is str
"""
"""
def test_StartLevel():
    debutpartie = main.StartLevel (coucou, [3]/12,[5]/3)
    assert debutpartie.sprites_list = coucou
"""
