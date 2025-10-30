"""
In Python packages, this file called __main__.py is run when the package is run
directly from command line, as opposed to importing it into another program.
"""
import sys
from animalsay.animalsay import dog, cow


def main():
    """
    Main function that runs when package is executed as a script.
    Shows introduction, usage, available animals and moods, and an example.
    """
    # Package introduction
    print("=== animalsay - A Fun Python Package ===")
    print("Make animals say things with moods in ASCII art!\n")
    
    # Show usage information
    print("USAGE:")
    print("  From Python code:")
    print("    from animalsay import cow, dog, [...]")
    print("    print(dog('Hello!', mood='happy'))")

    print()
    print("AVAILABLE ANIMALS: cow, dog, [...]")
    print("AVAILABLE MOODS: happy, sad, neutral, angry, surprised")
    print()
    
    # Show an example using dog()
    print("EXAMPLE OUTPUT:")
    example = dog("Hello! I'm a happy dog!", mood="happy")
    print(example)



if __name__ == "__main__":
    # run the main function
    main()

