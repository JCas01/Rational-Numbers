SUPER_NUMS = ['⁰', '¹', '²', '³', '⁴', '⁵', '⁶', '⁷', '⁸', '⁹']
SUB_NUMS = ['₀', '₁', '₂', '₃', '₄', '₅', '₆', '₇', '₈', '₉']

def strangeSuperScript(number):
  output = ""
  number = int(number)
  for digit in str(number):
    digit = int(digit)
    output += SUPER_NUMS[digit]
  return output


def strangeSubScript(number):
  output = ""
  number = int(number)
  for digit in str(number):
    digit = int(digit)
    output += SUB_NUMS[digit]
  return output

def gcd(a, b):
  """
  Returns the Greatest Common Divisor between `a` and `b`.
  """
  while b:
    a, b = b, a % b
  return a


class Rational:
  """
  Represents any rational number in fraction form.
  """
  
  def __init__(self, numerator, denominator=1):
    self.numerator = numerator
    self.denominator = denominator
    
  def __eq__(a, b):
    return str(a) == str(b)

  def __str__(self):
    """
    Returns a string representing this Rational number.
    """
    mult = 0
    numNeg = False
    output = ""
    divisor = gcd(self.numerator, self.denominator)
    numerator = self.numerator / divisor
    denominator = self.denominator / divisor
    if numerator < 0:
      numNeg = True
      numerator = numerator* -1
    while numerator > denominator:
      numerator -= denominator
      mult += 1
    if numNeg:
      output += "-"
    if mult > 0:
      output += str(mult)

    output += strangeSuperScript(numerator) + "/" + strangeSubScript(denominator)
    
    if numerator == denominator:
      mult += 1
      output = str(mult)
    elif numerator == 0:
      output = str(0)
    return output
  
  def __add__(a, b):
    denom = a.denominator * b.denominator
    nom = a.numerator * b.denominator + b.numerator * a.denominator
    return Rational(nom, denom)
  
  def __mul__(a, b):
    return Rational(a.numerator * b.numerator, a.denominator * b.denominator)

  def __sub__(a, b):
    denom = a.denominator * b.denominator
    nom = a.numerator * b.denominator - b.numerator * a.denominator
    return Rational(nom, denom)
  
  def __truediv__(a, b):
    return a * Rational(b.denominator, b.numerator)


def test_rational():
  x = Rational(684, 857)
  y = Rational(100, 20)
  print(x)
  print(y)
