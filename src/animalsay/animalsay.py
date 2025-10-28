def cow(text="Hello world!", mood="neutral"):
    """
    Make a cow say something with a specific mood.
    
    Args:
        text (str): The text for the cow to say
        mood (str): Cow's mood - 'happy', 'sad', 'neutral', 'angry', 'surprised'
    
    Returns:
        str: ASCII art of cow with speech bubble
    """
    # Define cow faces based on mood
    faces = {
        "happy": "^^",
        "sad": "••", 
        "neutral": "oo",
        "angry": "><",
        "surprised": "OO"
    }
    
    face = faces.get(mood, "oo")
    
    # Create speech bubble
    bubble = text
    
    # Create cow art using raw string to avoid escape sequence warnings
    cow_art = fr"""
{bubble}
        \   ^__^
         \  ({face})\_______
            (__)\       )\/\
                ||----w |
                ||     ||
    """
    
    return cow_art


def dog(text="Hello world!", mood="neutral"):
    """
    Make a dog say something with a specific mood.
    
    Args:
        text (str): The text for the dog to say
        mood (str): Dog's mood - 'happy', 'sad', 'neutral', 'angry', 'surprised'
    
    Returns:
        str: ASCII art of dog with speech bubble
    """
    # Define dog faces based on mood
    faces = {
        "happy": "∩",
        "sad": "╥", 
        "neutral": "@",
        "angry": ">",
        "surprised": "O"
    }
    
    face = faces.get(mood, "@")
    
    # Create speech bubble
    bubble = text
    
    # Create dog art using raw string to avoid escape sequence warnings
    dog_art = fr"""
{bubble}
      \
       \   / \__
          (    {face}\\__
          /         O
         /   (_____/
        /_____/   U
"""
    
    return dog_art
