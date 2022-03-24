cake_01 = {
    "taste": 'vanilia',
    "glaze": 'chocolade',
    "text": 'Happy Brithday',
    "weight": 0.7}

cake_02 = {
    "taste": 'tee',
    "glaze": 'lemon',
    "text": 'Happy Python Coding',
    "weight": 1.3}


def show_cake_info(piece_of_cake):
    print('{} cake with {} glaze with text "{}" of {} kg'.format(
        piece_of_cake["taste"], piece_of_cake["glaze"], piece_of_cake["text"], piece_of_cake["weight"]))


cakes_list = [cake_01, cake_02]
for cake in cakes_list:
    show_cake_info(cake)

