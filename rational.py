SUPER_NUMS = ['⁰', '¹', '²', '³', '⁴', '⁵', '⁶', '⁷', '⁸', '⁹']
SUB_NUMS = ['₀', '₁', '₂', '₃', '₄', '₅', '₆', '₇', '₈', '₉']


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
    """
    Initialises a rational number with the given numerator and denominator.
    """
    # TODO implement this method.
    
  def __eq__(self, other):
    """
    Returns True if the two given Rational numbers are equal.
    """
    # TODO implement this method.
    return False

  def __str__(self):
    """
    Returns a string representing this Rational number.
    """
    # TODO implement this method.
    return 'Not Implemented'
  
  def __add__(self, other):
    """
    Returns the addition (+) of two Rational numbers.
    """
    # TODO implement this method.
    return Rational(1, 1)
  
  def __mul__(self, other):
    """
    Returns the multiplication (*) of two Rational numbers.
    """
    # TODO implement this method.
    return Rational(1, 1)

  def __sub__(self, other):
    """
    Returns self minus (-) other of two Rational numbers.
    """
    # TODO implement this method.
    return Rational(1, 1)
  
  def __truediv__(self, other):
    """
    Returns self divided by (/) other.
    """
    # TODO implement this method.
    return Rational(1, 1)


def test_rational():
  """
  Put your own tests here.
  This function will never be called during marking.
  """
