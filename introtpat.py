#!/usr/bin/python3

# introtpat.py

# (partial) reimplentation of https://demonstrations.wolfram.com/IntegerRotationPatterns/

from math import sin, cos, radians as rad

def save_svg(filename, data):
    with open(filename, 'w') as f:
        f.write("""<?xml version="1.0" standalone="no"?><svg width="256" height="256" version="1.1" xmlns="http://www.w3.org/2000/svg">""")

        for line in data:
            # "+'\n'" to make readable
            f.write(line)

        # debug
        #f.write("""<circle cx="128" cy="128" r="2" fill="red"/>""")

        # from view-source of the original:
        # 192px Arimo, Arial or Sans Serif with weight of 400 (default) and normal style
        # Arial is a proprietary font that is substituted with Liberation Sans on my system
        # should look into Arimo from Google Fonts as a free alternative
        f.write("""<style><![CDATA[text{font: 192px Arial;}]]></style>""")

        f.write("""</svg>""")

def calculate_xy(origo, i, symmetry, offset):
    alpha = i * 360/symmetry

    x = origo + offset * cos(rad(alpha))
    y = origo + offset * sin(rad(alpha))

    return x,y

def create_pattern(origo, text, symmetry, rotation, offset):
    pattern = []
    # https://stackoverflow.com/questions/12250403/vertical-alignment-of-text-element-in-svg/15997503#15997503
    other = ' dominant-baseline="central"' # doesn't work in Chrome! -> remove & research new values...
    for i in range(0,symmetry):
        x,y = calculate_xy(origo, i, symmetry, offset)
        pattern.append(f'<text x="{x}" y="{y}" rotate="{(i+1)*(360/symmetry)+rotation}"{other}>{text}</text>')
    return pattern

def create_svg(text, symmetry, rotation, offset):
    return create_pattern(128, text, symmetry, rotation, offset)

if __name__ == "__main__":
    #TODO: remove "other" && recreate

    # I call this one "Sharing ninjas"
    save_svg("introt.svg", create_svg(3, 9, 352.369, 21.5))
    # This one is called "Concentrated knowledge"
    save_svg("docs.svg", create_svg(3, 9, 317, 21.5))

