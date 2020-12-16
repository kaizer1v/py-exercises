'''
Convex Hull

[video link](https://www.coursera.org/learn/algorithms-part1/lecture/KHJ1t/convex-hull)
'''

'''
Part 1

Given three co-ordinates / points (A, B & C) on a plane, how do you determine that
they are counter-clock-wise arranged?
Here, A, B & C are arranged in          

  clock-wise                     counter-clock-wise

      •B                                  •B
              •C                     •C
  •A                                          •A

Formulae for determining that is

                      determinant

                      | Ax Ay 1 | 
2 * Area(A, B, C) =   | Bx By 1 | = (Bx - Ax)(Cy - Ay) - (By - Ay)(Cx - Ax)
                      | Cx Cy 1 |

if the result is

> 0, then A -> B -> C is counter-clockwise
< 0, then A -> B -> C is clockwise
= 0, then A -> B -> C are co-linear (on a vertical line)

'''
