# [python] computor-v1 - 42 project


## GOAL
You can read the subject [here](https://github.com/tbeauzam/computor-v1/blob/master/SUBJECT-computorv1.fr.pdf)

TL;DR: \
This script is a solver for polynomial equations of degree 2 (or less).

## SUMMARY

(For more detailed examples on usage, see [usage](#usage)) \
Straightforward example: \
`python3 computor-v1.py "1 * x^0 + 3 * x^1 + -4 * x^2 = 0"`

Output:
>Received expression: \
>1 * x^0 + 3 * x^1 + -4 * x^2 = 0
>
>Reduced form: 1 + 3 * x - 4 * x^2 = 0 \
>Polynomial degree: 2
>
>Solutions: \
>x1 = -0.25 and x2 = 1

### What is a polynomial equation of degree 2?
`1 * x^0 + 3 * x^1 - 4 * x^2 = 0` is an example of such an equation. \
Each term is constitued like that: \
*1* is a **coefficient**. It applies to the rest of the term (here: *x^0* ) \
*x* is called a **variable**, and this is what we are looking for here. We want to know the value of x. \
*^0* is the **exponent**. It applies to x, and in the case of polynomial equations of degree 2, it cannot be more than 2.

### What are solutions of such equations?
* if equation is degree 0, the solution is super simple: x can be **any real number**.
* if degree is 1, x will always have **one** solution, always a real number too.
* if degree is 2, things get a bit more complicated. You need to find the **discriminant** (more on that in [usage](#usage) below)
  * if discriminant = 0: equation have **one real** solution.
  * if discriminant > 0: equation have **two real** solutions.
  * if discriminant < 0: equation have **two complex** solutions.
 
 As we will see in examples below, this equation has a **positive** discriminant.

## USAGE

As we have seen above, you can just call the script with one equation and it will work. But what if you want to know more about the process? Well, no worries, there is a lot of options for that. \
Here is a copy of usage:

>Usage:
> --> python3 \<options\> computor-v1.py "polynomial equation"
>
>Notes: \
>\- this is a python 3 script, not python 2 \
>\- polynomial degree of reduced form must be 0, 1 or 2 \
>\- no negative or non-integer exponents allowed (valid range: 0 to 99) \
>\- valid characters set: |0123456789.*-+=x^| \
>\- x can be written x or X, but every occurence will be lower-cased \
>\- options must start with a '-' and contain only valid options. See the list below. \
>
>Options list: \
>    -d: displays debug about input \
>    -s: displays reduced form in "scientific" notation (displays all exponents in the form a * x^e) \
>    -u: ends execution and displays usage \
>    -v: always displays more info on discriminant step \
>    -vv: displays every steps with formulas and basic explanations
> 
>Example of polynomial equation: 1 * X^0 + 2 * X^1 = - 1 * X^0 + 4 * X^1
>
>Example of usage: \
>$> python3 computor-v1.py -s "1 * X^0 + 2 * X^1 = - 1 * X^0 + 4 * X^1" \
>Reduced form: 2 * x^0 - 2 * x^1 = 0 \
>Polynomial degree: 1 \
>Solution: \
>x = 1 \

### Options with examples

## -d
Displays a lot of debug about the equation. This debug is about the parsing of the input, so you can see how I handle the terms, signs etc. This is also the step where all terms that are on the right of the equation are transfered to the left, if applicable. Example: \
`$>python3 computor-v1.py -d "1 + 3 \* x^1 - 4 \* x^2 = 0"`
>Received expression: \
>1 + 3 \* x^1 - 4 \* x^2 = 0
>
>Removed spaces: \
>1+3\*x^1-4\*x^2=0
>
>Checked signs: \
>1+3\*x^1-4\*x^2=0
>
>Remade spacing: \
>1 +3\*x^1 -4\*x^2=0
>
>Left part: 1 +3\*x^1 -4\*x^2 \
>Right part: 0
>
>Transfer right terms to the left: \
>\['+1', '+3\*x^1', '-4\*x^2', '-0'\]
>
>Reduced form: 1 + 3 \* x - 4 \* x^2 = 0 \
>Polynomial degree: 2
>
>Solutions: \
>x1 = -0.25 and x2 = 1

## -s
Simply displays the reduced form of the equation with scientific notation for all terms. For example, it will display: \
`Reduced form: x^0 + 3 * x^1 - 4 * x^2 = 0` \
Instdead of: \
`Reduced form: 1 + 3 * x - 4 * x^2 = 0`

## -u
Displays [usage](#usage).

## -v
If equation is degree 2, adds a step about discriminant. Example: \
`$>python3 computor-v1.py -v "1 + 3 * x^1 - 4 * x^2 = 0"`
>Received expression: \
>1 + 3 * x^1 - 4 * x^2 = 0
>
>Reduced form: 1 + 3 * x - 4 * x^2 = 0 \
>Polynomial degree: 2
>
>Δ = 25 \
>Discriminant is strictly greater than 0. This means there are two real numbers as solutions. \
>Solutions: \
>x1 = -0.25 and x2 = 1

## -vv
Super verbose mode. This will add a lot of explanations about each step to solve the equation, with formulas and resolutions. Let's take an example that gives complex solutions: \
`$>python3 computor-v1.py -vv "1 + 2 * x^1 + 5 * x^2 = 0" \`
>Received expression: \
>1 + 2 * x^1 + 5 * x^2 = 0
>
>Reduced form: 1 + 2 * x + 5 * x^2 = 0 \
>Polynomial degree: 2
>
>Degree is 2. Let's solve that. \
>For the sake of resolution, let's say that: \
>\- c is the degree 0 term \
>\- b is the degree 1 term \
>\- a is the degree 2 term \
>The first thing to do is to find the discriminant (Called Delta or Δ). The formula is: Δ = b² - 4ac \
>Δ = 2² - ( 4 * 5 * 1 ) \
>Δ = -16 \
>Discriminant is strictly lower than 0. This means there are two complex numbers as solutions. \
>For this one, we are obligated to introduce a number that allow us to achieve negative square root. But still write Δ as a positive number. \
>Formulas for each solution are: x1 = (-b + i√Δ) / 2a  and  x2 = (-b - i√Δ) / 2a \
>This displays like this: x1 = (-b / (2a)) + ((i√Δ) / (2a))  and  x2 = (-b / (2a)) - ((i√Δ) / (2a)) \
>So, x1 = ((-2 / ( 2 * 5 )) + (i√16) / ( 2 * 5 )) \
>And x2 = ((-2 / ( 2 * 5 )) - (i√16) / ( 2 * 5 ))
>
>Solutions: \
>x1 = -0.2 + i * 0.4 and x2 = -0.2 - i * 0.4
