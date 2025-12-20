def calculate_area(radius :float) -> float :
    """Returns area of circle. Input float."""
    if radius < 0:
        return 0
    return 3.14 * (radius**2)

## main execuition
r=5
print(calculate_area(r))