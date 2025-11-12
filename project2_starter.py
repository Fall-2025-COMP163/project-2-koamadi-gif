import random # Used by Rogue for the random chance of a critical hit
"""
COMP 163 - Project 2: Character Abilities Showcase
Name: Kobby Amadi
Date: 11/14/25

AI Usage: Google Gemini helped with debugging and making code adjustments to fulfill test cases.
Example: AI helped with inheritance structure and method overriding concepts
"""

# ============================================================================
# PROVIDED BATTLE SYSTEM (DO NOT MODIFY)
# ============================================================================

class SimpleBattle:
    """
    Simple battle system provided for testing character interactions.
    You can use this to simulate fights between two characters.
    """

    def __init__(self, character1, character2):
        """
        Constructor that initializes a battle between two character objects.

        Parameters:
        - character1: The first character (attacker/defender)
        - character2: The second character (opponent)
        """
        self.char1 = character1
        self.char2 = character2

    def fight(self):
        """Simulates one round of combat between the two characters."""
        # Print header showing which characters are battling
        print(f"\n=== BATTLE: {self.char1.name} vs {self.char2.name} ===")
        
        # Display the starting statistics for both characters
        print("\nStarting Stats:")
        self.char1.display_stats()
        self.char2.display_stats()
        
        # Begin Round 1
        print(f"\n--- Round 1 ---")
        
        # Character 1 attacks first
        print(f"{self.char1.name} attacks:")
        self.char1.attack(self.char2)
        
        # If Character 2 is still alive after attack, they retaliate
        if self.char2.health > 0:
            print(f"\n{self.char2.name} attacks:")
            self.char2.attack(self.char1)
        
        # Display post-battle results (remaining health, etc.)
        print(f"\n--- Battle Results ---")
        self.char1.display_stats()
        self.char2.display_stats()
        
        # Determine the winner based on who has more health left
        if self.char1.health > self.char2.health:
            print(f"🏆 {self.char1.name} wins!")
        elif self.char2.health > self.char1.health:
            print(f"🏆 {self.char2.name} wins!")
        else:
            print("🤝 It's a tie!")


# ============================================================================
# BASE CHARACTER CLASSES
# ============================================================================

class Character:
    """Base class representing any character in the game."""

    def __init__(self, name, health, strength, magic):
        """
        Initializes basic character attributes.

        Parameters:
        - name (str): Character’s name
        - health (int): Character’s current health points
        - strength (int): Determines physical attack damage
        - magic (int): Determines magical power or magic-based damage
        """
        self.name = name
        self.health = health
        self.strength = strength
        self.magic = magic

    def attack(self, target):
        """
        Performs a standard physical attack using strength.
        The target’s health is reduced by 'damage'.
        """
        damage = self.strength
        print(f"{self.name} attacks {target.name} for {damage} damage!")
        target.take_damage(damage)

    def take_damage(self, damage):
        """
        Reduces health by the damage received.
        Prevents health from dropping below zero.
        """
        self.health -= damage
        if self.health < 0:
            self.health = 0  # Clamp health at 0 so it doesn't go negative
        print(f"{self.name} takes {damage} damage! Health is now {self.health}.")

    def display_stats(self):
        """Displays character's current name, health, strength, and magic."""
        print(f"{self.name} | Health: {self.health} | Strength: {self.strength} | Magic: {self.magic}")


# ============================================================================
# PLAYER CLASSES (Derived from Character)
# ============================================================================

class Player(Character):
    """Base class for all player-controlled characters."""

    def __init__(self, name, character_class, health, strength, magic):
        """
        Initializes a player with character-specific data and extra stats.

        Adds:
        - character_class (str): Class name (e.g., Warrior, Mage)
        - level (int): Player level (starts at 1)
        - experience (int): Experience points (starts at 0)
        """
        super().__init__(name, health, strength, magic)
        self.character_class = character_class
        self.level = 1
        self.experience = 0

    def display_stats(self):
        """Displays base character stats plus class, level, and experience."""
        super().display_stats()  # Call base method to print general stats
        print(f"Class: {self.character_class} | Level: {self.level} | EXP: {self.experience}")


# ============================================================================
# SPECIFIC CHARACTER CLASSES
# ============================================================================

class Warrior(Player):
    """A powerful melee fighter with high strength and health."""

    def __init__(self, name):
        """
        Creates a Warrior with predefined attributes:
        - Health: 120 (high endurance)
        - Strength: 15 (strong attacks)
        - Magic: 5 (minimal magic power)
        """
        super().__init__(name, "Warrior", health=120, strength=15, magic=5)

    def attack(self, target):
        """
        Overrides base attack method.
        Adds +5 bonus to strength-based attacks.
        """
        damage = self.strength + 5
        print(f"{self.name} swings a mighty sword at {target.name} for {damage} damage!")
        target.take_damage(damage)

    def power_strike(self, target):
        """
        Special ability that delivers a stronger attack.
        Deals strength + 15 damage.
        """
        damage = self.strength + 15
        print(f"{self.name} performs a POWER STRIKE on {target.name} for {damage} damage!")
        target.take_damage(damage)


# ----------------------------------------------------------------------------

class Mage(Player):
    """A master of magical attacks with high magic power."""

    def __init__(self, name):
        """
        Creates a Mage with predefined attributes:
        - Health: 80 (low endurance)
        - Strength: 8 (weak physically)
        - Magic: 20 (strong magic attacks)
        """
        super().__init__(name, "Mage", health=80, strength=8, magic=20)

    def attack(self, target):
        """
        Overrides attack method to perform a magic-based attack.
        Damage is based entirely on the 'magic' stat.
        """
        damage = self.magic
        print(f"{self.name} casts a spell on {target.name} for {damage} magic damage!")
        target.take_damage(damage)

    def fireball(self, target):
        """
        Special ability that deals even higher magic damage.
        Deals magic + 10 damage.
        """
        damage = self.magic + 10
        print(f"{self.name} launches a FIREBALL at {target.name} for {damage} damage!")
        target.take_damage(damage)


# ----------------------------------------------------------------------------

class Rogue(Player):
    """A stealthy and agile fighter who excels at critical hits."""

    def __init__(self, name):
        """
        Creates a Rogue with moderate stats:
        - Health: 90
        - Strength: 12
        - Magic: 10
        """
        super().__init__(name, "Rogue", health=90, strength=12, magic=10)

    def attack(self, target):
        """
        Attack with a random chance of critical hit.
        Critical hit = double damage (30% chance).
        """
        crit_chance = random.randint(1, 10)  # Generate random number 1–10
        if crit_chance <= 3:  # 3 out of 10 chance = 30%
            damage = self.strength * 2
            print(f"Critical hit! {self.name} strikes {target.name} for {damage} damage!")
        else:
            damage = self.strength
            print(f"{self.name} attacks {target.name} for {damage} damage.")
        target.take_damage(damage)

    def sneak_attack(self, target):
        """
        Special Rogue ability.
        Guaranteed critical hit that deals double damage.
        """
        damage = self.strength * 2
        print(f"{self.name} performs a SNEAK ATTACK on {target.name} for {damage} damage!")
        target.take_damage(damage)


# ============================================================================
# WEAPON CLASS (Example of Composition)
# ============================================================================

class Weapon:
    """
    Represents a weapon that can be equipped by a character.
    Demonstrates composition: a character HAS a weapon.
    """

    def __init__(self, name, damage_bonus):
        """
        Initializes weapon attributes.
        - name (str): The weapon's name (e.g., "Longsword")
        - damage_bonus (int): Additional damage provided by the weapon
        """
        self.name = name
        self.damage_bonus = damage_bonus

    def display_info(self):
        """Prints weapon name and bonus damage."""
        print(f"Weapon: {self.name} | Damage Bonus: +{self.damage_bonus}")

# ============================================================================
# MAIN PROGRAM FOR TESTING (YOU CAN MODIFY THIS FOR TESTING)
# ============================================================================

if __name__ == "__main__":
    print("=== CHARACTER ABILITIES SHOWCASE ===")
    print("Testing inheritance, polymorphism, and method overriding")
    print("=" * 50)
    
    # TODO: Create one of each character type
    # warrior = Warrior("Sir Galahad")
    # mage = Mage("Merlin")
    # rogue = Rogue("Robin Hood")
    
    # TODO: Display their stats
    # print("\n📊 Character Stats:")
    # warrior.display_stats()
    # mage.display_stats()
    # rogue.display_stats()
    
    # TODO: Test polymorphism - same method call, different behavior
    # print("\n⚔️ Testing Polymorphism (same attack method, different behavior):")
    # dummy_target = Character("Target Dummy", 100, 0, 0)
    # 
    # for character in [warrior, mage, rogue]:
    #     print(f"\n{character.name} attacks the dummy:")
    #     character.attack(dummy_target)
    #     dummy_target.health = 100  # Reset dummy health
    
    # TODO: Test special abilities
    # print("\n✨ Testing Special Abilities:")
    # target1 = Character("Enemy1", 50, 0, 0)
    # target2 = Character("Enemy2", 50, 0, 0)
    # target3 = Character("Enemy3", 50, 0, 0)
    # 
    # warrior.power_strike(target1)
    # mage.fireball(target2)
    # rogue.sneak_attack(target3)
    
    # TODO: Test composition with weapons
    # print("\n🗡️ Testing Weapon Composition:")
    # sword = Weapon("Iron Sword", 10)
    # staff = Weapon("Magic Staff", 15)
    # dagger = Weapon("Steel Dagger", 8)
    # 
    # sword.display_info()
    # staff.display_info()
    # dagger.display_info()
    
    # TODO: Test the battle system
    # print("\n⚔️ Testing Battle System:")
    # battle = SimpleBattle(warrior, mage)
    # battle.fight()
    
    print("\n✅ Testing complete!")
