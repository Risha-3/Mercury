def main():
  """
  This function asks the user to enter a fraction (X/Y).
  Converts fraction to a percentage using the convert function.
  Using the gauge function, an appropriate gauge reading is displayed based on the percentage. 
  """
  fraction = input("Enter a fraction as X/Y: ")
  try:
    # Calling the convert and gauge functions.
    percentage = convert(fraction)
    gauge_reading = gauge(percentage)
    print(f"Gauge: {gauge_reading}")
  except ZeroDivisionError:
    # This message is displayed if there is a division by zero. 
    print("Y cannot be 0 in X/Y.")
  except ValueError:
    # This message is displayed if an improper fraction or non-integers are entered.
    print("X and Y must be integers and X must be less than or equal to Y.")
  
def convert(fraction):
  """
  Convert the user input (X/Y) into a percentage.
  """
  # The input X/Y is split into numerator and denominator.
  numerator, denominator = fraction.split("/")
  # Converting the numerator and denominator to integers. A ValueError is raised if it cannot be done.
  numerator = int(numerator)
  denominator = int(denominator)
  # If the denomiator is 0, the convert function raises a ZeroDivisionError.
  if denominator == 0: 
    raise ZeroDivisionError
  # If the user enters an improper fraction, the convert function raises a ValueError.
  if numerator > denominator:
    raise ValueError
  # Calculate and return the percentage.
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
    # If the percentage is greater than 1 and less than 99, the {percentage}% is returned.
    return f"{percentage}%"

if __name__ == "__main__":
    main()
