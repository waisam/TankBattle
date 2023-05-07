from enum import Enum


class EnemyType(Enum):
    """敌方坦克的类型和属性
    """
    BASIC = {
        'health': 1,
        'speed_ratio': 1,
        'fire_ratio': 1,
        'bullet_speed_ratio': 1,
        'point': 100
    }
    FAST = {
        'health': 1,
        'speed_ratio': 3,
        'fire_ratio': 2,
        'bullet_speed_ratio': 1,
        'point': 200
    }
    POWER = {
        'health': 1,
        'speed_ratio': 2,
        'fire_ratio': 3,
        'bullet_speed_ratio': 1,
        'point': 300
    }
    ARMOR = {
        'health': 4,
        'speed_ratio': 2,
        'fire_ratio': 2,
        'bullet_speed_ratio': 1,
        'point': 400
    }


class Direction(Enum):
    """坦克朝向
    """
    UP = 'up'
    DOWN = 'down'
    LEFT = 'left'
    RIGHT = 'right'
