def main():
  fraction = input("Enter a fraction as X/Y: ")
  percentage = convert(fraction)
  result = gauge(percentage)
  print(f"percentage: {percentage}")
  print(f"Gauge: {result}")
  
def convert(fraction):
    numerator, denominator = fraction.split("/")
    numerator = int(numerator)
    denominator = int(denominator)
    percentage = round((numerator/denominator)*100)
    return percentage

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
       return "F"
    else:
       return "Z%"

if __name__ == "__main__":
 main()
