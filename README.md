# Saturated Reverse Polish Notation (SRPN) Calculator

SRPN is a reverse polish notation calculator with the extra feature
that all arithmetic is saturated i.e. when it reaches the maximum value that
can be stored in a variable, it stays at the maximum rather than wrapping
around.

First coursework for Principles of Programming module. **Achieved a grade of 81%**.

Task was to write a program which matches the functionality of SRPN as closely as possible:

1. Single operations. The program must be able to input at least
   two numbers and perform one operation correctly and output

   ```
    Input:
    10
    2
    +
    =

    Input:
    11
    3
    -
    =

    Input:
    9
    4
    *
    =

    Input:
    11
    3
    /
    =

    Input:
    11
    3
    %
    =
   ```

2. Multiple operations. The program must be able to handle
   multiple numbers and multiple operations

   ```
    Input:
    3
    3
    *
    4
    4
    *
    +
    =

    Input:
    1234
    2345
    3456
    d
    +
    d
    +
    d
    =
   ```

3. Saturation. The program must be able to correctly handle
   saturation

   ```
    Input:
    2147483647
    1
    +
    =

    Input:
    -2147483647
    1
    -
    =
    20
    -
    =

    Input:
    100000
    0
    -
    d
    *
    =
   ```

4. Obscure functionality. The program includes the less obvious
   features of SRPN

   ```
    Input:
    1
    +

    Input:
    10
    5
    -5
    +
    /

    Input:
    11+1+1+d

    Input:
    # This is a comment #
    1 2 + # And so is this #
    d

    Input:
    3 3 ^ 3 ^ 3 ^=

    Input:
    r r r r r r r r r r r r r r r r r r r r r r d r r r d
   ```
