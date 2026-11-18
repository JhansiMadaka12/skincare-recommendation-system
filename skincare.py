# Personalized Skin Care Products Recommendation System
# Using rule-based logic + data preprocessing concept

products_data = {
    "oily": {
        "acne": ["Oil-Free Face Wash", "Salicylic Acid Serum", "Gel Moisturizer"],
        "sensitive": ["Gentle Foaming Cleanser", "Aloe Vera Gel", "Oil-Free Moisturizer"],
        "normal": ["Foam Cleanser", "Niacinamide Serum", "Light Moisturizer"]
    },
    "dry": {
        "acne": ["Hydrating Cleanser", "Hyaluronic Acid Serum", "Cream Moisturizer"],
        "sensitive": ["Gentle Cream Cleanser", "Ceramide Moisturizer", "Sunscreen SPF 50"],
        "normal": ["Cream Cleanser", "Vitamin C Serum", "Rich Moisturizer"]
    },
    "combination": {
        "acne": ["Balancing Cleanser", "BHA Serum", "Gel-Cream Moisturizer"],
        "sensitive": ["Mild Cleanser", "Centella Serum", "Light Cream Moisturizer"],
        "normal": ["Gel Cleanser", "Niacinamide Serum", "Moisturizer"]
    }
}

def preprocess_input(skin_type, skin_condition):
    # Data Preprocessing - clean input
    skin_type = skin_type.lower().strip()
    skin_condition = skin_condition.lower().strip()
    return skin_type, skin_condition

def recommend_products(skin_type, skin_condition):
    skin_type, skin_condition = preprocess_input(skin_type, skin_condition)
    try:
        return products_data[skin_type][skin_condition]
    except KeyError:
        return ["Gentle Cleanser", "Basic Moisturizer", "Sunscreen"]

if __name__ == "__main__":
    skin_type = input("Enter skin type (oily/dry/combination): ")
    condition = input("Enter skin condition (acne/sensitive/normal): ")
    result = recommend_products(skin_type, condition)
    print("Recommended Products:", result)
