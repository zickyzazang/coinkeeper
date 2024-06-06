from ._anvil_designer import OverviewTemplate
from anvil import *
import anvil.server

class Overview(OverviewTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    current_user = anvil.server.call('get_user')
    
    data = anvil.server.call('get_balances')  
    self.balance_panel.items = data
    user_balance_array = []
    for row in data:
      user_balance_array.append([row['Name'], row['balance']])
      
    user_balance_array.sort(key=lambda a: a[1])
    debit = list(filter(lambda x: x[1] > 0, user_balance_array))
    credit = list(filter(lambda x: x[1] < 0, user_balance_array))
    debit.sort(key=lambda a: a[1], reverse=True)
    credit.sort(key=lambda a: a[1], reverse=False)
    credit = [[c[0], c[1]*-1] for c in credit]
    repayment = {}
    di = 0
    ci = 0
    debit_sum = sum([x[1] for x in debit])
    
    while debit_sum > 0:
      
      d = debit[di]
      c = credit[ci]
      
      if d[0] not in repayment.keys():
        repayment[d[0]] = {}
      
      if debit[di][1] >= credit[ci][1] and credit[ci][1] > 0:
        
        repayment[d[0]][c[0]] = credit[ci][1]
        debit[di][1] = debit[di][1] - credit[ci][1]
        credit[ci][1] = 0
        
      elif debit[di][1] < credit[ci][1] and credit[ci][1] > 0 and debit[di][1] > 0:
        
        repayment[d[0]][c[0]] = debit[di][1]
        credit[ci][1] = credit[ci][1] - debit[di][1]
        debit[di][1] = 0
        
      debit_sum = sum([x[1] for x in debit])

      if debit[di][1] <= 0:
        di += 1
      if credit[ci][1] <= 0:
        ci += 1
    print(repayment)
        
    settle_text = ""
    if current_user in repayment.keys():
      for user in repayment[current_user].keys():
        amount = repayment[current_user][user]
        settle_text += f"{user} owes you {amount}\n"
    else: 
      for key in repayment.keys():
        if current_user in repayment[key].keys():
          owes_to = key
          amount = repayment[key][current_user]
          settle_text += f"You owe {owes_to} {amount}\n"
          
    self.settle_text.content = settle_text  


