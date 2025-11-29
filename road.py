import sys
if len(sys.argv) == 4:
    distance = float(sys.argv[1])
    speed = float(sys.argv[2])
    road_type = sys.argv[3].lower()
else:
    print("No arguments provided. Using default values...")
    distance = 100
    speed = 20
    road_type = "city"

# Fuel efficiency dictionary
efficiency = {"highway": 15, "city": 10, "offroad": 8}
fuel_eff = efficiency.get(road_type, 12)

# Calculate trip time and fuel usage
time = distance / speed
fuel = distance / fuel_eff

# Output results
print("Trip time:", round(time, 2), "hours")
print("Fuel used:", round(fuel, 2), "liters")
print("Road type:", road_type, "(efficiency used:", fuel_eff, "km/l)")
