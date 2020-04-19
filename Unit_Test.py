import objects

def test_cons_PlayerSpaceShip():
    """ Test des constantes de la class PlayerSpaceShip : """
    my_PlayerSpaceShip = objects.PlayerSpaceShip(sprite="Player", x=10, y=4)
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
    assert my_PlayerSpaceShip.sprite == "Player"
    assert my_PlayerSpaceShip.x == 10
    assert my_PlayerSpaceShip.y == 4
