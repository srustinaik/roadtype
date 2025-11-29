import sys

# Expect: python trip.py <distance> <speed> <road_type>
if len(sys.argv) != 4:
    print("Usage: python trip.py <distance> <speed> <road_type>")
    sys.exit(1)

distance = float(sys.argv[1])
speed = float(sys.argv[2])
road_type = sys.argv[3].lower()

# Fuel efficiency assumptions (km per liter)
efficiency = {"highway": 15, "city": 10, "offroad": 8}

# If road type not in dictionary, use a default value
fuel_eff = efficiency.get(road_type, 12)

time = distance / speed
fuel = distance / fuel_eff

print("Trip time:", round(time, 2), "hours")
print("Fuel used:", round(fuel, 2), "liters")
print("Road type:", road_type, "(efficiency used:", fuel_eff, "km/l)")
