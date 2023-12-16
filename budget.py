class Category:

  def __init__(self, category):
    self.category = category
    self.ledger = []
    self.balance = 0

  def deposit(self, amount, description=""):
    self.balance += amount
    self.ledger.append({"amount": amount, "description": description})

  def withdraw(self, amount, description=""):
    if self.check_funds(amount):
      self.balance -= amount
      self.ledger.append({"amount": -amount, "description": description})
      return True
    else:
      return False

  def get_balance(self):
    return self.balance

  def transfer(self, amount, category):
    if self.check_funds(amount):
      self.withdraw(amount, f'Transfer to {category.category}')
      category.deposit(amount, f'Transfer from {self.category}')
      return True
    else:
      return False

  def check_funds(self, amount):
    if amount > self.balance:
      return False
    else:
      return True

  def __str__(self):
    header = f"{'*' * ((30-len(self.category))//2)}{self.category}{'*' * ((30-len(self.category))//2)}"
    records = "\n".join([
        f"{record['description'][:23]:23}{record['amount']:>7.2f}"
        for record in self.ledger
    ])
    return f"{header}\n{records}\nTotal: {self.balance}"


def create_spend_chart(categories):
  total_amount = [
      sum([item['amount'] for item in category.ledger if item['amount'] < 0])
      for category in categories
  ]

  percentages = [(amount / sum(total_amount)) * 100 for amount in total_amount]

  chart = "Percentage spent by category\n"
  for i in range(100, -10, -10):
    chart += str(i).rjust(3) + "| "
    for percent in percentages:
      chart += 'o  ' if percent >= i else '   '
    chart += '\n'
  chart += "    ----------\n"

  names = [category.category for category in categories]
  max_name_length = max([len(name) for name in names])
  for i in range(max_name_length):
    chart += "" if i == 0 else "\n"
    chart += " " * 5
    for name in names:
      if i < len(name):
        chart += name[i] + "  "
      else:
        chart += " " * 3

  return chart
