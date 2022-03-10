################### Scope ####################

enemies = 1


def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")


# local Scope
def drink_potion():
    potion_strength = 20
    print(potion_strength)


drink_potion()

# Global Scope

player_health = 10


def drink_potion():
    potion_strength = 20
    print(player_health)


drink_potion()

# Modifying global variables option 1
enemies = 1


def increase_enemies():
    global enemies
    enemies = 2
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")

# Modifying global variables option 2
enemies = 1


def increase_enemies():
    print(f"enemies inside function: {enemies}")
    return enemies + 1


enemies = increase_enemies()
print(f"enemies outside function: {enemies}")

# Global Constants
PI = 3.14159
URL="http://www.github.com"
