# Import the random library to use for the dice later
import random

# Define Variables
numLives = 10           # number of player's lives remaining
mNumLives = 12          # number of monster's lives remaining

# Use list() and range() to create a list of dice values ([1, 2, 3, 4, 5, 6])
diceOptions = list(range(1, 7))
print("Dice Options:", diceOptions)

# TODO: Use a for loop with the in keyword to iterate over the weapons array and display the available weapons to the player.
weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear Bomb"]
print("Available weapons:")

i = 1
for w in weapons:
    print(f"{i}. {w}")
    i += 1

# Input and validation for combat strengths
combatStrength = input("Enter your combat Strength (1-6): ")
isValid = combatStrength.isnumeric() and 1 <= int(combatStrength) <= 6

while not isValid:
    print("Input must be a number between 1-6.")
    combatStrength = input("Enter your combat Strength (1-6): ")
    isValid = combatStrength.isnumeric() and 1 <= int(combatStrength) <= 6

combatStrength = int(combatStrength)

mCombatStrength = input("Enter the monster's combat Strength (1-6): ")
isValid = mCombatStrength.isnumeric() and 1 <= int(mCombatStrength) <= 6

while not isValid:
    print("Input must be a number between 1-6.")
    mCombatStrength = input("Enter the monster's combat Strength (1-6): ")
    isValid = mCombatStrength.isnumeric() and 1 <= int(mCombatStrength) <= 6

mCombatStrength = int(mCombatStrength)

# Simulate a battle with 10 rounds
for round_num in range(1, 21, 2):
    print(f"\nRound {round_num}:")

    # Roll dice for hero and monster
    hero_roll = random.choice(diceOptions)
    monster_roll = random.choice(diceOptions)

    # Update combat strengths
    hero_total_strength = combatStrength + hero_roll
    monster_total_strength = mCombatStrength + monster_roll

    # Announce selected weapons
    hero_weapon = weapons[hero_roll - 1]
    monster_weapon = weapons[monster_roll - 1]

    print(f"Hero rolled {hero_roll}, Monster rolled {monster_roll}.")
    print(f"Hero selected: {hero_weapon}, Monster selected: {monster_weapon}.")
    print(f"Hero Total Strength: {hero_total_strength}, Monster Total Strength: {monster_total_strength}.")

    # Determine the winner of the round
    if hero_total_strength > monster_total_strength:
        print("Hero wins the round!")
    elif hero_total_strength < monster_total_strength:
        print("Monster wins the round!")
    else:
        print("It's a tie!")

    # Break condition for round 11
    if round_num == 11:
        print("\nBattle Truce declared in Round 11. Game Over!")
        break
