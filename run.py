
def get_cuisine_choice():
    """Gets the user input for choice of cuisine with validation using the numbered options."""
    while True:
        print("Select your preferred cuisine:")
        print("1. Chinese")
        print("2. Turkish")

        choice = input("Enter your choice (1 or 2): ")
        # Validate input (to be sure that number is between 1 and 2)
        if not choice.isdigit() or not (1 <= int(choice) <= 2):
            print("Invalid choice. Please enter 1 or 2.\n")
        else:    
            cuisine_map = {
                "1": "Chinese",
                "2": "Turkish"
            }
            return cuisine_map[choice]
        
            

          
def get_food_type():
    """Get the user preference for Vegetarian or Non-Vegetarian dishes."""
    vegetarian_choice = None # Prepares the variable to store the user's choice for vegetarian or non-vegetarian dishes.

    while vegetarian_choice not in ("1", "2"):
        print("Select your preferred food type:")
        print("1. Vegetarian")
        print("2. Non-Vegetarian")
        
        vegetarian_choice = input("Enter your choice (1 or 2) ")
        if vegetarian_choice not in ("1", "2"):
            print("Invalid choice. Please enter 1 or 2. ")
    else: 
        return {"food_type": ("Vegetarian" if vegetarian_choice== "1" else "Non-Vegetarian")} 
    # Store user choice in a dictionary and return.
    user_preferences = {"food_type": ("Vegetarian" if vegetarian_choice == "1" else "Non-Vegetarian")}
    return user_preferences


def get_chinese_vegetarian_choice():
    """Gets the user's preferred base (Rice or Noodle) for Vegetarian dishes in Chinese cuisine."""
    while True:
        print("For your Vegetarian Chinese dish, would you prefer: \n")
        print("1. Rice")
        print("2. Noodles")
        base_choice = input("Enter your choice (1 or 2): ")
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
                    style_choice = input("Enter your choice (1 or 2): ")
                    if style_choice not in ("1", "2"):
                        print("Invalid choice. Please enter 1 or 2.")
                    else: 
                        food_preferences["style"] = style_choice
                        rice_style = "Fried Rice" if style_choice == "1" else "Soup and Rice Noodles"
                        food_options = suggestions["Chinese"]["Vegetarian"]["Rice"][rice_style]
                        "Fried Rice" if style_choice == "1" else "Soup and Rice Noodles"
                        print(f"\nHere are 3 suggestions for {food_preferences['base']} with {food_preferences["style"]}:")
                        for i in range(3):
                            print(f"{i+1}. {food_options[i]}")
                        return food_preferences
            else: #Noodles
                while True :
                    print("How would you like your Noodles?")
                    print("1. Spicy")
                    print("2. Classic Savory")
                    style_choice = input("Enter your choice (1 or 2): ")
                    if style_choice not in ("1", "2"):
                        print("Invalid choice. Please enter 1 or 2.")
                    else: 
                        style_choice = int(style_choice)
                        food_preferences["style"] = style_choice
                        noodle_style = "Spicy" if style_choice == 1 else "Classic Savory"
                        food_options = suggestions["Chinese"]["Vegetarian"]["Noodle"][noodle_style]
                        "Spicy" if style_choice == "1" else "Classic Savory"
                        
                        print(f"\nHere are 3 suggestions for {food_preferences['base']} with {food_preferences['style']}:")
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
        protein_choice = input("Enter your choice (1, 2 or 3): ")
        if protein_choice not in ("1", "2", "3"):
            print("Invalid choice. Please enter 1, 2, or 3")
        else:
            if protein_choice == "1": # Seafood 
                while True:
                    print("How would you like your Seafood?")
                    print("1. Classic Seafood")
                    print("2. Spicy Seafood")
                    classic_or_spicy = input("Enter your choice (1 or 2): ")
                    if classic_or_spicy not in ("1", "2"):
                        print("Invalid Choice. Please enter 1 or 2")
                    else: 
                        seafood_style = "Classic Seafood" if classic_or_spicy == "1" else "Spicy Seafood"
                        food_options = suggestions["Chinese"]["Non-Vegetarian"]["Sea Food"][seafood_style]
                        print(f"\nHere are 3 suggestions for Seafood with {seafood_style}:")
                        for i in range(3):
                            print(f"{i+1}. {food_options[i]}")
                        return seafood_style
            elif protein_choice == "2": # Red Meat
                while True:
                    print("How would you like your Red Meat? ")
                    print("1. Stir-Fries")
                    print("2. Braised Dishes")
                    stir_or_braised = input("Enter your choice (1 or 2): ")
                    if stir_or_braised not in ("1", "2"):
                        print("Invalid Choice. Please enter 1 or 2")                        
                    else: 
                        meat_style = "Stir Fries" if stir_or_braised == "1" else "Braised Foods"
                        food_options = suggestions["Chinese"]["Non-Vegetarian"]["Red Meat"][meat_style]
                        print(f"\nHere are 3 suggestions for Red Meat with {meat_style}:")
                        for i in range(3):
                            print(f"{i+1}. {food_options[i]}")
                        return meat_style
            else:
                while True:
                    print("How would you like your Chicken? ")
                    print("1. Stir-Fries-Chicken")
                    print("2. Noodle Soups")
                    stir_or_noodle = input("Enter your choice (1 or 2): ")                       
                    if stir_or_noodle not in ("1", "2"):
                        print("Invalid Choice. Please enter 1 or 2")
                    else: 
                        chicken_style = "Stir Fries Chicken" if stir_or_noodle == "1" else "Noodle Soups"
                        food_options = suggestions["Chinese"]["Non-Vegetarian"]["Chicken"][chicken_style]
                        print(f"\nHere are 3 suggestions for Chicken with {chicken_style}:")
                        for i in range(3):
                            print(f"{i+1}. {food_options[i]}")
                        return "Stir-Fries-Chicken" if stir_or_noodle == "1" else "Noodle Soups"
               
    return "Non-Vegetarian Choice"  


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
                } ,
                },
        "Turkish": {
            "Vegetarian": {
                "Main Courses": {
                    "Stuffed Vegetables": ["Imam bayildi", "Kabak dolmasi(stuffed zucchini)", "Biber dolmasi(Stuffed peppers)"],
                    "Savory Fritters and Pancakes": ["Mucver", "Gozleme", "Cigar boreks"],
                "Lentil and Chickpea": {
                    "Stew and soups": ["Lentil soup", "Chickpea stew", "Zucchini fritter soup"],
                    "Salads and colds": ["Chichkpea salad", "Lentil salad", "White bean salad"],
            "Non-Vegetarian": {
                "Sea Food": {
                    "Fresh fish dishes": ["Levrek izgara(seabass)", "Hamsili Pilav", "Alinazik with shrimp"],
                    "Seafood stews and soups": ["Fish stew", "seafood soup", "Dalyan dolmasi(stuffed mussels)"],
                "Red Meat": {
                    "Kebabs": ["Doner kebab", "Adana kebab", "Shish kebab"],
                    "Stews and Braises": ["Hunkar begendi", "Osmanli kebab"],
                "Chicken": {
                    "Grilled": ["Tavuk shish", "Alinazik", "Iskender chicken"],
                    "Baked and Casserole": ["Chicken guvec", "Sultan's delight", "Chicken and pita bread casserole(pide)"]
                }
                }
                }
            }
                }
                }
            }
        }
            } 
            
        
     
    



cuisine_preference = get_cuisine_choice()
print(f"You selected {cuisine_preference} cuisine.\n")

food_preferences = get_food_type() # Call function to store the returned dictionary.

if food_preferences["food_type"] in ("Vegetarian", "Non-Vegetarian"):
    if cuisine_preference == "Chinese":
        if food_preferences["food_type"] == "Vegetarian":
            base_choice = get_chinese_vegetarian_choice()
            food_preferences["base"] = base_choice
        else:
            protein_choice = get_chinese_non_vegetarian_choice()
            food_preferences["protein"] = protein_choice
            









def food_advice(cuisine, food_type):
    """Suggests food based on the user's preferences."""
    suggestions = {
        "Chinese": {
            "Vegetarian": {
                "Rice": {
                    "Fried Rice": ["Yangzhou fried rice", "Vegetable lo mein, Spicy tofu fried rice"],
                    "Soup and Rice Noodles": ["Buddha's delight", "Mapo tofu rice bowl", "Spicy eggplant with rice"],
                "Noodle": {
                    "Spicy": ["Sichuan dan dan noodles", "Spicy tofu noodle soup", "Spicy zha jiang mian"],
                    "Classic Savory": ["Sesame noodle salad(Liang mian)", "Vegetable lo mein", "Wombock noodle soup"]
                },
                },
            "Non-Vegetarian": {
                "Sea Food": {
                    "Classic Seafood": ["Steamed whole fish", "Stir-fried shrimp with snow peas", "Braised fish with black bean sauce"],
                    "Spicy Seafood": ["Kung pao prwans", "Spicy mussel hot pot", "Spicy garlic lobster"],
                "Red Meat": {
                    "Stir Fries": ["Kung pao beef", "Black pepper beef", "Beef and broccoli"],
                    "Braised Foods": ["Braised  pork belly with brown sauce", "Spich sichuan beef stew", "Lion's head meatballs"],
                "Chicken": {
                    "Stir Fries Chicken": ["Cashew chicken", "Chicken with garlic sauce", "Hunan chicken"],
                    "Noodle Soups": ["Wonton soup with chicken", "Spicy chicken noodle soup", "Chicken noodle soup with egg drop"]
                }
                } 
                },
        "Turkish": {
            "Vegetarian": {
                "Main Courses": {
                    "Stuffed Vegetables": ["Imam bayildi", "Kabak dolmasi(stuffed zucchini)", "Biber dolmasi(Stuffed peppers)"],
                    "Savory Fritters and Pancakes": ["Mucver", "Gozleme", "Cigar boreks"],
                "Lentil and Chickpea": {
                    "Stew and soups": ["Lentil soup", "Chickpea stew", "Zucchini fritter soup"],
                    "Salads and colds": ["Chichkpea salad", "Lentil salad", "White bean salad"],
            "Non-Vegetarian": {
                "Sea Food": {
                    "Fresh fish dishes": ["Levrek izgara(seabass)", "Hamsili Pilav", "Alinazik with shrimp"],
                    "Seafood stews and soups": ["Fish stew", "seafood soup", "Dalyan dolmasi(stuffed mussels)"],
                "Red Meat": {
                    "Kebabs": ["Doner kebab", "Adana kebab", "Shish kebab"],
                    "Stews and Braises": ["Hunkar begendi", "Osmanli kebab"],
                "Chicken": {
                    "Grilled": ["Tavuk shish", "Alinazik", "Iskender chicken"],
                    "Baked and Casserole": ["Chicken guvec", "Sultan's delight", "Chicken and pita bread casserole(pide)"]
                }
                }
                }
            }
                }
                }
            }
        }
            } 
            
        }
     }
    } 
    #print(f"{suggestions}")

#food_advice("Chinese, Turkish", "Vegetarian, Non-Vegetarian")