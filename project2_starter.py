import random  # Used for Rogue's critical hit chance

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
        self.char1 = character1  # Store first character
        self.char2 = character2  # Store second character

    def fight(self):
        """Simulates one round of combat between the two characters."""
        # Print battle title using character names
        print(f"\n=== BATTLE: {self.char1.name} vs {self.char2.name} ===")
        
        # Print starting stats for both characters
        print("\nStarting Stats:")
        self.char1.display_stats()  # Show stats of character 1
        self.char2.display_stats()  # Show stats of character 2
        
        # Round header
        print(f"\n--- Round 1 ---")
        
        # Character 1 attacks first
        print(f"{self.char1.name} attacks:")
        self.char1.attack(self.char2)  # char1 deals damage to char2
        
        # Character 2 attacks only if not defeated
        if self.char2.health > 0:
            print(f"\n{self.char2.name} attacks:")
            self.char2.attack(self.char1)  # char2 deals damage to char1
        
        # Print stats after the battle round
        print(f"\n--- Battle Results ---")
        self.char1.display_stats()
        self.char2.display_stats()
        
        # Determine the winner based on remaining health
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
        """
        self.name = name      # Character's name
        self.health = health  # Current health points
        self.strength = strength  # Determines physical attack damage
        self.magic = magic        # Determines magical attack power

    def attack(self, target):
        """
        Performs a standard physical attack using strength.
        """
        damage = self.strength  # Damage equals character's strength stat
        print(f"{self.name} attacks {target.name} for {damage} damage!")
        target.take_damage(damage)  # Apply damage to target

    def take_damage(self, damage):
        """
        Reduces health by the damage received.
        Prevents health from dropping below zero.
        """
        self.health -= damage  # Subtracts incoming damage
        if self.health < 0:    # Stop health from going negative
            self.health = 0
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
        """
        super().__init__(name, health, strength, magic)  # Initialize base Character fields
        self.character_class = character_class  # Class type (Warrior, Mage, Rogue)
        self.level = 1      # Starting level
        self.experience = 0 # Starting experience points

    def display_stats(self):
        """Displays base character stats plus class, level, and experience."""
        super().display_stats()  # Print Character stats
        print(f"Class: {self.character_class} | Level: {self.level} | EXP: {self.experience}")


# ============================================================================
# SPECIFIC CHARACTER CLASSES
# ============================================================================

class Warrior(Player):
    """A powerful melee fighter with high strength and health."""

    def __init__(self, name):
        """
        Creates a Warrior with predefined stats.
        """
        super().__init__(name, "Warrior", health=120, strength=15, magic=5)

    def attack(self, target):
        """
        Overrides attack to add extra melee damage.
        """
        damage = self.strength + 5  # Warrior bonus damage
        print(f"{self.name} swings a mighty sword at {target.name} for {damage} damage!")
        target.take_damage(damage)

    def power_strike(self, target):
        """
        Special ability that deals heavy physical damage.
        """
        damage = self.strength + 15  # Stronger attack
        print(f"{self.name} performs a POWER STRIKE on {target.name} for {damage} damage!")
        target.take_damage(damage)


# ----------------------------------------------------------------------------

class Mage(Player):
    """A master of magical attacks with high magic power."""

    def __init__(self, name):
        """
        Creates a Mage with predefined stats.
        """
        super().__init__(name, "Mage", health=80, strength=8, magic=20)

    def attack(self, target):
        """
        Overrides attack to use magic instead of strength.
        """
        damage = self.magic  # Magic-based damage
        print(f"{self.name} casts a spell on {target.name} for {damage} magic damage!")
        target.take_damage(damage)

    def fireball(self, target):
        """
        Special high-damage magic attack.
        """
        damage = self.magic + 10  # Stronger magic attack
        print(f"{self.name} launches a FIREBALL at {target.name} for {damage} damage!")
        target.take_damage(damage)


# ----------------------------------------------------------------------------

class Rogue(Player):
    """A stealthy and agile fighter who excels at critical hits."""

    def __init__(self, name):
        """
        Creates a Rogue with predefined stats.
        """
        super().__init__(name, "Rogue", health=90, strength=12, magic=10)

    def attack(self, target):
        """
        Attack with a random chance of critical hit.
        Critical hit = double damage (30% chance).
        """
        crit_chance = random.randint(1, 10)  # Random value for critical hit chance
        if crit_chance <= 3:  # Critical hit threshold
            damage = self.strength * 2  # Double damage
            print(f"Critical hit! {self.name} strikes {target.name} for {damage} damage!")
        else:
            damage = self.strength  # Normal damage
            print(f"{self.name} attacks {target.name} for {damage} damage.")
        target.take_damage(damage)

    def sneak_attack(self, target):
        """
        Rogue special ability: guaranteed critical hit.
        """
        damage = self.strength * 2  # Always double damage
        print(f"{self.name} performs a SNEAK ATTACK on {target.name} for {damage} damage!")
        target.take_damage(damage)


# ============================================================================
# WEAPON CLASS (Example of Composition)
# ============================================================================

class Weapon:
    """
    Represents a weapon that can be equipped by a character.
    """

    def __init__(self, name, damage_bonus):
        """
        Initializes weapon with name and damage bonus.
        """
        self.name = name              # Weapon name
        self.damage_bonus = damage_bonus  # Bonus damage provided

    def display_info(self):
        """Prints weapon details."""
        print(f"Weapon: {self.name} | Damage Bonus: +{self.damage_bonus}")
# ============================================================================
# MAIN PROGRAM FOR TESTING (YOU CAN MODIFY THIS FOR TESTING)
# ============================================================================

if __name__ == "__main__":
    print("=== CHARACTER ABILITIES SHOWCASE ===")
    print("Testing inheritance, polymorphism, and method overriding")
    print("=" * 50)
    
    # Create characters
    warrior = Warrior("Sir Galahad")
    mage = Mage("Merlin")
    rogue = Rogue("Robin Hood")
    
    # Display stats
    print("\n📊 Character Stats:")
    warrior.display_stats()
    mage.display_stats()
    rogue.display_stats()
    
    # Polymorphism test — all use attack(), but behavior varies
    print("\n⚔️ Testing Polymorphism (same attack method, different behavior):")
    dummy_target = Character("Target Dummy", 100, 0, 0)
    
    for character in [warrior, mage, rogue]:
        print(f"\n{character.name} attacks the dummy:")
        character.attack(dummy_target)
        dummy_target.health = 100  # Reset
    
    # Special abilities
    print("\n✨ Testing Special Abilities:")
    target1 = Character("Enemy1", 50, 0, 0)
    target2 = Character("Enemy2", 50, 0, 0)
    target3 = Character("Enemy3", 50, 0, 0)
    
    warrior.power_strike(target1)
    mage.fireball(target2)
    rogue.sneak_attack(target3)
    
    # Weapon composition
    print("\n🗡️ Testing Weapon Composition:")
    sword = Weapon("Iron Sword", 10)
    staff = Weapon("Magic Staff", 15)
    dagger = Weapon("Steel Dagger", 8)
    
    sword.display_info()
    staff.display_info()
    dagger.display_info()
    
    # Battle system test
    print("\n⚔️ Testing Battle System:")
    battle = SimpleBattle(warrior, mage)
    battle.fight()
    
    print("\n✅ Testing complete!")
