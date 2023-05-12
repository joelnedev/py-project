import math
import json

# Load instrument data from JSON file
with open("./instruments.json", "r") as in_file:
	loaded = json.load(in_file)
	guitar_attributes = loaded["guitarAttributes"]
	bass_attributes = loaded["bassAttributes"]
	guitars = loaded["guitars"]
	basses = loaded["basses"]

# Set up the main menu
def user_interface():
	print("**** GUITAR FINDER ****\n")
	print("Welcome to the guitar finder! This program will help you find the guitar or bass of your dreams, based on your preferences for various specs.\n")

	while True:
		print("\n")
		print("____ Guitar or Bass? ____")
		print("1. Find a guitar")
		print("2. Find a bass")
		print("0. Quit")

		choice = input("Menu selection: ")

		# Handle user's choice
		match choice:
			case "1":
				guitar_menu()
			case "2":
				bass_menu()
			case "0":
				print("Goodbye!")
				return
			case _:
				print("Invalid selection, please try again")

def guitar_menu():
	print("\n")
	print("1. Find a guitar by model name")
	print("2. Find a guitar by price")
	print("3. Find a guitar by pickup configuration")
	print("4. Find a guitar by pickup switch")
	print("5. Find a guitar by bridge")
	print("6. Find a guitar by hardware configuration")
	print("7. Go back")
	print("")
	choice = input("Menu selection: ")

	# Handle user's choice in the guitar menu
	match choice:
		case "1":
			find_by_model("guitar")
		case "2":
			find_by_price("guitar")
		case "3":
			find_by_pickup_config("guitar")
		case "4":
			find_by_pickup_switch()
		case "5":
			find_by_bridge()
		case "6":
			find_by_hardware_config("guitar")
		case "7":
			return
		case _:
			print("Invalid selection, please try again")

def bass_menu():
	print("\n")
	print("1. Find a bass by model name")
	print("2. Find a bass by price")
	print("3. Find a bass by pickup configuration")
	print("4. Find a bass by hardware configuration")
	print("5. Go back")
	print("")
	choice = input("Menu selection: ")

	# Handle user's choice in the bass menu
	match choice:
		case "1":
			find_by_model("bass")
		case "2":
			find_by_price("bass")
		case "3":
			find_by_pickup_config("bass")
		case "4":
			find_by_hardware_config("bass")
		case "5":
			return
		case _:
			print("Invalid selection, please try again")

def find_by_model(g_type):
	print(f"Find a {g_type} by model name")
	print("")
	model = input("Enter a model name: ")
	print("")
	found = []

	# Search for the specified model in the guitars or basses list
	for guitar in (guitars if (g_type == "guitar") else basses):
		gtr = (guitars if (g_type == "guitar") else basses)[guitar]
		model_match = gtr["model"].lower() == model.lower()
		brand_match = gtr["brand"].lower() == model.lower()
		nick_match = guitar.lower() == model.lower()
		bm_match = f"{gtr['brand'].lower()} {gtr['model'].lower()}" == model.lower()
		bn_match = f"{gtr['brand'].lower()} {guitar.lower()}" == model.lower()
		if model_match or brand_match or nick_match or bm_match or bn_match:
			found.append(gtr)
			break

	if not found: print("No match found.")
	else: print_guitar(found)

def find_by_price(g_type):
	print(f"Find a {g_type} by price")
	print("")
	price = input("Enter a price: ")
	print("")

	# Search for guitars or basses with prices close to the specified price
	found = []
	for guitar in (guitars if (g_type == "guitar") else basses):
		gtr = (guitars if (g_type == "guitar") else basses)[guitar]
		if math.isclose(gtr["price"], float(price), rel_tol=1e-3, abs_tol=500):
			found.append(gtr)

	print_guitar(found)

def find_by_pickup_config(g_type):
	print(f"Find a {g_type} by pickup configuration")
	print("")

	# Display available pickup options
	pickups = (guitar_attributes if (g_type == "guitar") else bass_attributes).get("pickups")
	selections = []
	for i, option in enumerate(pickups, start=1):
		print(f"{i}. {option}")
	selected = input("Enter the numbers corresponding to your choices: ").split()
	if not selected or any(not index.isdigit() or int(index) < 1 or int(index) > len(pickups) for index in selected):
		print("Invalid input. Please enter valid indices.")
	else:
		# Process selected indices
		selections = [pickups[int(index) - 1] for index in selected]


	# Search for guitars or basses with matching pickup configurations
	found = []
	for guitar in (guitars if (g_type == "guitar") else basses):
		gtr = (guitars if (g_type == "guitar") else basses)[guitar]
		if any(pickup in gtr["stats"]["pickups"] for pickup in selections):
			found.append(gtr)

	print_guitar(found)

def find_by_pickup_switch():
	print("Find a guitar by pickup switch")
	print("")

	# Display available switch options
	switches = guitar_attributes.get("switch")
	selections = []
	for i, option in enumerate(switches, start=1):
		print(f"{i}. {option}")
	selected = input("Enter the numbers corresponding to your choices: ").split()
	if not selected or any(not index.isdigit() or int(index) < 1 or int(index) > len(switches) for index in selected):
		print("Invalid input. Please enter valid indices.")
	else:
		# Process selected indices
		selections = [switches[int(index) - 1] for index in selected]


	# Search for guitars with matching pickup switches
	found = []
	for guitar in guitars:
		gtr = guitars[guitar]
		if any(switch in gtr["stats"]["switch"] for switch in selections):
			found.append(gtr)

	print_guitar(found)

def find_by_bridge():
	print("Find a guitar by bridge")
	print("")

	# Display available bridge options
	bridges = guitar_attributes.get("bridge")
	selections = []
	for i, option in enumerate(bridges, start=1):
		print(f"{i}. {option}")
	selected = input("Enter the numbers corresponding to your choices: ").split()
	if not selected or any(not index.isdigit() or int(index) < 1 or int(index) > len(bridges) for index in selected):
		print("Invalid input. Please enter valid indices.")
	else:
		# Process selected indices
		selections = [bridges[int(index) - 1] for index in selected]


	# Search for guitars with matching bridges
	found = []
	for guitar in guitars:
		gtr = guitars[guitar]
		if any(bridge in gtr["stats"]["bridge"] for bridge in selections):
			found.append(gtr)

	print_guitar(found)

def find_by_hardware_config(g_type):
	print(f"Find a {g_type} by hardware configuration")
	print("")

	# Display available hardware options
	hardware = (guitar_attributes if (g_type == "guitar") else bass_attributes).get("hardware") 
	if (g_type == "guitar"):
		hardware = hardware + guitar_attributes.get("hardwareFeatures")
	selections = []
	for i, option in enumerate(hardware, start=1):
		print(f"{i}. {option}")
	selected = input("Enter the numbers corresponding to your choices: ").split()
	if not selected or any(not index.isdigit() or int(index) < 1 or int(index) > len(hardware) for index in selected):
		print("Invalid input. Please enter valid indices.")
	else:
		# Process selected indices
		selections = [hardware[int(index) - 1] for index in selected]

	# Search for guitars or basses with matching hardware configurations
	found = []
	for guitar in (guitars if (g_type == "guitar") else basses):
		gtr = (guitars if (g_type == "guitar") else basses)[guitar]
		if any(hardware in gtr["stats"]["hardware"] for hardware in selections):
			found.append(gtr)
		if any(hardware in gtr["stats"]["hardware"][0] for hardware in selections):
			found.append(gtr)

	print_guitar(found)

# Print guitar or bass information; passed a list of guitars or basses within another menu function
def print_guitar(guitars):
	print("\n\n")
	for guitar in guitars:
		# Extract guitar attributes
		switch = ""
		bridge = ""
		pup_config = ""
		hardware = []
		hardware_features = []
		stats = guitar["stats"]

		# Determine switch and bridge configuration
		if guitar["type"] == "guitar":
			switch = f"{stats['switch'][0]} {stats['switch'][1]}"
			bridge = f"{stats['bridge'][1]} {stats['bridge'][0]}"

		# Determine pickup configuration
		pup_config = {
			"H": "Humbucker",
			"HH": "Humbucker/Humbucker",
			"HHH": "Humbucker/Humbucker/Humbucker",
			"S": "Single Coil",
			"SS": "Single Coil/Single Coil",
			"SSS": "Single Coil/Single Coil/Single Coil"
		}.get(stats["pickups"], "")

		# Determine hardware configuration
		for hardware_item in stats["hardware"][0]:
			if hardware_item == "1V":
				hardware.append("1 Volume")
			elif hardware_item == "2V":
				hardware.append("2 Volume")
			elif hardware_item == "1T":
				hardware.append("1 Tone")
			elif hardware_item == "2T":
				hardware.append("2 Tone")

		# Determine hardware features
		for feature in stats["hardware"]:
			if type(feature) != list:
				hardware_features.append(feature)

		# Print guitar information
		print(f"Model: {guitar['brand']} {guitar['model']}")
		print(f"Price: ${guitar['price']}")
		print(f"Pickup Configuration: {pup_config}")
		if guitar["type"] == "guitar":
			print(f"Pickup Switch: {switch}")
			print(f"Bridge: {bridge}")
		print(f"Hardware Configuration: {', '.join(hardware)}")
		print(f"Hardware Features: {', '.join(hardware_features)}")
		print("")

try:
	user_interface()
	pass
except KeyboardInterrupt:
	pass
