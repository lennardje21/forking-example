#-----------------------------------------------------------------------------

import random

#-----------------------------------------------------------------------------

def get_contributions():

    """
    Each student should add their name and a fun fact or a short fact in the 'contributions' list below.
    Example: ("Alice", "I love Python!")
    """
    contributions = [

        # Teacher contribution
        ("Ruud", "Ik ben getrouwd, maar woon niet samen."),
        
        # Students, add your entries here:
        ("Koiya", "Your fun fact"),
        ("Yasin", "Your fun fact"),
        ("Alaa", "Your fun fact"),
        ("Ihssane", "Your fun fact"),
        ("Adam", "Your fun fact"),
        ("Bart", "Your fun fact"),
        ("Thomas", "Your fun fact"),
        ("Jade", "Your fun fact"),
        ("Floris", "Your fun fact"),
        ("Jeffrey", "Your fun fact"),
        ("Mohamed", "Your fun fact"),
        ("Manu", "Your fun fact"),
        ("Anmol", "Your fun fact"),
        ("Saif", "Your fun fact"),
        ("Artur", "Your fun fact"),
        ("Yashin", "Your fun fact"),
        ("Tabitha", "Your fun fact"),
        ("Matthijs", "Your fun fact"),
        ("Yash", "Your fun fact"),
        ("Daan", "Your fun fact"),
        ("Noortje", "Your fun fact"),
        ("Irmak", "Your fun fact"),
        ("Kimberly", "Your fun fact"),
        ("Kelvin", "Your fun fact"),
        ("Rafael", "Your fun fact"),
        ("Lennard", "Ik ben kleurenblind"),

    ]

    return contributions

#-----------------------------------------------------------------------------

def main():

    contributions = get_contributions()

    if not contributions:

        print("No contributions yet. Add some first!")
        
        return
    
    # Shuffle contributions to ensure random order without repeats
    random.shuffle(contributions)

    print("=" * 40)

    print("🎲 Random Fun Facts Generator 🎲")

    print("=" * 40)

    print("Press Enter to see the next fact, or type 'q' to quit.\n")
    
    while contributions:
            
        user_input = input(">> ")
        
        if user_input.lower() in {"q", "quit"}:
            
            print("Goodbye! 👋")
            
            break

        # Remove from list (no repeats)
        name, fact = contributions.pop()
        
        print(f"- {name}: {fact}\n")
    
    if not contributions:

        print("✅ All contributions have been shown!")

#-----------------------------------------------------------------------------

if __name__ == "__main__":

    main()

#-----------------------------------------------------------------------------
