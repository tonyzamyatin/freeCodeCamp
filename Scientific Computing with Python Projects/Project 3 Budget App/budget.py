class Category:
  
  def __init__(self, nam):
    self.name = nam
    self.balance = 0.0
    self.deposits = 0.0
    self.withdrawls = 0.0
    self.ledger = list() 

  def __repr__(self):
    receipt = f'{self.name:*^30}\n'
    for item in self.ledger:
        line = f'{item["description"][:23]:23}' + f'{item["amount"]:>7.2f}' + '\n'
        receipt += line
    
    total = 'Total: ' + str("{:.2f}".format(self.balance))
    receipt += total
    return receipt


  def check_funds(self, amount):
    if  amount > self.balance:
      return False
    else:
      return True

  def deposit(self, amount, descript=''):
    self.ledger.append({"amount": amount, "description": descript})
    self.balance += float(amount)
    self.deposits += float(amount)
  
  def withdraw(self, amount, descript=''):
    if self.check_funds(amount) is True:
      self.ledger.append({"amount": -1*amount, "description": descript})
      self.balance -= float(amount)
      self.withdrawls += float(amount)
      return True
    else:
      return False
  
  def get_balance(self):
    return self.balance
  
  def transfer(self, amount, transcat):
    if self.check_funds(amount) is True:
      self.withdraw(float(amount), f"Transfer to {transcat.name}")
      transcat.deposit(float(amount), f"Transfer from {self.name}")
      return True
    else:
      return False

def create_spend_chart(categories):
  spendings = [category.withdrawls for category in categories]
  total = sum(spendings)
  percentages = [s * 100 / total for s in spendings]
  names =list()
  output = 'Percentage spent by category\n'

  for category in categories:
    names.append(category.name)
  
  i = 100
  while i >= 0:
    line = f'{i:>3}| '
    for item in percentages:
      if float(item) >= i:
        line += 'o  '
      else:
        line += '   '
    output += f'{line}\n'
    i -= 10

  width = 1 + 3*len(categories)
  output += f'    {width * "-"}\n' 
  
  catlength = 0
  for name in names:
    if len(name) > catlength:
      catlength = len(name)
    
  i = 0
  while i < catlength:
    line = 5*' '
    for item in names:
      if i < len(item):
        line += f'{item[i]}  '
      else:
        line += '   ' 
    if i == catlength - 1:
      output += f'{line}'
    else:
      output += f'{line}\n'
    i += 1
  # all that extra white space is hella annoying
  return output