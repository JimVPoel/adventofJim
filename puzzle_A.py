MIN_VALUE = 0
MAX_VALUE = 100

base = 50

print("Starting base value:", base)

with open("adjustments.txt", "r") as file:
    for line in file:
        line = line.strip()
        if not line:
            continue
        operation, value_str = line.split()
        value = int(value_str)

        if operation == "add":
            base += value
        elif operation == "subtract":
            base -= value
        else:
            print(f"Unknown operation: {operation}")
            continue

        if base < MIN_VALUE:
            base = MIN_VALUE
        elif base > MAX_VALUE:
            base = MAX_VALUE

        print(f"After {operation} {value}: {base}")