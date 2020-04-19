import objects
import main

def test_var_PlayerSpaceShip():
    """ Test des variables de la class PlayerSpaceShip : """
    my_PlayerSpaceShip = objects.PlayerSpaceShip(sprite=2, x=10, y=4)
    assert type(my_PlayerSpaceShip.sprite) is int or float
    assert type(my_PlayerSpaceShip.x) is int or float
    assert type(my_PlayerSpaceShip.y) is int or float
    assert type(my_PlayerSpaceShip.angle) is int or float
    assert type(my_PlayerSpaceShip.speed) is int or float
    assert type(my_PlayerSpaceShip.acceleration) is int or float
    assert type(my_PlayerSpaceShip.size) is int or float
    assert type(my_PlayerSpaceShip.life) is int or float
    assert type(my_PlayerSpaceShip.shoot_rate) is int or float
    assert type(my_PlayerSpaceShip.type) is int or float
    assert my_PlayerSpaceShip.sprite == 2
    assert my_PlayerSpaceShip.x == 10
    assert my_PlayerSpaceShip.y == 4

def test_var_Game():
    debut = main.Game()
    assert type (debut.score) is int
    assert type (debut.level) is int
    assert type (debut.window_size) is int
    assert type (debut.sprites_list) is string
    
def test_StartLevel():
    debutpartie = main.StartLevel (coucou, [3]/12,[5]/3)
    assert debutpartie.sprites_list = coucou
