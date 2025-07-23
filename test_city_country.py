from city_country import receive_city_country

def test_city_country():
    output = receive_city_country('beijing','china',5000000)
    assert output == 'Beijing,China-population 5000000'


