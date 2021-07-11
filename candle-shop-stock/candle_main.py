from classes.catalogue_manager_class import CatalogueManager


# Adding Candles:
CatalogueManager.add_candle('Candle1', 100, 'vanilla', 'jar', 5, 30.0, 30.0, 19.99)
CatalogueManager.add_candle('Candle2', 200, 'Raspberry', 'tealight', 9, 40.0, 40.0, 29.99)

print('--------------------------------------')

# Getting Candle with ID
print(CatalogueManager.get_candle(100))
print('--------------------------------------')

# Printing List of Candles:
print(CatalogueManager.list_all_candles())
print('--------------------------------------')

# Deleting Candle 
CatalogueManager.delete_candle(100)
print(CatalogueManager.list_all_candles())
print('--------------------------------------')

# Update Candle Price
print(CatalogueManager.update_candle_price(200, 99.99))
print('--------------------------------------')

