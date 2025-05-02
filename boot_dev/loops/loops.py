"""
regenerate function
"""

def regenerate(current_health, max_health, enemy_distance):

    while current_health < max_health:

        if enemy_distance <= 3:
            return current_health

        current_health += 1
        enemy_distance -= 2
    return current_health