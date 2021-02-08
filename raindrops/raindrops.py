def convert(number):

    raindrops = {
    3:'Pling',
    5:'Plang',
    7:'Plong',
    }


    result = [value for key, value in raindrops.items() if not number % key]
    return ''.join(result) if result else str(number)