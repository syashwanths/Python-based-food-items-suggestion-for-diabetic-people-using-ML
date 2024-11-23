def extract_nutrition_info(filename):
    nutrition_dict = {}
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split(' ', 1)
            key = parts[0]
            value = parts[1] if len(parts) > 1 else ""  
            if key in ['TotalCarbohydrate','Sugars']:
                if key in nutrition_dict:
                    nutrition_dict[key] += ', ' + value  # Accumulate values for duplicate keys
                else:
                    nutrition_dict[key] = value
    return nutrition_dict

filename = ('output.txt')
nutrition_info = extract_nutrition_info('output.txt')
print(nutrition_info)

def sum_nutrition_values(nutrition_dict):
    total_sum = 0
    for value in nutrition_dict.values():
        # Split the values by comma and convert to float before summing
        values = value.split(', ')
        total_sum += sum(float(v) for v in values if v.isdigit() or v.replace('.', '', 1).isdigit())
    return total_sum

nutrition_info = extract_nutrition_info('output.txt')
# print(nutrition_info)

# Calculate the sum of the numeric values in the dictionary
total_value_sum = sum_nutrition_values(nutrition_info)
print(f"Total sum of nutrition values: {total_value_sum}")