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