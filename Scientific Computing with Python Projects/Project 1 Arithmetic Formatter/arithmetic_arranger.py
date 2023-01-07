import re

def arithmetic_arranger(problems, solve = False):
  # print(type(problems))
  if len(problems) > 5: #Errorcheck 1: Only accept up to 5 problmes
    return 'Error: Too many problems.'

  line1 = ''
  line2 = ''
  line3 = ''
  line4 = ''
  for problem in problems: #Errorcheck 2: Only accept problems with operators '+' and '-'
    if '+' in problem:
      numbers = problem.split('+')
      operator = '+'

    elif '-' in problem:
      numbers = problem.split('-')
      operator = '-'
    else:
      return "Error: Operator must be '+' or '-'."

    longernum = None
    for number in numbers:
      number = number.strip()
      if len(number) > 4: #Errorcheck 4: The numbers cannot be longer than 4 digits
        return 'Error: Numbers cannot be more than four digits.'
      # print(number)
      if longernum == None or len(number)> len(longernum):
        longernum = number #determin the longer number of the problem in order to determin colon width
      columnwid = len(longernum) + 2 #determin the width of every column, the numer of '-' will equal this number

      if (re.search('[^0-9.]', number)): #Errorcheck 3: The numbers must only contain digits
        return 'Error: Numbers must only contain digits.'
        
    firstnum = numbers[0].strip()
    secondnum= numbers[1].strip()

    if solve:
      if operator == '+':
        sum = str(int(firstnum) + int(secondnum))
      if operator == '-':
        sum = str(int(firstnum) - int(secondnum))

    top = (columnwid - len(firstnum)) * ' ' + firstnum
    bottom = operator + ' ' + (len(longernum) - len(secondnum)) * ' ' + secondnum
    if solve:
      res = (columnwid - len(sum)) * ' ' + sum

    if problem is not problems[-1]:
      line1 += top + '    '
      line2 += bottom + '    '
      line3 += columnwid * '-' + '    '
      if solve:
        line4 += res + '    '
    else:
      line1 += top
      line2 += bottom
      line3 += columnwid * '-'
      if solve:
        line4 += res

  if solve:
    arranged_problems = line1 + '\n' + line2 + '\n' + line3 + '\n' + line4
  else:
    arranged_problems = line1 +'\n' + line2 +'\n' + line3

  return arranged_problems