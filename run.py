import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


"""Gets the user's preferred base for both Chinese and Turkish cuisine."""
suggestions = {
        "Chinese": {
            "Vegetarian": {
                "Rice": {
                    "Fried Rice": [
                        "Yangzhou fried rice",
                        "Vegetable lo mein",
                        "Spicy tofu fried rice"
                    ],
                    "Soup and Rice Noodles": [
                        "Buddha's delight",
                        "Mapo tofu rice bowl",
                        "Spicy eggplant with rice"
                    ],
                },
                "Noodle": {
                    "Spicy": [
                        "Sichuan dan dan noodles",
                        "Spicy tofu noodle soup",
                        "Spicy zha jiang mian"
                    ],
                    "Classic Savory": [
                        "Sesame noodle salad(Liang mian)",
                        "Vegetable lo mein",
                        "Wombock noodle soup"
                    ]
                },
            },
            "Non-Vegetarian": {
                "Sea Food": {
                    "Classic Seafood": [
                        "Steamed whole fish",
                        "Stir-fried shrimp with snow peas",
                        "Braised fish with black bean sauce"
                    ],
                    "Spicy Seafood": [
                        "Kung pao prwans",
                        "Spicy mussel hot pot",
                        "Spicy garlic lobster"
                    ],
                },
                "Red Meat": {
                    "Stir Fries": [
                        "Kung pao beef",
                        "Black pepper beef",
                        "Beef and broccoli"
                    ],
                    "Braised Foods": [
                        "Braised  pork belly with brown sauce",
                        "Spich sichuan beef stew",
                        "Lion's head meatballs"
                    ],
                },
                "Chicken": {
                    "Stir Fries Chicken": [
                        "Cashew chicken",
                        "Chicken with garlic sauce",
                        "Hunan chicken"
                    ],
                    "Noodle Soups": [
                        "Wonton soup with chicken",
                        "Spicy chicken noodle soup",
                        "Chicken noodle soup with egg drop"
                    ]
                },
            },
        },
        "Turkish": {
            "Vegetarian": {
                "Main Courses": {
                    "Stuffed Vegetables": [
                        "Imam bayildi",
                        "Kabak dolmasi(stuffed zucchini)",
                        "Biber dolmasi(Stuffed peppers)"
                    ],
                    "Savory Fritters and Pancakes": [
                        "Mucver",
                        "Gozleme",
                        "Cigar boreks"
                    ]
                },
                "Lentil and Chickpea": {
                    "Stew and Soups": [
                        "Lentil soup",
                        "Chickpea stew",
                        "Zucchini fritter soup"
                    ],
                    "Salads and Colds": [
                        "Chichkpea salad",
                        "Lentil salad",
                        "White bean salad"
                    ]
                },
            },
            "Non-Vegetarian": {
                "Sea Food": {
                    "Fresh Fish Dishes": [
                        "Levrek izgara(seabass)",
                        "Hamsili Pilav",
                        "Alinazik with shrimp"
                    ],
                    "Seafood Stews and Soups": [
                        "Fish stew",
                        "Seafood soup",
                        "Dalyan dolmasi(stuffed mussels)"
                    ]
                },
                "Red Meat": {
                    "Kebabs": [
                        "Doner kebab",
                        "Adana kebab",
                        "Shish kebab"
                    ],
                    "Stews and Braises": [
                        "Hunkar begendi",
                        "Osmanli kebab",
                        "Iskender kebab"
                    ]
                },
                "Chicken": {
                    "Grilled": [
                        "Tavuk shish",
                        "Alinazik",
                        "Iskender chicken"
                    ],
                    "Baked and Casserole": [
                        "Chicken guvec",
                        "Sultan's delight",
                        "Chicken and pita bread casserole(pide)"
                    ]
                }
            }
        }
}


def get_choice(prompt, options):
    """Get user choice from an options list."""
    while True:
        print(prompt)
        choice = input().strip()
        if not choice:
            print("Invalid choice. Please enter a valid option.")
            continue
        if choice.isdigit() and int(choice) in options:
            return int(choice)
        else:
            print("Invalid choice. Please enter a valid option.")


# Function to get user preferences for cuisine and food type
def get_user_preferences(suggestions):
    while True:
        # Prompt for cuisine choice
        clear_screen()
        print("Select your preferred cuisine:\n ")
        print("1. Chinese")
        print("2. Turkish")
        cuisine_choice = get_choice(
            "\nEnter your choice (1. Chinese / 2. Turkish): ",
            [1, 2])
        cuisine = "Chinese" if cuisine_choice == 1 else "Turkish"
        # Prompt for food type choice
        while True:
            clear_screen()
            print("Select your preferred food type:\n ")
            print("1. Vegetarian")
            print("2. Non-Vegetarian")
            food_type_choice = get_choice(
                "\nEnter your choice (1. Vegetarian / 2. Non-Vegetarian): ",
                [1, 2])
            food_type = ("Vegetarian"
                         if food_type_choice == 1
                         else "Non-Vegetarian")
            break
        base_preferences = get_base_preferences(
            suggestions, cuisine, food_type)
        clear_screen()
        print(f"Here are 3 suggestions for {base_preferences['base']}:\n ")
        for i, suggestion in enumerate(base_preferences['suggestions'], 1):
            print(f"{i}. {suggestion}")
        # Ask if the user wants to try again
        while True:
            try_again = get_choice(
                "\nWould you like to try again? (1. Yes / 2. No): ",
                [1, 2])
            if try_again == 2:
                clear_screen()
                print("Thanks for using Food Finder. Have a good day!")
                exit()
            elif try_again == 1:
                break
            else:
                print("Invalid choice. Please enter 1 or 2.")


# Function to get user preferences for base type
def get_base_preferences(suggestions, cuisine, food_type):
    while True:
        clear_screen()
        print(f"For your {food_type} {cuisine} dish, would you prefer:\n ")
        base_types = suggestions[cuisine][food_type].keys()
        for i, base_type in enumerate(base_types, 1):
            print(f"{i}. {base_type}")
        prompt = f"\nEnter your choice (1 to {len(base_types)}): "
        base_choice = get_choice(prompt, range(1, len(base_types) + 1))
        selected_base = list(base_types)[base_choice - 1]
        return {"base": selected_base,
                "suggestions": get_suggestions(
                    suggestions, cuisine, food_type, selected_base
                )
                }


# Function to get suggestions for a specific base type
def get_suggestions(suggestions, cuisine, food_type, base_type):
    while True:
        clear_screen()
        print(f"How would you like your {base_type}?\n ")
        sub_categories = suggestions[cuisine][food_type][base_type].keys()
        for i, sub_category in enumerate(sub_categories, 1):
            print(f"{i}. {sub_category}")
        prompt = f"\nEnter your choice (1 to {len(sub_categories)}):\n "
        sub_choice = get_choice(prompt, range(1, len(sub_categories) + 1))
        if sub_choice is not None:
            selected_sub_category = list(sub_categories)[sub_choice - 1]
            return (suggestions[cuisine]
                    [food_type][base_type]
                    [selected_sub_category])


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


# Function to display the instructions
def instructions():
    clear_screen()
    print(
        """
Food Finder App Instructions:

1. Answer the following questions to receive food suggestions.
2. Select your preferred cuisine, food type, and dish.
3. Enjoy your personalized food recommendations!\n
        """
    )


# Function to handle the user instructions
def handle_instructions():
    instructions()
    while True:
        user_ready = input("Are you ready to begin (1. Yes / 2. No): ").strip()
        if user_ready == "1":
            return True
        elif user_ready == "2":
            clear_screen()
            print("Thanks for checking the instructions. Have a good day...")
            exit()
        else:
            print("Invalid choice. Please enter 1 or 2.")


# Function to start the app
def start_app():
    clear_screen()
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
            print("Thanks for using Food Finder. Have a good day!")
            return


# Function to run the main logic of the app
def main():
    """Runs the main logics of the Food Finder app."""
    while True:
        start_app()

        try_again = input(
            "Would you like to try again? (1. Yes / 2. No):\n ").strip()
        if not try_again:
            print("Invalid choice. Please enter 1 or 2.:\n ")
            continue
        if try_again == "2":
            print("Thanks for trying Food Finder.\nHave a good day.")
            exit()
        elif try_again == "1":
            continue


if __name__ == "__main__":
    main()
