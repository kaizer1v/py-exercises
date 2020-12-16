'''
Dijkstra's two stack algorithm helps in performing the following operation

[Video from around 8th minute](https://www.coursera.org/learn/algorithms-part1/lecture/2Mbvz/stack-and-queue-applications-optional)

Here's what it does. Say we want to comute arithmentic expression like

(1 + ( ( 2 + 3 ) * ( 4 * 5 ) ) )

Rules of the algo (when you encounter the following, do the following)

* Value: push into the value stack
* Operator: push into the operator stack
* Left Paranthesis: Ignore
* Right Paranthesis:
  - pop top 2 values
  - pop top operator
  - perform the evaluation using the two values and the oprator
  - push the result back into the value stack
'''
from stacks import StackUsingArrays

class TwoStackAlgo:

  def execute(self, expr):
    for char in expr:
      if char in ['+', '-', '*', '/']:
        self.os.push(char)
      elif char == '(' or ' ':
        continue
      elif char == ')':
        val_1 = self.vs.pop()
        val_2 = self.vs.pop()
        oper = self.os.pop()
        result = eval(val_1 + oper + val_2)
        self.vs.push(result)
      else:
        self.vs.push(char)

      self.os.print()
      self.vs.print()

  def get_result(self):
    return self.vs.pop()

  def __init__(self, expr):
    self.os = StackUsingArrays()
    self.vs = StackUsingArrays()
    self.execute(expr.replace(' ', ''))

tsa = TwoStackAlgo('(1 + ( ( 2 + 3 ) * ( 4 * 5 ) ) )')
print(tsa.get_result())
