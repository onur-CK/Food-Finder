
def get_cuisine_choice():
    """Gets the user input for choice of cuisine with validation using the numbered options."""
    while True:
        print("Select your preferred cuisine:")
        print("1. Chinese")
        print("2. Turkish")

        choice = input("Enter your choice (1 or 2): ")
        # Validate input (to be sure that number is between 1 and 2)
        if choice.isdigit() and (1 <= int(choice) <= 2):
            cuisine_map = {
                "1": "Chinese",
                "2": "Turkish"
            }
            return cuisine_map[choice]
        else:
            print("Invalid choice. Please enter 1 or 2.")


get_cuisine_choice()











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
                    "Stir Fries": ["Cashew chicken", "Chicken with garlic sauce", "Hunan chicken"],
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

food_advice("Chinese, Turkish", "Vegetarian, Non-Vegetarian")