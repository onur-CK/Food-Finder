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


def get_user_preferences(suggestions):
    while True:
        print("Select your preferred cuisine:")
        print("1. Chinese")
        print("2. Turkish")
        cuisine_choice = input('Enter your choice (1 or 2):\n ')
        if cuisine_choice not in ("1", "2"):
            print("Invalid choice. Please enter 1 or 2.")
            continue
        cuisine = "Chinese" if cuisine_choice == "1" else "Turkish"

        print("Select your preferred food type:")
        print("1. Vegetarian")
        print("2. Non-Vegetarian")
        food_type_choice = input("Enter your choice (1 or 2):\n ")
        if food_type_choice not in ("1", "2"):
            print("Invalid choice. Please enter 1 or 2.\n ")    
            continue
        food_type = "Vegetarian" if food_type_choice == "1" else "Non-Vegetarian"

        base_preferences = get_base_preferences(suggestions, cuisine, food_type)    
        print(f"\nHere are 3 suggestions for {base_preferences['base']}:\n ")
        for i, suggestion in enumerate(base_preferences['suggestions'], 1):
            print(f"{i}. {suggestion}")
        try_again = input("\nWould you like to try again? (1. Yes / 2. No):\n")
        if try_again != "1":
            print("Thanks for using Food Finder. Have a good day!")
            break
    

def get_base_preferences(suggestions, cuisine, food_type):
    while True:
        print(f"For your {food_type} {cuisine} dish, would you prefer:\n ")
        base_types = suggestions[cuisine][food_type].keys()
        for i, base_type in enumerate(base_types, 1):
            print(f"{i}. {base_type}")
        base_choice = input(f"Enter your choice (1 or {len(base_types)}):\n ")
        if base_choice.isdigit() and 1 <= int(base_choice) <= len(base_types):
            selected_base = list(base_types)[int(base_choice) - 1]
            return {"base": selected_base, "suggestions": get_suggestions(suggestions, cuisine, food_type, selected_base)}
        else:
            print("Invalid choice. Please enter a number corresponding to the optins.\n ")


def get_suggestions(suggestions, cuisine, food_type, base_type):
    while True:
        print("How would you like your {base_type}")
        sub_categories = suggestions[cuisine][food_type][base_type].keys()
        for i, sub_category in enumerate(sub_categories, 1):
            print(f"{i}. {sub_category}")
        sub_choice = input(f"Enter your choice (1 or {len(sub_categories)}):\n ")
        if sub_choice.isdigit() and 1 <= int(sub_choice) <= len(sub_categories):
            selected_sub_category = list(sub_categories)[int(sub_choice) - 1]
            return suggestions[cuisine][food_type][base_type][selected_sub_category]
        else:
            print ("Invalid choice. Please enter a number corresponding to the options.")



# Function to get the user's choice of cuisine
def get_cuisine_choice():
    """
    Gets the user input for choice of cuisine with validation using the numbered options."""
    while True:
        print("Select your preferred cuisine:")
        print("1. Chinese")
        print("2. Turkish")
        choice = input("Enter your choice (1 or 2):\n ")
        # Validate input (to be sure that number is between 1 and 2)
        if choice in ("1", "2"):
            cuisine_map = {"1": "Chinese", "2": "Turkish"}
            return cuisine_map[choice]
        else:
            print("Invalid choice. Please enter 1 or 2.\n ")

                
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

    base_type = get_base_dish_choice(suggestions, cuisine, food_type)    
    return {"food_type": food_type, "base": base_type}
    




def get_chinese_vegetarian_choice():
    """Gets the user's preferred base (Rice or Noodle) for Vegetarian dishes in Chinese cuisine."""
    while True:
        print("For your Vegetarian Chinese dish, would you prefer: \n")
        print("1. Rice")
        print("2. Noodles")
        base_choice = input("Enter your choice (1 or 2):\n ")
        if base_choice not in ("1", "2"):
            print("Invalid choice. Please enter 1 or 2.")
        else: 
            base_choice = int(base_choice)
            food_preferences = {"food_type": "Vegetarian", "base": base_choice}
            if base_choice == 1: #Rice
                while True:
                    print("How would you like your Rice? \n")
                    print("1. Fried Rice")
                    print("2. Soup and Rice Noodles")
                    style_choice = input("Enter your choice (1 or 2):\n ")
                    if style_choice not in ("1", "2"):
                        print("Invalid choice. Please enter 1 or 2.\n")
                    else: 
                        food_preferences["style"] = style_choice
                        rice_style = "Fried Rice" if style_choice == "1" else "Soup and Rice Noodles"
                        food_options = suggestions["Chinese"]["Vegetarian"]["Rice"][rice_style]
                        "Fried Rice" if style_choice == "1" else "Soup and Rice Noodles"
                        # Print 3 food suggestions based on user preferences
                        print(f"\nHere are 3 suggestions for {food_preferences['base']} with {rice_style}:\n ")
                        for i in range(3):
                            print(f"{i+1}. {food_options[i]}")
                        return food_preferences
            else: #Noodles
                while True :
                    print("How would you like your Noodles?\n ")
                    print("1. Spicy")
                    print("2. Classic Savory")
                    style_choice = input("Enter your choice (1 or 2):\n ")
                    if style_choice not in ("1", "2"):
                        print("Invalid choice. Please enter 1 or 2.")
                    else: 
                        style_choice = int(style_choice)
                        food_preferences["style"] = style_choice
                        noodle_style = "Spicy" if style_choice == 1 else "Classic Savory"
                        food_options = suggestions["Chinese"]["Vegetarian"]["Noodle"][noodle_style]
                        "Spicy" if style_choice == "1" else "Classic Savory"
                        # Print 3 food suggestions based on user preferences
                        print(f"\nHere are 3 suggestions for {food_preferences['base']} with {noodle_style}:\n ")
                        for i in range(3):
                            print(f"{i+1}. {food_options[i]}")
                        return food_preferences


def get_chinese_non_vegetarian_choice():
    """Gets the user's preferred protein for Non-Vegetarian dishes in Chinese cuisine."""
    while True:
        print("For your Non-Vegetarian Chinese dish, would you prefer: ")
        print("1. Sea Food")
        print("2. Red Meat")
        print("3. Chicken")
        protein_choice = input("Enter your choice (1, 2 or 3):\n ")
        if protein_choice not in ("1", "2", "3"):
            print("Invalid choice. Please enter 1, 2, or 3")
        else:
            if protein_choice == "1": # Seafood 
                while True:
                    print("How would you like your Seafood?")
                    print("1. Classic Seafood")
                    print("2. Spicy Seafood")
                    classic_or_spicy = input("Enter your choice (1 or 2):\n ")
                    if classic_or_spicy not in ("1", "2"):
                        print("Invalid Choice. Please enter 1 or 2")
                    else: 
                        seafood_style = "Classic Seafood" if classic_or_spicy == "1" else "Spicy Seafood"
                        food_options = suggestions["Chinese"]["Non-Vegetarian"]["Sea Food"][seafood_style]
                        # Print 3 food suggestions based on user preferences
                        print(f"\nHere are 3 suggestions for Seafood with {seafood_style}:\n ")
                        for i in range(3):
                            print(f"{i+1}. {food_options[i]}")
                        return seafood_style
            elif protein_choice == "2": # Red Meat
                while True:
                    print("How would you like your Red Meat? ")
                    print("1. Stir-Fries")
                    print("2. Braised Dishes")
                    stir_or_braised = input("Enter your choice (1 or 2):\n ")
                    if stir_or_braised not in ("1", "2"):
                        print("Invalid Choice. Please enter 1 or 2")                        
                    else: 
                        meat_style = "Stir Fries" if stir_or_braised == "1" else "Braised Foods"
                        food_options = suggestions["Chinese"]["Non-Vegetarian"]["Red Meat"][meat_style]
                        # Print 3 food suggestions based on user preferences
                        print(f"\nHere are 3 suggestions for Red Meat with {meat_style}:\n ")
                        for i in range(3):
                            print(f"{i+1}. {food_options[i]}")
                        return meat_style
            else: # Chicken
                while True:
                    print("How would you like your Chicken? ")
                    print("1. Stir-Fries-Chicken")
                    print("2. Noodle Soups")
                    stir_or_noodle = input("Enter your choice (1 or 2):\n ")                       
                    if stir_or_noodle not in ("1", "2"):
                        print("Invalid Choice. Please enter 1 or 2")
                    else: 
                        chicken_style = "Stir Fries Chicken" if stir_or_noodle == "1" else "Noodle Soups"
                        food_options = suggestions["Chinese"]["Non-Vegetarian"]["Chicken"][chicken_style]
                        # Print 3 food suggestions based on user preferences
                        print(f"\nHere are 3 suggestions for Chicken with {chicken_style}:\n ")
                        for i in range(3):
                            print(f"{i+1}. {food_options[i]}")
                        return "Stir-Fries-Chicken" if stir_or_noodle == "1" else "Noodle Soups"
               
    return "Non-Vegetarian Choice"  

def get_turkish_vegetarian_choice():
    """Gets the user's preferred base (Rice or Noodle) for Vegetarian dishes in Chinese cuisine."""
    while True:
        print("For your Vegetarian Turkish dish, would you prefer:\n ")
        print("1. Main Courses")
        print("2. Lentil and Chickpea")
        base_choice = input("Enter your choice (1 or 2):\n ")
        if base_choice not in ("1", "2"):
            print("Invalid choice. Please enter 1 or 2:\n ")
        else: 
            base_choice = int(base_choice)
            food_preferences = {"food_type": "Vegetarian", "base": base_choice}
            if base_choice == 1: # Main Courses
                while True:
                    print("How would you like your Main courses?\n ")
                    print("1. Stuffed Vegetables")
                    print("2. Savory Fritters and Pancakes")
                    style_choice = input("Enter your choice (1 or 2):\n ")
                    if style_choice not in ("1", "2"):
                        print("Invalid choice. Please enter 1 or 2:\n ")
                    else: 
                        food_preferences["style"] = style_choice
                        main_courses_style = "Stuffed Vegetables" if style_choice == "1" else "Savory Fritters and Pancakes"
                        food_options = suggestions["Turkish"]["Vegetarian"]["Main Courses"][main_courses_style]
                        "Stuffed Vegetables" if style_choice == "1" else "Savory Fritters and Pancakes"
                        # Print 3 food suggestions based on user preferences
                        print(f"\nHere are 3 suggestions for {food_preferences['base']} with {main_courses_style}:\n ")
                        for i in range(3):
                            print(f"{i+1}. {food_options[i]}")
                        return food_preferences
            else: # Lentil and Chickpea
                while True :
                    print("How would you like your Lentil and Chickpea?\n ")
                    print("1. Stew and Soups")
                    print("2. Salads and Colds")
                    style_choice = input("Enter your choice (1 or 2):\n ")
                    if style_choice not in ("1", "2"):
                        print("Invalid choice. Please enter 1 or 2:\n ")
                    else: 
                        style_choice = int(style_choice)
                        food_preferences["style"] = style_choice
                        lentil_and_chickpea_style = "Stew and Soups" if style_choice == 1 else "Salads and Colds"
                        food_options = suggestions["Turkish"]["Vegetarian"]["Lentil and Chickpea"][lentil_and_chickpea_style]
                        "Stew and Soups" if style_choice == "1" else "Salad and Colds"
                        # Print 3 food suggestions based on user preferences
                        print(f"\nHere are 3 suggestions for {food_preferences['base']} with {lentil_and_chichpea_style}:\n ")
                        for i in range(3):
                            print(f"{i+1}. {food_options[i]}")
                        return food_preferences

def get_turkish_non_vegetarian_choice():
    """Gets the user's preferred protein for Non-Vegetarian dishes in Turkish cuisine."""
    while True:
        print("For your Non-Vegetarian Turkish dish, would you prefer:\n ")
        print("1. Sea Food")
        print("2. Red Meat")
        print("3. Chicken")
        protein_choice = input("Enter your choice (1, 2 or 3):\n ")
        if protein_choice not in ("1", "2", "3"):
            print("Invalid choice. Please enter 1, 2, or 3")
        else:
            if protein_choice == "1": # Seafood 
                while True:
                    print("How would you like your Seafood?\n ")
                    print("1. Fresh Fish Dishes")
                    print("2. Seafood Stews and Soups")
                    fresh_fish_or_soups = input("Enter your choice (1 or 2):\n ")
                    if fresh_fish_or_soups not in ("1", "2"):
                        print("Invalid Choice. Please enter 1 or 2:\n ")
                    else: 
                        seafood_style = "Fresh Fish Dishes" if fresh_fish_or_soups == "1" else "Seafood Stews and Soups"
                        food_options = suggestions["Turkish"]["Non-Vegetarian"]["Sea Food"][seafood_style]
                        # Print 3 food suggestions based on user preferences
                        print(f"\nHere are 3 suggestions for Seafood with {seafood_style}:\n ")
                        for i in range(3):
                            print(f"{i+1}. {food_options[i]}")
                        return seafood_style
            elif protein_choice == "2": # Red Meat
                while True:
                    print("How would you like your Red Meat? ")
                    print("1. Kebabs")
                    print("2. Stews and Braises")
                    kebabs_or_stews = input("Enter your choice (1 or 2):\n ")
                    if kebabs_or_stews not in ("1", "2"):
                        print("Invalid Choice. Please enter 1 or 2:\n ")                        
                    else: 
                        meat_style = "Kebabs" if kebabs_or_stews == "1" else "Stews and Braises"
                        food_options = suggestions["Turkish"]["Non-Vegetarian"]["Red Meat"][meat_style]
                        # Print 3 food suggestions based on user preferences
                        print(f"\nHere are 3 suggestions for Red Meat with {meat_style}:\n ")
                        for i in range(3):
                            print(f"{i+1}. {food_options[i]}")
                        return meat_style
            else: # Chicken
                while True:
                    print("How would you like your Chicken? ")
                    print("1. Grilled")
                    print("2. Baked and Casserole")
                    grilled_or_baked_casserole = input("Enter your choice (1 or 2):\n ")                       
                    if grilled_or_baked_casserole not in ("1", "2"):
                        print("Invalid Choice. Please enter 1 or 2:\n ")
                    else: 
                        chicken_style = "Grilled" if grilled_or_baked_casserole == "1" else "Baked and Casserole"
                        food_options = suggestions["Turkish"]["Non-Vegetarian"]["Chicken"][chicken_style]
                        # Print 3 food suggestions based on user preferences
                        print(f"\nHere are 3 suggestions for Chicken with {chicken_style}:\n ")
                        for i in range(3):
                            print(f"{i+1}. {food_options[i]}")
                        return "Grilled" if grilled_or_baked_casserole == "1" else "Baked and Casserole"
               
    return "Non-Vegetarian Choice"  


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
        cuisine_preference = get_cuisine_choice()
        print(f"You selected {cuisine_preference} cuisine.\n")

        food_preferences = get_food_preferences(suggestions, cuisine_preference)
        base_choice = get_base_dish_preferences(suggestions, cuisine_preference, food_preferences["food_type"], food_preferences["base"])
        print(f"Here are 3 suggestions for {base_choice}:\n")
            
        try_again = input("Would you like to try again? (1. Yes / 2. No):\n ")
        while try_again not in ("1", "2"):
            print("Invalid choice. Please enter 1 or 2.:\n ")
            try_again = input("Would you like to try again? (1. Yes / 2. No):\n ")
        if try_again != "1":
            print("Thanks for trying to Food Finder.\nHave a good day.")
            break  

if __name__ == "__main__":  
    start_app()