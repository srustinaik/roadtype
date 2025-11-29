import sys

# Expect: python trip.py <distance> <speed> <road_type>
if len(sys.argv) != 4:
    print("Usage: python trip.py <distance> <speed> <road_type>")
    sys.exit(1)

distance = float(sys.argv[1])
speed = float(sys.argv[2])
road_type = sys.argv[3].lower()

# Simple fuel efficiency assumptions (km per liter)
efficiency = {"highway": 15, "city": 10, "offroad": 8}

if road_type not in efficiency:
    print("Road type must be: highway, city, or offroad")
    sys.exit(1)

time = distance / speed
fuel = distance / efficiency[road_type]

print("Trip time:", round(time, 2), "hours")
print("Fuel used:", round(fuel, 2), "liters")
