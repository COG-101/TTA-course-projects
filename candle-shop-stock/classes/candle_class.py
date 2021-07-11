import locale
locale.setlocale(locale.LC_ALL, 'en_GB')

class Candle():
    name = ''
    id = 0
    fragrance = ''
    candle_type = ''
    burn_time = 0
    diam_or_side = 0
    height = 0
    price = 0

    def __init__(self, name, id, fragrance, candle_type, burn_time, diam_or_side, height, price):
        valid_candle_type = ['pillar', 'square', 'jar', 'votive', 'tealight']

        self.name = name
        self.id = id
        self.fragrance = fragrance
        self.candle_type = candle_type
        self.burn_time = f'{burn_time}hr'
        self.diam_or_side = f'{diam_or_side}cm'
        self.height = f'{height}cm'
        self.price = locale.currency(price, grouping=True)
        
        if not isinstance(name, str):
            raise TypeError('Name must be a string')
        if not isinstance(id, int) or isinstance(id, bool):
            raise TypeError('ID must be an integer')
        if not isinstance(fragrance, str):
            raise TypeError('Fragrance must be a string')
        if not isinstance(candle_type, str):
            raise TypeError('Candle Type must be a string')
        if candle_type.lower() not in valid_candle_type:
            raise ValueError(f'Invaid candle type, valid types include: {valid_candle_type}')
        if not isinstance(burn_time, (int, float)) or isinstance(burn_time, bool):
            raise TypeError('Burn Time must be an int or a float')
        if not isinstance(diam_or_side, float):
            raise TypeError('Diameter/Side must be a float')
        if not isinstance(height, float):
            raise TypeError('Height must be an float ')
        if not isinstance(price, float):
            raise TypeError('Price must be an float ')   


    def __str__(self):
        diam_or_side = 'Diameter'
        if self.candle_type.lower() == 'square':
            diam_or_side = 'Side'
        return f'Name = {self.name} | ID = {self.id} | Fragrance = {self.fragrance} | Candle Type = {self.candle_type} | Burn Time = {self.burn_time} | {diam_or_side} x Height = {self.diam_or_side} x {self.height} | Price = {self.price}'
         