"""Gets the user's preferred base for both Chinese and Turkish cuisine."""
suggestions = {
        "Chinese": {
            "Vegetarian": {
                "Rice": {
                    "Fried Rice": ["Yangzhou fried rice", "Vegetable lo mein", "Spicy tofu fried rice"],
                    "Soup and Rice Noodles": ["Buddha's delight", "Mapo tofu rice bowl", "Spicy eggplant with rice"],
                },
                "Noodle": {
                    "Spicy": ["Sichuan dan dan noodles", "Spicy tofu noodle soup", "Spicy zha jiang mian"],
                    "Classic Savory": ["Sesame noodle salad(Liang mian)", "Vegetable lo mein", "Wombock noodle soup"]
                },
            },
            "Non-Vegetarian": {
                "Sea Food": {
                    "Classic Seafood": ["Steamed whole fish", "Stir-fried shrimp with snow peas", "Braised fish with black bean sauce"],
                    "Spicy Seafood": ["Kung pao prwans", "Spicy mussel hot pot", "Spicy garlic lobster"],
                },
                "Red Meat": {
                    "Stir Fries": ["Kung pao beef", "Black pepper beef", "Beef and broccoli"],
                    "Braised Foods": ["Braised  pork belly with brown sauce", "Spich sichuan beef stew", "Lion's head meatballs"],
                },
                "Chicken": {
                    "Stir Fries Chicken": ["Cashew chicken", "Chicken with garlic sauce", "Hunan chicken"],
                    "Noodle Soups": ["Wonton soup with chicken", "Spicy chicken noodle soup", "Chicken noodle soup with egg drop"]
                },
            },
        },
        "Turkish": {
            "Vegetarian": {
                "Main Courses": {
                    "Stuffed Vegetables": ["Imam bayildi", "Kabak dolmasi(stuffed zucchini)", "Biber dolmasi(Stuffed peppers)"],
                    "Savory Fritters and Pancakes": ["Mucver", "Gozleme", "Cigar boreks"]
                },
                "Lentil and Chickpea": {
                    "Stew and Soups": ["Lentil soup", "Chickpea stew", "Zucchini fritter soup"],
                    "Salads and Colds": ["Chichkpea salad", "Lentil salad", "White bean salad"]
                },
            },   
            "Non-Vegetarian": {
                "Sea Food": {
                    "Fresh Fish Dishes": ["Levrek izgara(seabass)", "Hamsili Pilav", "Alinazik with shrimp"],
                    "Seafood Stews and Soups": ["Fish stew", "Seafood soup", "Dalyan dolmasi(stuffed mussels)"]
                },
                "Red Meat": {
                    "Kebabs": ["Doner kebab", "Adana kebab", "Shish kebab"],
                    "Stews and Braises": ["Hunkar begendi", "Osmanli kebab", "Iskender kebab"]
                },
                "Chicken": {
                    "Grilled": ["Tavuk shish", "Alinazik", "Iskender chicken"],
                    "Baked and Casserole": ["Chicken guvec", "Sultan's delight", "Chicken and pita bread casserole(pide)"]
                }
            }
            
        }
}

def get_choice(prompt, options):
    """Get user choice from an options list."""
    while True:
        choice = input(prompt).strip()
        if choice.isdigit() and int(choice) in options:
            return int(choice)
        else:
            print("Invalid choice. Please enter a valid option.")

def get_user_preferences(suggestions):
    # Prompt for cuisine choice
    while True:
        print("Select your preferred cuisine:")
        print("1. Chinese")
        print("2. Turkish")
        cuisine_choice = input("Enter your choice (1. Yes / 2. No): ").strip() 
        if not cuisine_choice:
            print("Invalid choice. Please enter 1 or 2.")
            continue
        if cuisine_choice not in ("1", "2"):
            print("Invalid choice. Please enter 1 or 2.")
            continue
        cuisine = "Chinese" if cuisine_choice == "1" else "Turkish"

        # Prompt for food type choice
        while True:
            print("Select your preferred food type:")
            print("1. Vegetarian")
            print("2. Non-Vegetarian")
            food_type_choice = input("Enter your choice (1. Yes / 2. No): ").strip()
            if not food_type_choice:
                print("Invalid choice. Please enter 1 or 2.")
                continue
            if food_type_choice not in ("1", "2"):
                print("Invalid choice. Please enter 1 or 2.")
                continue
            food_type = "Vegetarian" if food_type_choice == "1" else "Non-Vegetarian"
            break

        base_preferences = get_base_preferences(suggestions, cuisine, food_type)    
        print(f"\nHere are 3 suggestions for {base_preferences['base']}:\n ")
        for i, suggestion in enumerate(base_preferences['suggestions'], 1):
            print(f"{i}. {suggestion}")
        
        # Prompt for trying again
        while True:
            try_again = input("\nWould you like to try again? (1. Yes / 2. No):\n").strip()
            if not try_again: # Check if the user input is empty
                print("Invalid choice. Please enter (1. Yes / 2. No):\n ")
                continue
            if try_again not in ("1", "2"):
                print("Invalid choice. Please enter (1. Yes / 2. No):\n ")
                continue
            if try_again == "2":
                print("Thanks for using Food Finder. Have a good day!")
                return
            break


def get_base_preferences(suggestions, cuisine, food_type):
    while True:
        print(f"For your {food_type} {cuisine} dish, would you prefer:\n ")
        base_types = suggestions[cuisine][food_type].keys()
        for i, base_type in enumerate(base_types, 1):
            print(f"{i}. {base_type}")
        base_choice = get_choice(f"Enter your choice (1 or {len(base_types)}): ", range(1, len(base_types) + 1)) 
        
        selected_base = list(base_types)[base_choice - 1]
        return {"base": selected_base, "suggestions": get_suggestions(suggestions, cuisine, food_type, selected_base)}


def get_suggestions(suggestions, cuisine, food_type, base_type):
    while True:
        print(f"How would you like your {base_type}?")
        sub_categories = suggestions[cuisine][food_type][base_type].keys()
        for i, sub_category in enumerate(sub_categories, 1):
            print(f"{i}. {sub_category}")
        sub_choice = get_choice(f"Enter your choice (1 or {len(sub_categories)}):\n ", range(1, len(sub_categories) + 1))
        if sub_choice is not None:
            selected_sub_category = list(sub_categories)[sub_choice -1]
            return suggestions[cuisine][food_type][base_type][selected_sub_category]

"""
def get_suggestions(suggestions, cuisine, food_type, base_type):
    while True:
        print(f"How would you like your {base_type}")
        sub_categories = suggestions[cuisine][food_type][base_type].keys()
        for i, sub_category in enumerate(sub_categories, 1):
            print(f"{i}. {sub_category}")
        sub_choice = get_choice(f"Enter your choice (1 or {len(sub_categories)}):\n ", range(1, len(sub_categories) + 1))
        selected_sub_category = list(sub_categories)[sub_choice -1]
        return suggestions[cuisine][food_type][base_type][selected_sub_category]
"""       

def get_food_preferences(suggestions):
    """Get the user preference for Vegetarian or Non-Vegetarian dishes."""
    vegetarian_choice = None
    while vegetarian_choice not in ("1", "2"):
        print("Select your preferred food type:")
        print("1. Vegetarian")
        print("2. Non-Vegetarian")
        vegetarian_choice = input("Enter your choice (1 or 2):\n ")
        if vegetarian_choice not in ("1", "2"):
            print("Invalid choice. Please enter 1 or 2.\n ")    

    food_type = "Vegetarian" if vegetarian_choice == "1" else "Non-Vegetarian"
    base_preferences = get_base_preferences(suggestions, cuisine, food_type)
    return {"food_type": food_type, "base": base_preferences["base"]}
    

# Food Finder ASCII logo
def intro():
    print(
    """
  _____ ___   ___  ____    _____ ___ _   _ ____  _____ ____  
 |  ___/ _ \\ / _ \\|  _ \\  |  ___|_ _| \\ | |  _ \\| ____|  _ \\ 
 | |_ | | | | | | | | | | | |_   | ||  \\| | | | |  _| | |_) |
 |  _|| |_| | |_| | |_| | |  _|  | || |\\  | |_| | |___|  _ < 
 |_|   \\___/ \\___/|____/  |_|   |___|_| \\_|____/|_____|_| \\_\\


Welcome to Food Finder App\n
Please select an option:
1. Begin answering the questions.
2. See the instructions.                                                     

    """
)


def instructions():
    print(
"""
Food Finder App Instructions:

1. Answer the following questions to receive food suggestions.
2. Select your preferred cuisine, food type, and dish.
3. Enjoy your personalized food recommendations!\n
"""
)

def ask_if_user_ready():
    user_ready = input("Are you ready to begin (1. Yes . 2. No): ")

    while user_ready not in ("1", "2"):
        print("Invalid choice. Please enter 1 or 2.")
        user_ready = input("Are you ready to begin? (1. Yes / 2. No): ")

    return user_ready

def handle_instructions():
    instructions()
    user_ready = ask_if_user_ready()
    return user_ready == "1"


def start_app():
    intro()
    user_choice = input("Enter your choice (1 or 2): ")

    while user_choice not in ("1", "2"):
        print("Invalid choice.Please enter 1 or 2.")
        user_choice = input("Enter your choice (1 or 2): ")

    if user_choice == "1":
        print("Let's get started!\n")
        get_user_preferences(suggestions)
    elif user_choice == "2":
        user_ready = handle_instructions()
        if user_ready:
            print("Let's get started!\n ")
            get_user_preferences(suggestions)
        else: 
            print("Thanks for checking the instructions. Have a good day!")
        

def main():
    """Runs the main logics of the Food Finder app."""
    while True:
        start_app()
        
        try_again = input("Would you like to try again? (1. Yes / 2. No):\n ").strip()
        if try_again == "":
            print("Invalid choice. Please enter 1 or 2.:\n ")
            continue
        if try_again == "2":
            print("Thanks for trying Food Finder.\nHave a good day.") 
            break
        if try_again != "1":
            print("Invalid choice. Please enter 1 or 2.:\n ")
            continue # Restart the loop to allow user to try again

if __name__ == "__main__":  
    main()          

            
