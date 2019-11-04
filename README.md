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
*1* is a coefficient. It applies to the rest of the term (here: *x^0* )
*x* is called a **variable**, and this is what we are looking for here. We want to know the value of x. \
*^0* is the exponent. It always applies to x, and in the case of polynomial equations of degree 2, it cannot be more than 2.

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
>    -vv: displays every steps with formulas and basic explanations \
> 
>Example of polynomial equation: 1 * X^0 + 2 * X^1 = - 1 * X^0 + 4 * X^1
>
>Example of usage: \
>$> python3 computor-v1.py -s "1 * X^0 + 2 * X^1 = - 1 * X^0 + 4 * X^1" \
>Reduced form: 2 * x^0 - 2 * x^1 = 0 \
>Polynomial degree: 1 \
>Solution: \
>x = 1 \

