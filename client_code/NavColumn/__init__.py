from ._anvil_designer import NavColumnTemplate
import anvil.users
import anvil
from .. import Module1

class NavColumn(NavColumnTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    anvil.users.login_with_form()
    self.current_user = anvil.server.call('get_user')
    if self.current_user == 'Niels':
      self.settings_button.visible = True
    else:
      self.settings_button.visible = False
    # Any code you write here will run before the form opens.

  def logout_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.users.logout()
    anvil.open_form('Homepage')

  def coins_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.open_form('Homepage')

  def overview_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.open_form('Overview')

  def settings_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.open_form('Settings')

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.open_form('Signup')
