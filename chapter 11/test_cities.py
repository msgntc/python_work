from city_functions import city_country
def test_city_country():
    """Test for city_country function"""
    formatted_city_country = city_country("Santiago", "Chile")
    assert formatted_city_country == '"Santiago, Chile"'
