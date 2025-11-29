import sys
print("Trip Time & Fuel Usage Estimator")
if len(sys.argv) == 4:
    distance = float(sys.argv[1])
    speed = float(sys.argv[2])
    road_type = sys.argv[3].lower()
else:
    distance = 100
    speed = 60
    road_type = "city"
    print("\nArguments not provided – using default values:")
    print("Distance = 100 km")
    print("Speed = 60 km/h")
    print("Road type = city")
if road_type == "highway":
    efficiency = 15
elif road_type == "city":
    efficiency = 10
elif road_type == "offroad":
    efficiency = 8
else:
    print("\nRoad type must be highway, city, or offroad")
    sys.exit(1)
time = distance / speed
fuel = distance / efficiency
print("\nTrip time =", round(time, 2), "hours")
print("Fuel used =", round(fuel, 2), "liters")
