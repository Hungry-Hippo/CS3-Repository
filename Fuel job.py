
    
def calculate_fuel(cargo_weight):
    if cargo_weight == "satellite":
        weight = 1000
    elif cargo_weight == "rover":
        weight = 2000
    elif cargo_weight == "supplies":
        weight = 500
    else:
        weight = 0
    return weight

cargo_weight = 1
fuel = cargo_weight * 3

cargo_weight = input("Enter cargo weight (satellite/rover/supplies): ")
fuel = calculate_fuel(cargo_weight)

command = input("Type 'launch' to end. Type 'augment'/'postpone' to continue: ")

while True:
    if command == "launch":
        print("Total fuel:", fuel)
        break
    elif command == "augment":
        cargo_weight = input("Enter another cargo weight (satellite/rover/supplies): ")
        fuel = calculate_fuel(cargo_weight)
    elif command == "postpone":
        cargo_weight = input("Enter another cargo weight (satellite/rover/supplies): ")
        fuel = calculate_fuel(cargo_weight)