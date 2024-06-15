countries = {
    "Australia": ["Sydney", "Melbourne", "Brisbane", "Perth"],
    "UAE": ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"],
    "India": ["Mumbai", "Bangalore", "Chennai", "Delhi"]
}

def find_country(city):
    for country, cities in countries.items():
        if city in cities:
            return country
    return None

city1 = input("Enter the first city: ")
city2 = input("Enter the second city: ")

country1 = find_country(city1)
country2 = find_country(city2)

if country1 and country2:
    if country1 == country2:
        print(f"Both cities are in {country1}")
    else:
        print("They don't belong to the same country")
else:
    if not country1:
        print(f"{city1} is not in the list of known cities.")
    if not country2:
        print(f"{city2} is not in the list of known cities.")
