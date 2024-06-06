from ._anvil_designer import paymentrowTemplate
import anvil.server
from anvil.tables import app_tables
from anvil_extras.storage import local_storage
from anvil_extras.animation import Effect, pulse
import anvil
import datetime
from ... import Module1

class paymentrow(paymentrowTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    self.add_1_clicked = False
    self.add_15_clicked = False
    self.add_2_clicked = False
    self.add_1.text = f"€{Module1.beer_price}"
    self.add_15.text = f"€{Module1.big_beer_price}"
    self.add_2.text = f"€{Module1.double_beer_price}"
    self.reset_storage()
    
  def reset_storage(self):
    self.other_amount_storage = {}
    self.small_storage = {}
    self.big_storage = {}
    self.double_storage = {}
    self.local_storage = [self.small_storage, self.big_storage, self.double_storage, self.other_amount_storage]
    
    
  def add_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    amount = Module1.beer_price
    if not self.add_1_clicked:
      self.small_storage[self.item['Name']] = amount
      self.pulse_effect = Effect(pulse, duration=100)
      self.pulse_effect.animate(self.add_1)
      self.add_1.background = "theme:On Primary Container"
      self.add_1.foreground = "theme:Primary Container"
      self.parent.parent.parent.color_timer_count = self.parent.parent.parent.starttime_value
      self.add_1_clicked = True
    else:
      del self.small_storage[self.item['Name']]
      self.add_1.background = "theme:Primary Container"
      self.add_1.foreground = "theme:On Primary Container"
      self.add_1_clicked = False
      
    
  def add_15_click(self, **event_args):
    """This method is called when the button is clicked"""
    amount = Module1.big_beer_price
    if not self.add_15_clicked:
      self.big_storage[self.item['Name']] = amount
      self.pulse_effect = Effect(pulse, duration=100)
      self.pulse_effect.animate(self.add_15)
      self.add_15.background = "theme:On Primary Container"
      self.add_15.foreground = "theme:Primary Container"
      self.parent.parent.parent.color_timer_count = self.parent.parent.parent.starttime_value
      self.add_15_clicked = True
    else:
      del self.big_storage[self.item['Name']]
      self.add_15.background = "theme:Primary Container"
      self.add_15.foreground = "theme:On Primary Container"
      self.add_15_clicked = False
      
      
  def add_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    amount = Module1.double_beer_price
    if not self.add_2_clicked:
      self.double_storage[self.item['Name']] = amount
      self.pulse_effect = Effect(pulse, duration=100)
      self.pulse_effect.animate(self.add_2)
      self.add_2.background = "theme:On Primary Container"
      self.add_2.foreground = "theme:Primary Container"
      self.parent.parent.parent.color_timer_count = self.parent.parent.parent.starttime_value
      self.add_2_clicked = True
    else:
      del self.double_storage[self.item['Name']]
      self.add_2.background = "theme:Primary Container"
      self.add_2.foreground = "theme:On Primary Container"
      self.add_2_clicked = False
      

  def other_amount_change(self, **event_args):
    """This method is called when the text in this text box is edited"""
    try:
      self.other_amount_storage[self.item['Name']] = float(self.other_amount.text)
    except TypeError:
      del self.other_amount_storage[self.item['Name']]


