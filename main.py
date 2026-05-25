actual_yields =      [45, 80, 30, 90]
theoretical_yields = [50, 90, 80, 95]
def percentage_yield(actual_yields, theoretical_yields):
    result = []
    for actual, theoretical in zip(actual_yields, theoretical_yields):
        percentage = (actual / theoretical) * 100
        percentage = round(percentage, 1)

        if percentage < 60:
            message = "Low yield"
        else:
            message = "Acceptable"
        result.append(f"{percentage}% -> {message}")
    return result
percentages = percentage_yield(actual_yields, theoretical_yields)

for index, result in enumerate(percentages, start=1):
    print(f"Experiment {index}: {result}")


