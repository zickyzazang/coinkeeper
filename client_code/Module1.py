import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

beer_price = float(app_tables.settings.get(Setting='beer_price')['Value'])
big_beer_price = float(app_tables.settings.get(Setting='big_beer_price')['Value'])
double_beer_price = float(app_tables.settings.get(Setting='double_beer_price')['Value'])

def say_hello():
  print("Hello, world")
