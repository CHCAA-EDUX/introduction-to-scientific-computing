"""
# Defensive Programming #

- Write programs that check their own operation.
- Write and run tests for widely-used functions.
- Make sure we know what “correct” actually means.

* A precondition is something that must be true at the start of a function in order for it to work correctly.
* A postcondition is something that the function guarantees is true when it finishes.
* An invariant is something that is always true at a particular point inside a piece of code.


"""


def normalize_rectangle(rect):
    """Normalizes a rectangle so that it is at the origin and 1.0 units long on its longest axis.
    Input should be of the format (x0, y0, x1, y1).
    (x0, y0) and (x1, y1) define the lower left and upper right corners
    of the rectangle, respectively."""
    assert len(rect) == 4, 'Rectangles must contain 4 coordinates'
    x0, y0, x1, y1 = rect
    assert x0 < x1, 'Invalid X coordinates'
    assert y0 < y1, 'Invalid Y coordinates'

    dx = x1 - x0
    dy = y1 - y0
    if dx > dy:
        scaled = float(dx) / dy# should be float(dy) / dx
        #scaled = float(dy) / dx
        upper_x, upper_y = 1.0, scaled
    else:
        scaled = float(dx) / dy
        upper_x, upper_y = scaled, 1.0

    assert 0 < upper_x <= 1.0, 'Calculated upper X coordinate invalid'
    assert 0 < upper_y <= 1.0, 'Calculated upper Y coordinate invalid'

    return (0, 0, upper_x, upper_y)


def main():
    
    ### PRECONDITIONS assertions

    print(normalize_rectangle((0.0, 1.0, 2.0))) # missing fourth coordinate

    print(normalize_rectangle((4., 2., 1., 5.))) # inverted coordinate


    ### 

    ### POSTCONDITION assertions

    # wider than tall is correct
    print(normalize_rectangle((0., 0., 1., 5.)))

    # if not: (would have passed) - taller than wide
    print(normalize_rectangle((0., 0., 5., 1.)))

    # we need to update line float(dy) / dx

if __name__=='__main__':
    main()