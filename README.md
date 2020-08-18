# Rational-Numbers

```program.py``` is read-only For this question.

Imagine you're working in a team. Together, you're writing a small game for kids to learn about fractions and your teammate is in charge of the ```program.py``` part. Your job is to handle the fractions themselves.

You can't use regular Python ```float``` floating-point numbers for this, since they have a limited number of decimal places (in binary) and can't accurately represent or manipulate all rational numbers (fractions). You must create your own Rational class to store and manipulate rational numbers.

# Construction and print
Your class should support creating any valid rational number with a numerator and denominator, e.g ```²/₃``` is constructed like this: ```x = Rational(2, 3).```

You do not need to handle zero denominators or any cases of division by zero. These won't be in the tests.

When print is called (which in turn calls the ```__str__``` method), your Rational class should display in simplified form. For example, ```Rational(21, 12)``` should be displayed as ```1³/₄```. The small numbers must be done using unicode superscript and subscript digits. These have been provided to you in the ```SUPER_NUMS and SUB_NUMS``` variables in ```rational.py```.

# Operators
The == operator should return True if the rational numbers are equivalent. For example, ```Rational(4, 8)``` is equivalent to ```Rational(1, 2)```

The +, -, *, and / operators should all work as expected on two Rational numbers and return a new Rational instance without modifying the originals.

Note that the / operator is implemented with the ```__truediv__``` method. You do not need to implement ```__floordiv__```.

#Testing
Since program.py is read-only, we've given you a test function in rational.py which is optionally called instead of running the game. You can use this or delete it as you choose; it will never be called during marking.

# The game
When you have implemented all the methods correctly, the game should work like this:

```Run tests? no

What is 4 × 1¹/₄?
0) 5
1) 1⁴/₅
2) ¹/₂
3) 1¹/₅
> 0
Correct!
​
What is 1 ÷ ²/₅?
0) 1¹/₅
1) ¹/₄
2) 2¹/₂
3) 1
> 1
Incorrect. The correct answer was: 2¹/₂
​
What is ⁷/₉ - 1¹/₂?
0) 10
1) -¹³/₁₈
2) 3
3) ⁷/₁₀
> 1
Correct!
​
What is ³/₈ × 1²/₇?
0) 2
1) ²⁷/₅₆
2) 0
3) 1¹/₂
> 
Invalid input. The correct answer was: ²⁷/₅₆
```

# Maths
The greatest common divisor (gcd) of two or more integers, which are not all zero, is the largest positive integer that divides each of the integers. You can compute the gcd of two integers using the following code. We have provided it to you in rational.py:
 
```
def gcd(a, b):
  while b:
    a, b = b, a % b
  return a
  ```
# Be ready for anything
We'll be swapping out program.py during marking so that we can push your Rational class to the limits and test cases you might not have thought of (but not zero denominators).
