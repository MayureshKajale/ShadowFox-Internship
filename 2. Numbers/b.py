"""
In a village, there is a circular pond with a radius of 84 meters.
Calculate the area of the pond using the formula: Circle Area = π
r^2. (Use the value 3.14 for π) Bonus Question: If there is exactly
1.4 liters of water in a square meter, what is the total amount of
water in the pond? Print the answer without any decimal point in
it. Hint: Circle Area = π r^2 Water in the pond = Pond Area
Water per Square Meter
"""

import math

def calculate_area(radius):
    return math.pi * (radius ** 2)

def calculate_total_water(area, water_per_sq_meter):
    return int(area * water_per_sq_meter)

radius = 84
water_per_sq_meter = 1.4 * 1000
area = calculate_area(radius)
total_water = calculate_total_water(area, water_per_sq_meter)
print(f"Area of the pond: {area} square meters")
print(f"Total amount of water in the pond: {total_water} milliliters")
print(f"Total amount of water in the pond (rounded in liters): {total_water/1000} liters")
