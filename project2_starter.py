"""
COMP 163 - Project 2: Character Abilities Showcase
Name: Kobby Amadi
Date: [Date]

AI Usage: [Document any AI assistance used]
Example: AI helped with inheritance structure and method overriding concepts
"""

# ============================================================================
# PROVIDED BATTLE SYSTEM (DO NOT MODIFY)
# ============================================================================

class SimpleBattle:
    """
    Simple battle system provided for you to test your characters.
    DO NOT MODIFY THIS CLASS - just use it to test your character implementations.
    """
    
    def __init__(self, character1, character2):
        self.char1 = character1
        self.char2 = character2
    
    def fight(self):
        """Simulates a simple battle between two characters"""
        print(f"\n=== BATTLE: {self.char1.name} vs {self.char2.name} ===")
        
        # Show starting stats
        print("\nStarting Stats:")
        self.char1.display_stats()
        self.char2.display_stats()
        
        print(f"\n--- Round 1 ---")
        print(f"{self.char1.name} attacks:")
        self.char1.attack(self.char2)
        
        if self.char2.health > 0:
            print(f"\n{self.char2.name} attacks:")
            self.char2.attack(self.char1)
        
        print(f"\n--- Battle Results ---")
        self.char1.display_stats()
        self.char2.display_stats()
        
        if self.char1.health > self.char2.health:
            print(f"🏆 {self.char1.name} wins!")
        elif self.char2.health > self.char1.health:
            print(f"🏆 {self.char2.name} wins!")
        else:
            print("🤝 It's a tie!")

# ============================================================================
# YOUR CLASSES TO IMPLEMENT (6 CLASSES TOTAL)
# ============================================================================

import random

class Character:
    """Base class for all characters."""

    def __init__(self, name, health, strength, magic):
        self.name = name
        self.health = health
        self.strength = strength
        self.magic = magic

    def attack(self, target):
        """Basic attack: damage based on strength."""
        damage = self.strength
        print(f"{self.name} attacks {target.name} for {damage} damage!")
        target.take_damage(damage)

    def take_damage(self, damage):
        """Reduce health by damage, not below 0."""
        self.health -= damage
        if self.health < 0:
            self.health = 0
        print(f"{self.name} takes {damage} damage! Health is now {self.health}.")

    def display_stats(self):
        """Print name, health, strength, and magic."""
        print(f"{self.name} | Health: {self.health} | Strength: {self.strength} | Magic: {self.magic}")


# ----------------------------------------------------------------------------
class Player(Character):
    """Base class for player-controlled characters."""

    def __init__(self, name, character_class, health, strength, magic):
        super().__init__(name, health, strength, magic)
        self.character_class = character_class
        self.level = 1
        self.experience = 0

    def display_stats(self):
        """Show basic + player-specific info."""
        super().display_stats()
        print(f"Class: {self.character_class} | Level: {self.level} | EXP: {self.experience}")


# ----------------------------------------------------------------------------
class Warrior(Player):
    """Strong physical fighter."""

    def __init__(self, name):
        super().__init__(name, "Warrior", health=120, strength=15, magic=5)

    def attack(self, target):
        """Powerful melee attack."""
        damage = self.strength + 5
        print(f"{self.name} swings a mighty sword at {target.name} for {damage} damage!")
        target.take_damage(damage)

    def power_strike(self, target):
        """Special warrior ability."""
        damage = self.strength + 15
        print(f"{self.name} performs a POWER STRIKE on {target.name} for {damage} damage!")
        target.take_damage(damage)


# ----------------------------------------------------------------------------
class Mage(Player):
    """Magical spellcaster."""

    def __init__(self, name):
        super().__init__(name, "Mage", health=80, strength=8, magic=20)

    def attack(self, target):
        """Magic-based attack."""
        damage = self.magic
        print(f"{self.name} casts a spell on {target.name} for {damage} magic damage!")
        target.take_damage(damage)

    def fireball(self, target):
        """Special mage ability."""
        damage = self.magic + 10
        print(f"{self.name} launches a FIREBALL at {target.name} for {damage} damage!")
        target.take_damage(damage)


# ----------------------------------------------------------------------------
class Rogue(Player):
    """Quick and sneaky fighter."""

    def __init__(self, name):
        super().__init__(name, "Rogue", health=90, strength=12, magic=10)

    def attack(self, target):
        """Attack with chance of critical hit."""
        crit_chance = random.randint(1, 10)
        if crit_chance <= 3:
            damage = self.strength * 2
            print(f"💥 Critical hit! {self.name} strikes {target.name} for {damage} damage!")
        else:
            damage = self.strength
            print(f"{self.name} attacks {target.name} for {damage} damage.")
        target.take_damage(damage)

    def sneak_attack(self, target):
        """Guaranteed critical hit."""
        damage = self.strength * 2
        print(f"🗡️ {self.name} performs a SNEAK ATTACK on {target.name} for {damage} damage!")
        target.take_damage(damage)


# ----------------------------------------------------------------------------
class Weapon:
    """Demonstrates composition (character has-a weapon)."""

    def __init__(self, name, damage_bonus):
        self.name = name
        self.damage_bonus = damage_bonus

    def display_info(self):
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
