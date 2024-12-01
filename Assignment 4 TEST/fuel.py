def main():
  """
  
  """
  fraction = input("Enter a fraction as X/Y: ")
  try:
    percentage = convert(fraction)
    gauge_reading = gauge(percentage)
    print(f"Gauge: {gauge_reading}")
  except ZeroDivisionError:
    print("Y cannot be 0 in X/Y.")
  except ValueError:
    print("X must be less than or equal to Y.")
  
def convert(fraction):
  """

  """
  numerator, denominator = fraction.split("/")
  numerator = int(numerator)
  denominator = int(denominator)
  if denominator == 0:
    raise ZeroDivisionError
  if numerator > denominator:
    raise ValueError
  percentage = round((numerator / denominator) * 100)
  return percentage

def gauge(percentage):
  """
  This function returns the gauge reading as a string based on the percentage.
  """
  if percentage <= 1:
    return "E" 
  elif percentage >= 99:
    return "F"
  else:
    return f"{percentage}%"

if __name__ == "__main__":
    main()

# cd "C:\Users\risha\Documents\Mercury repo\Mercury\Assignment 4 TEST"
# pytest test_fuel.py
