class_size = 100

for student in range(1, class_size + 1):
    print(f"\nStudent {student}:")

    # Get input for weight and height
    weight = float(input("Enter weight in kg (30 to 100): "))
    height = float(input("Enter height in cm (150, 160, 175): "))

    # Categorize health status based on weight and height
    if 30 <= weight <= 45 and height == 150:
        health_status = "Healthy"
    elif 46 <= weight <= 60 and height == 160:
        health_status = "Average Health"
    elif 61 <= weight <= 100 and height == 175:
        health_status = "Not Healthy"
    else:
        health_status = "Invalid input or not categorized"

    # Print health status
    print(f"Health Status: {health_status}")
