from typing import Counter


def cn(expression):
  expression = expression.replace(" ", "")
  precedence = {"+": 2, "-": 2, "*": 1, "/": 1}
  operator_stack = []
  operand_stack = []
  tokens = []
  token = ""
  for i, char in enumerate(expression):
    if char.isdigit() or (char == '-' and
                          (i == 0 or expression[i - 1] in "+-*/")):
      token += char
    else:
      if token:
        tokens.append(token)
        token = ""
      tokens.append(char)
  if token:
    tokens.append(token)

  for token in tokens:
    if token.lstrip('-').isdigit():
      operand_stack.append(int(token))
    elif token in "+-*/":
      while operator_stack and precedence[token] <= precedence[
          operator_stack[-1]]:
        operator = operator_stack.pop()
        operand2 = operand_stack.pop()
        operand1 = operand_stack.pop()
        result = 0
        if operator == "+":
          result = operand1 + operand2
        elif operator == "-":
          result = operand1 - operand2
        elif operator == "*":
          result = operand1 * operand2
        elif operator == "/":
          result = operand1 / operand2
        operand_stack.append(result)
      operator_stack.append(token)

  while operator_stack:
    operator = operator_stack.pop()
    operand2 = operand_stack.pop()
    operand1 = operand_stack.pop()
    result = 0
    if operator == "+":
      result = operand1 + operand2
    elif operator == "-":
      result = operand1 - operand2
    elif operator == "*":
      result = operand1 * operand2
    elif operator == "/":
      result = operand1 / operand2
    operand_stack.append(result)

  return operand_stack[0] if operand_stack else None


def run(file1):
  with open(file1, "r") as file:
    han = file.read().replace("\n", "")
    hanl = han.split(";")
    val = {}
    for j in hanl:
      al = ""
      if j.startswith("돌"):
        hcount = j.count("돌")
        for i in j:
          if i == "꽁":
            if not al:
              al += "+1"
            elif (al[-1] == "/" or al[-1] == "*"):
              al += "1"
            else:
              al += "+1"
          elif i == "고":
            if not al:
              al += "-1"
            elif (al[-1] == "/" or al[-1] == "*"):
              al += "-1"
            else:
              al += "-1"
          elif i == "양":
            al = al + "*"
          elif i == "이":
            al = al + "/"
        val[hcount] = cn(al[1:])
      elif j.startswith("얼어붙은") and j.endswith("~"):
        ins = j[4:-1]
        if "돌" in ins:
          hcount2 = ins.count("돌")
          print(val[hcount2])
        else:
          al1 = ""
          for i in ins:
            if i == "꽁":
              if not al1:
                al1 += "+1"
              elif (al1[-1] == "/" or al1[-1] == "*"):
                al1 += "1"
              else:
                al1 += "+1"
            elif i == "고":
              if not al1:
                al1 += "-1"
              elif (al1[-1] == "/" or al1[-1] == "*"):
                al1 += "-1"
              else:
                al1 += "-1"
            elif i == "양":
              al1 = al1 + "*"
            elif i == "이":
              al1 = al1 + "/"
          print(cn(al1))
