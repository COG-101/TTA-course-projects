from classes.candle_class import Candle
import locale
locale.setlocale(locale.LC_ALL, 'en_GB')

class CatalogueManager():
    list_of_candles = []


    def __init__(self):
        pass


    def list_all_candles():
        format_to_print = 'All Candles:\n'
        for candle in CatalogueManager.list_of_candles:
            format_to_print += (f'{candle.__str__()}\n')
        return format_to_print


    def add_candle(name, id, fragrance, candle_type, burn_time, diam_or_side, height, price):
        candle = Candle(name, id, fragrance, candle_type, burn_time, diam_or_side, height, price) 
        for item in CatalogueManager.list_of_candles:
            if item.__dict__ == candle.__dict__:
                raise ValueError('This candle currently exists within the catalogue')  
            elif id == item.id: 
                raise ValueError('A candle with this ID currently exists in the catatlogue.')    
        CatalogueManager.list_of_candles.append(candle) 
        return candle


    def get_candle(id):
        if not isinstance(id, int) or isinstance(id, bool):
            raise TypeError('ID must be an integer')
        is_candle_listed = False
        for candle in CatalogueManager.list_of_candles:
            if id == candle.id:
                is_candle_listed = True
                return candle
        if is_candle_listed == False:
            raise ValueError('There is no candle with that ID. Please try again.')


    def delete_candle(id):
        if not isinstance(id, int) or isinstance(id, bool):
            raise TypeError('ID must be an integer') 
        is_candle_listed = False
        for candle in CatalogueManager.list_of_candles:
            if id == candle.id:
                is_candle_listed = True
                CatalogueManager.list_of_candles.remove(candle)
        if is_candle_listed == False:
            raise ValueError('Item cannot be deleted as it is not found in the catalogue')            


    def update_candle_price(id, new_price):
        if not isinstance(id, int) or isinstance(id, bool):
            raise TypeError('ID must be an integer')  
        if not isinstance(new_price, float) or isinstance(new_price, bool):
            raise TypeError('Price must be a float') 
        is_candle_listed = False
        new_price = locale.currency(new_price, grouping=True)
        for candle in CatalogueManager.list_of_candles:
            if id == candle.id:
                is_candle_listed = True
                candle.price = new_price
                return candle   
        if is_candle_listed == False:
            raise ValueError('Price cannot be updated as ID is not found')


    def number_of_candles():
        count = len(CatalogueManager.list_of_candles)
        return count
