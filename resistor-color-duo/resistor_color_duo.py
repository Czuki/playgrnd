def value(colors):

    return color_code(colors[0]) * 10 + color_code(colors[1])

def color_code(color):
    return colors(color)

def colors(color=False):

    colors_list = [
            "black",
            "brown",
            "red",
            "orange",
            "yellow",
            "green",
            "blue",
            "violet",
            "grey",
            "white",
        ]

    return colors_list.index(color) if color else colors_list
