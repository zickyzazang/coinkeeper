import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from datetime import datetime
from collections import defaultdict


@anvil.server.callable
def get_user():
  return anvil.users.get_user()['Name']


@anvil.server.callable
def get_payments(from_or_to):
  assert from_or_to in ['payment_to', 'payment_from'], 'from_or_to should be either payment_to, or payment_from'
  
  all_users = get_users()
  all_payments = app_tables.payments.search()
  all_payments = [dict(r) for r in all_payments]
  payments = {}
  for payment in all_payments:
    if payment[from_or_to] in payments.keys():
      payments[payment[from_or_to]].append(payment['amount'])
    else:
      payments[payment[from_or_to]] = [payment['amount']]
      
  for user in all_users:
    if user in payments.keys():
      payments[user] = sum(payments[user])
    else:
      payments[user] = 0
        
  return payments

@anvil.server.callable
def get_users():
  # Get a list of entries from the Data Table, sorted by 'created' column, in descending order
  users = app_tables.users.search()
  names = [r['Name'] for r in users]
  return names


@anvil.server.callable
def get_balances():
  all_users = get_users()
  # Any code you write here will run when the form opens
  payments_to = get_payments('payment_to') 
  payments_from = get_payments('payment_from')
  data = []
  
  for user in all_users:
    if user in payments_to.keys() and user in payments_from.keys():
      balance = (payments_to[user] - payments_from[user])
    else:
      balance = 0
    
    data.append({
      'Name': user, 
      'payments_to': payments_to[user], 
      'payments_from': payments_from[user],
      'balance': balance
    })
  return data

@anvil.server.callable
def update_settings(Setting, Value):
  row = app_tables.settings.get(Setting=Setting)
  row['Value'] = Value
  print('updated')