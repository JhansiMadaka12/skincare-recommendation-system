from skincare import recommend_products, preprocess_input

def test_oily_acne():
    result = recommend_products("oily", "acne")
    assert "Oil-Free Face Wash" in result

def test_dry_sensitive():
    result = recommend_products("dry", "sensitive")
    assert "Ceramide Moisturizer" in result

def test_preprocessing():
    skin_type, condition = preprocess_input("  OILY ", " Acne ")
    assert skin_type == "oily"
    assert condition == "acne"
