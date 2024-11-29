def main():
  fraction = input("Enter a fraction as X/Y: ")
  percentage = convert(fraction)
  gauge_reading = gauge(percentage)
  print(f"Gauge: {gauge_reading}")
  
def convert(fraction):
    numerator, denominator = fraction.split("/")
    numerator = int(numerator)
    denominator = int(denominator)
    percentage = round((numerator / denominator) * 100)
    return percentage

def gauge(percentage):
    if percentage <= 1:
        return "E" 
    elif percentage >= 99:
       return "F"
    else:
       return f"{percentage}%"

if __name__ == "__main__":
    main()
