#!/usr/bin/env python3
"""
Example program demonstrating all features of the animalsay package.
"""

import animalsay


def main():
    """
    Demonstrate all functions and features of the animalsay package.
    """
    print("=" * 60)
    print("🐮🐱🐶🐑 ANIMALSAY PACKAGE DEMONSTRATION 🐑🐶🐱🐮")
    print("=" * 60)
    
    # Show package information
    print(f"\n📦 PACKAGE INFO:")
    print(f"Available animals: cow, dog, cat, sheep")
    print(f"Available moods: happy, sad, neutral, angry, surprised")
    print(f"Version: {animalsay.__version__ if hasattr(animalsay, '__version__') else '0.1.0'}")
    
    # Demonstration 1: Basic usage with default parameters
    print("\n" + "=" * 40)
    print("1. BASIC USAGE WITH DEFAULTS")
    print("=" * 40)
    
    print("\n🐮 Cow with defaults:")
    print(animalsay.cow())
    
    print("\n🐶 Dog with defaults:")
    print(animalsay.dog())
    
    print("\n🐱 Cat with defaults:")
    print(animalsay.cat())
    
    print("\n🐑 Sheep with defaults:")
    print(animalsay.sheep())
    
    
    # Demonstration 2: Animals with custom messages and moods
    print("\n" + "=" * 40)
    print("2. Animals with custom messages and moods")
    print("=" * 40)
    
    print("\n🐮 Cow:")
    print(animalsay.cow("I love eating fresh grass!", mood="happy"))
    print(animalsay.cow("I am sad...", mood="sad"))
    print(animalsay.cow("Hmm, I wonder what's for dinner.", mood="neutral"))
    print(animalsay.cow("Wowwwww", mood="surprised"))
    print(animalsay.cow("Get out of my pasture!", mood="angry"))
    
    print("\n🐶 Dog:")
    print(animalsay.dog("Woof! Woof!", mood="happy"))
    print(animalsay.dog("I miss my owner...", mood="sad"))
    print(animalsay.dog("Just another day in the park.", mood="neutral"))
    print(animalsay.dog("What was that noise?", mood="surprised"))
    print(animalsay.dog("Grrrr! Stay away!", mood="angry"))
    
    print("\n🐱 Cat:")
    print(animalsay.cat("Purr... I am content.", mood="happy"))
    print(animalsay.cat("My toy mouse broke....", mood="sad"))
    print(animalsay.cat("Just napping in the sun.", mood="neutral"))
    print(animalsay.cat("Meow? What's that?", mood="surprised"))
    print(animalsay.cat("Don't touch my tail!", mood="angry"))
    
    

    
    print("\n🐑 Sheep:")
    print(animalsay.sheep("Baa baa! I am so happy!", mood="happy"))
    print(animalsay.sheep("I feel lonely...", mood="sad"))
    print(animalsay.sheep("Counting sheep helps you sleep!", mood="neutral"))
    print(animalsay.sheep("Ewe won't believe it!", mood="surprised"))
    print(animalsay.sheep("Get off my field!", mood="angry"))
    

    


if __name__ == "__main__":
    main()