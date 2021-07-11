import pytest
from classes.candle_class import Candle
from classes.catalogue_manager_class import CatalogueManager


def test_empty_list():
    catalogue_manager = CatalogueManager
    number_of_candles = catalogue_manager.number_of_candles()
    assert number_of_candles == 0


def test_creating_candle_with_correct_pricing_format():
    catalogue_manager = CatalogueManager
    candle = catalogue_manager.add_candle('name1', 100, 'fragrance', 'jar', 1.5, 20.0, 20.0, 9.99)  
    assert candle.__str__() == 'Name = name1 | ID = 100 | Fragrance = fragrance | Candle Type = jar | Burn Time = 1.5hr | Diameter x Height = 20.0cm x 20.0cm | Price = £9.99'
    

def test_auto_add_to_list():
    catalogue_manager = CatalogueManager
    number_of_candles = catalogue_manager.number_of_candles()
    assert number_of_candles == 1


def test_get_candle_by_id():
    catalogue_manager = CatalogueManager
    retrieved_candle = catalogue_manager.get_candle(100)
    assert retrieved_candle.__str__() == 'Name = name1 | ID = 100 | Fragrance = fragrance | Candle Type = jar | Burn Time = 1.5hr | Diameter x Height = 20.0cm x 20.0cm | Price = £9.99'


def test_update_candle_by_price():
    catalogue_manager = CatalogueManager
    updated_candle_price = catalogue_manager.update_candle_price(100, 29.99)
    assert updated_candle_price.__str__() == 'Name = name1 | ID = 100 | Fragrance = fragrance | Candle Type = jar | Burn Time = 1.5hr | Diameter x Height = 20.0cm x 20.0cm | Price = £29.99'


def test_list_all_candles_single_entry():
    catalogue_manager = CatalogueManager
    list_of_candles = catalogue_manager.list_all_candles()
    assert list_of_candles == 'All Candles:\nName = name1 | ID = 100 | Fragrance = fragrance | Candle Type = jar | Burn Time = 1.5hr | Diameter x Height = 20.0cm x 20.0cm | Price = £29.99\n'


def test_delete_candle():
    catalogue_manager = CatalogueManager
    catalogue_manager.delete_candle(100)
    number_of_candles = catalogue_manager.number_of_candles()
    assert number_of_candles == 0


def test_list_all_candles_multiple_entries():
    catalogue_manager = CatalogueManager
    catalogue_manager.add_candle('name1', 100, 'fragrance', 'jar', 1.5, 20.0, 20.0, 9.99)  
    catalogue_manager.add_candle('name2', 200, 'fragrance', 'jar', 2, 10.0, 10.0, 19.99)
    list_of_candles = catalogue_manager.list_all_candles()
    assert list_of_candles == 'All Candles:\nName = name1 | ID = 100 | Fragrance = fragrance | Candle Type = jar | Burn Time = 1.5hr | Diameter x Height = 20.0cm x 20.0cm | Price = £9.99\nName = name2 | ID = 200 | Fragrance = fragrance | Candle Type = jar | Burn Time = 2hr | Diameter x Height = 10.0cm x 10.0cm | Price = £19.99\n'

    CatalogueManager.delete_candle(100)
    CatalogueManager.delete_candle(200)


def test_square_candle_has_side_not_diameter():
    catalogue_manager = CatalogueManager
    candle = catalogue_manager.add_candle('name', 100, 'fragrance', 'square', 1.5, 20.0, 20.0, 9.99)
    assert candle.__str__() == 'Name = name | ID = 100 | Fragrance = fragrance | Candle Type = square | Burn Time = 1.5hr | Side x Height = 20.0cm x 20.0cm | Price = £9.99'
    catalogue_manager.delete_candle(100)


def test_candle_type_is_valid():
    catalogue_manager = CatalogueManager
    candle = catalogue_manager.add_candle('name', 100, 'fragrance', 'pillar', 1.5, 20.0, 20.0, 9.99)
    assert candle.__str__() == 'Name = name | ID = 100 | Fragrance = fragrance | Candle Type = pillar | Burn Time = 1.5hr | Diameter x Height = 20.0cm x 20.0cm | Price = £9.99'
    catalogue_manager.delete_candle(100)

    candle = catalogue_manager.add_candle('name', 100, 'fragrance', 'square', 1.5, 20.0, 20.0, 9.99)
    assert candle.__str__() == 'Name = name | ID = 100 | Fragrance = fragrance | Candle Type = square | Burn Time = 1.5hr | Side x Height = 20.0cm x 20.0cm | Price = £9.99'
    catalogue_manager.delete_candle(100)

    candle = catalogue_manager.add_candle('name', 100, 'fragrance', 'jar', 1.5, 20.0, 20.0, 9.99)
    assert candle.__str__() == 'Name = name | ID = 100 | Fragrance = fragrance | Candle Type = jar | Burn Time = 1.5hr | Diameter x Height = 20.0cm x 20.0cm | Price = £9.99'
    catalogue_manager.delete_candle(100)

    candle = catalogue_manager.add_candle('name', 100, 'fragrance', 'votive', 1.5, 20.0, 20.0, 9.99)
    assert candle.__str__() == 'Name = name | ID = 100 | Fragrance = fragrance | Candle Type = votive | Burn Time = 1.5hr | Diameter x Height = 20.0cm x 20.0cm | Price = £9.99'
    catalogue_manager.delete_candle(100)

    candle = catalogue_manager.add_candle('name', 100, 'fragrance', 'tealight', 1.5, 20.0, 20.0, 9.99)
    assert candle.__str__() == 'Name = name | ID = 100 | Fragrance = fragrance | Candle Type = tealight | Burn Time = 1.5hr | Diameter x Height = 20.0cm x 20.0cm | Price = £9.99'
    catalogue_manager.delete_candle(100)


#-----------------------------------------------------
#Exceptions
#-----------------------------------------------------


def test_name_is_not_str():
    with pytest.raises(TypeError):
        assert CatalogueManager.add_candle(23, 1, 'fragrance', 'jar', 1, 1.0, 1.0, 1.0)

    with pytest.raises(TypeError):
        assert CatalogueManager.add_candle(10.0, 100, 'fragrance', 'jar', 1, 1.0, 1.0, 1.0)

    with pytest.raises(TypeError):
        assert CatalogueManager.add_candle(True, 100, 'fragrance', 'jar', 1, 1.0, 1.0, 1.0)


def test_id_is_not_int():
    with pytest.raises(TypeError):
        assert CatalogueManager.add_candle('name', 'id', 'fragrance', 'jar', 1, 1.0, 1.0, 1.0)

    with pytest.raises(TypeError):
        assert CatalogueManager.add_candle('name', 1.1, 'fragrance', 'jar', 1, 1.0, 1.0, 1.0)

    with pytest.raises(TypeError):
        assert CatalogueManager.add_candle('name', True, 'fragrance', 'jar', 1, 1.0, 1.0, 1.0)


def test_fragrance_is_not_string():
    with pytest.raises(TypeError):
        assert CatalogueManager.add_candle('name', 1, 1, 'jar', 1, 1.0, 1.0, 1.0)

    with pytest.raises(TypeError):
        assert CatalogueManager.add_candle('name', 1, 1.1, 'jar', 1, 1.0, 1.0, 1.0)

    with pytest.raises(TypeError):
        assert CatalogueManager.add_candle('name', 1, True, 'jar', 1, 1.0, 1.0, 1.0)


def test_candle_type_is_not_string():
    with pytest.raises(TypeError):
        assert CatalogueManager.add_candle('name', 1, 'fragrance', 1, 1, 1.0, 1.0, 1.0)

    with pytest.raises(TypeError):
        assert CatalogueManager.add_candle('name', 1, 'fragrance', 1.0, 1, 1.0, 1.0, 1.0)

    with pytest.raises(TypeError):
        assert CatalogueManager.add_candle('name', 1, 'fragrance', True, 1, 1.0, 1.0, 1.0)


def test_candle_type_is_not_in_valid_list():
    with pytest.raises(ValueError):
        assert CatalogueManager.add_candle('name', 1, 'fragrance', 'dinner', 1, 1.0, 1.0, 1.0)


def test_burn_time_is_not_int_or_float():
    with pytest.raises(TypeError):
        assert CatalogueManager.add_candle('name', 1, 'fragrance', 'jar', 'one', 1.0, 1.0, 1.0)

    with pytest.raises(TypeError):
        assert CatalogueManager.add_candle('name', 1, 'fragrance', 'jar', True, 1.0, 1.0, 1.0)


def test_diam_or_side_is_not_float():
    with pytest.raises(TypeError):
        assert CatalogueManager.add_candle('name', 1, 'fragrance', 'jar', 1, 1, 1.0, 1.0)

    with pytest.raises(TypeError):
        assert CatalogueManager.add_candle('name', 1, 'fragrance', 'jar', 1, 'str', 1.0, 1.0)

    with pytest.raises(TypeError):
        assert CatalogueManager.add_candle('name', 1, 'fragrance', 'jar', 1, True, 1.0, 1.0)


def test_height_is_not_float():
    with pytest.raises(TypeError):
        assert CatalogueManager.add_candle('name', 1, 'fragrance', 'jar', 1, 1.0, 1, 1.0)

    with pytest.raises(TypeError):
        assert CatalogueManager.add_candle('name', 1, 'fragrance', 'jar', 1, 1.0, 'str', 1.0)

    with pytest.raises(TypeError):
        assert CatalogueManager.add_candle('name', 1, 'fragrance', 'jar', 1, 1.0, True, 1.0)


def test_price_is_not_float():
    with pytest.raises(TypeError):
        assert CatalogueManager.add_candle('name', 1, 'fragrance', 'jar', 1, 1.0, 1.0, 1)

    with pytest.raises(TypeError):
        assert CatalogueManager.add_candle('name', 1, 'fragrance', 'jar', 1, 1.0, 1.0, 'one')

    with pytest.raises(TypeError):
        assert CatalogueManager.add_candle('name', 1, 'fragrance', 'jar', 1, 1.0, 1.0, True)


def test_adding_a_candle_currently_in_existence():
    CatalogueManager.add_candle('name', 100, 'fragrance', 'jar', 1, 1.0, 1.0, 1.0)
    with pytest.raises(ValueError):
        assert CatalogueManager.add_candle('name', 100, 'fragrance', 'jar', 1, 1.0, 1.0, 1.0)
    CatalogueManager.delete_candle(100)


def test_adding_a_candle_with_existing_id():
    CatalogueManager.add_candle('name1', 100, 'fragrance', 'jar', 1, 1.0, 1.0, 1.0)
    with pytest.raises(ValueError):
        assert CatalogueManager.add_candle('name', 100, 'fragrance1', 'jar', 1, 1.0, 1.0, 1.0)


def test_get_candle_is_not_valid_type():
    with pytest.raises(TypeError):
        assert CatalogueManager.get_candle('string')
    with pytest.raises(TypeError):
        assert CatalogueManager.get_candle(1.0)
    with pytest.raises(TypeError):
        assert CatalogueManager.get_candle(True)


def test_get_candle_not_in_catalogue():
    with pytest.raises(ValueError):
        assert CatalogueManager.get_candle(999)


def test_delete_candle_is_not_valid_type():
    with pytest.raises(TypeError):
        assert CatalogueManager.delete_candle('string')
    with pytest.raises(TypeError):
        assert CatalogueManager.delete_candle(1.1)
    with pytest.raises(TypeError):
         assert CatalogueManager.delete_candle(False)
       

def test_delete_candle_not_in_catalogue():
    with pytest.raises(ValueError):
        assert CatalogueManager.delete_candle(999)


def test_update_price_is_not_valid_ID_input():
    with pytest.raises(TypeError):
        assert CatalogueManager.update_candle_price('string', 9.99)
    with pytest.raises(TypeError):
        assert CatalogueManager.update_candle_price(1.1, 9.99)
    with pytest.raises(TypeError):
        assert CatalogueManager.update_candle_price(True, 9.99)


def test_update_price_is_not_valid_price_input():
    with pytest.raises(TypeError):
        assert CatalogueManager.update_candle_price(100, 'string')
    with pytest.raises(TypeError):
        assert CatalogueManager.update_candle_price(1.100, 0)
    with pytest.raises(TypeError):
        assert CatalogueManager.update_candle_price(100, True)


def test_update_price_id_is_not_in_catalogue():
    with pytest.raises(ValueError):
        assert CatalogueManager.update_candle_price(999, 9.99)
