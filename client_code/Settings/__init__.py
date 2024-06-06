from ._anvil_designer import SettingsTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .. import Module1

class Settings(SettingsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.beer_price_box.text = app_tables.settings.get(Setting='beer_price')['Value']
    self.big_beer_price_box.text = app_tables.settings.get(Setting='big_beer_price')['Value']
    self.double_beer_price_box.text = app_tables.settings.get(Setting='double_beer_price')['Value']
    # Any code you write here will run when the form opens.

  def reset_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    app_tables.payments.delete_all_rows()

  def beer_price_box_lost_focus(self, **event_args):
    """This method is called when the TextBox loses focus"""
    beer_price = {'Setting': 'beer_price', 'Value': str(float(self.beer_price_box.text))}
    anvil.server.call('update_settings', **beer_price)
    print(beer_price)

  def big_beer_price_box_lost_focus(self, **event_args):
    """This method is called when the TextBox loses focus"""
    big_beer_price_box = {'Setting': 'big_beer_price', 'Value': str(float(self.big_beer_price_box.text))}
    anvil.server.call('update_settings', **big_beer_price_box)
    print(big_beer_price_box)

  def double_beer_price_box_lost_focus(self, **event_args):
    """This method is called when the TextBox loses focus"""
    double_beer_price_box = {'Setting': 'double_beer_price', 'Value': str(float(self.double_beer_price_box.text))}
    anvil.server.call('update_settings', **double_beer_price_box)
    print(double_beer_price_box)
