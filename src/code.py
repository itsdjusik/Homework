def up_first(stroke):
    """Делает первую буквы строки заглавной"""
    if stroke:
        return stroke[0].upper() + stroke[1:]
    else:
        return stroke
