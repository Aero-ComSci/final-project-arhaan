def process_temperatures(temps):
    result = []
    for temp in temps:
        temp = temp.strip()
        if temp.isdigit():
            temp = int(temp)
            if 70 <= temp <= 85:  
                status = "Perfect beach day!"
            elif temp > 85:
                status = "Too hot! Stay hydrated!"
            elif 60 <= temp <= 70:
                status = "Cool breeze—bring a light jacket!"
            else:
                status = "Very cold! Bring a heavy jacket."
            result.append(str(temp) + "°F - " + status)
        else:
            print("Invalid temp. Rerun Program.")
    return result

def main():
    user_input = input("Enter average temperatures(throughout the week) separated by commas (Example: 72, 85, 95): ")
    temps = user_input.split(",")
    results = process_temperatures(temps)  
    output_data = "\n".join(results)  
    print("\nSummer Forecast:")
    print(output_data)
main()
