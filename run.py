# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high


def food_advice(cuisine, food_type):
    """Suggests food based on the user's preferences."""
    suggestions = {
        "Chinese": {
            "Vegetarian": {
                "Rice": {
                    "Fried Rice": ["Yangzhou fried rice", "Vegetable lo mein, Spicy tofu fried rice"],
                    "Soup and Rice Noodles": ["Buddha's delight", "Mapo tofu rice bowl", "Spicy eggplant with rice."],
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
                    "Salads and colds": ["Chichkea salad", "Lentil salad", "White bean salad"],
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
    print(f"{suggestions}")

food_advice("Chinese, Turkish", "Vegetarian, Non-Vegetarian")