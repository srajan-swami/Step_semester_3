import random


def getBmiStatus(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"


def printWellnessReport(heights, weights):
    print("\nWellness Report")
    print("-" * 65)
    print("Person | Height (m) | Weight (kg) | BMI   | Status")
    print("-" * 65)

    for i in range(len(heights)):
        bmi = weights[i] / (heights[i] * heights[i])
        status = getBmiStatus(bmi)

        print(
            f"{i + 1:<6} | "
            f"{heights[i]:<11.2f} | "
            f"{weights[i]:<11.2f} | "
            f"{bmi:<5.2f} | "
            f"{status}"
        )

    print("-" * 65)


heights = []
weights = []

for i in range(10):
    height = round(random.uniform(1.5, 1.9), 2)
    weight = round(random.uniform(45, 100), 2)

    heights.append(height)
    weights.append(weight)

printWellnessReport(heights, weights)