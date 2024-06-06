from ._anvil_designer import HomepageTemplate
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .. import Module1
import datetime
from anvil_extras.storage import local_storage
from anvil import alert


class Homepage(HomepageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Any code you write here will run when the form opens.
    anvil.users.login_with_form()
    self.current_user = anvil.server.call('get_user')
    self.other_user_dropdown.selected_value = self.current_user
    
    self.refresh_table()
    self.starttime_value = 10*60
    self.color_timer_count = self.starttime_value
    # self.beer_price = float(app_tables.settings.get(Setting='beer_price')['Value'])
    # self.big_beer_price = float(app_tables.settings.get(Setting='big_beer_price')['Value'])
    # self.double_beer_price = float(app_tables.settings.get(Setting='double_beer_price')['Value'])

  def refresh_table(self, **event_args):
    self.user_logged_in.text = f"Logged in as {self.current_user}"
    self.other_user_dropdown.items = anvil.server.call('get_users')
    
    self.other_user_panel.items = app_tables.users.search(
      tables.order_by("Name"),
      Name=q.not_(self.current_user)
    )
    
  def logout_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.users.logout()

  def coins_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.open_form('Homepage')

  def overview_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.open_form('Overview')
  
  def reset_colors(self, **event_args):
    background_color = "theme:Primary Container"
    foreground_color = "theme:On Primary Container"
    self.color_timer_count = self.starttime_value
    for item in self.other_user_panel.get_components():
      item.add_1.background = background_color
      item.add_15.background = background_color
      item.add_2.background = background_color
      item.add_1.foreground = foreground_color
      item.add_15.foreground = foreground_color
      item.add_2.foreground = foreground_color
      item.other_amount.text = None
    
    
  def color_timer_tick(self, **event_args):
    """This method is called Every [interval] seconds. Does not trigger if [interval] is 0."""
    self.color_timer_count -= 1
    if self.color_timer_count < 1:
      self.reset_colors()

  def cancel_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.reset_colors()
    del local_storage['unsaved_data']
    

  def confirm_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.reset_colors()
    total_amount = []
    if 'unsaved_data' not in local_storage:
      local_storage['unsaved_data'] = []
    
    for component in self.other_user_panel.get_components():
        for storage in component.local_storage:
          if storage:
            for key in storage.keys():
              total_amount.append(storage[key])
              data_row = [dict(payment_from=key, payment_to=self.current_user, amount=storage[key], timestamp=datetime.datetime.now())]
              local_storage['unsaved_data'] += data_row
        component.reset_storage()
      
    alert(f"€{sum(total_amount)} saved")

    if anvil.server.is_app_online():
      for row in local_storage['unsaved_data']:
        app_tables.payments.add_row(
          payment_from=row['payment_from'], 
          payment_to=row['payment_to'], 
          amount=row['amount'], 
          timestamp=row['timestamp']
        )
      del local_storage['unsaved_data']

  def other_user_dropdown_change(self, **event_args):
    """This method is called when an item is selected"""
    self.current_user = self.other_user_dropdown.selected_value
    self.refresh_table()
    
      



