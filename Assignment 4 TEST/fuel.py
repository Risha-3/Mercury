def main():
  """
  
  """
  fraction = input("Enter a fraction as X/Y: ")
  try:
    percentage = convert(fraction)
    gauge_reading = gauge(percentage)
    print(f"Gauge: {gauge_reading}")
  except ZeroDivisionError as e:
    print(f"ERROR: {e}")
  except ValueError as e:
    print(f"ERROR: {e}")
  
def convert(fraction):
  """

  """
  numerator, denominator = fraction.split("/")
  numerator = int(numerator)
  denominator = int(denominator)
  if denominator == 0:
    raise ZeroDivisionError("Y cannot be 0 in X/Y.")
  if numerator > denominator:
    raise ValueError("X must be less than or equal to Y.")
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
