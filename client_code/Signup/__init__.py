from ._anvil_designer import SignupTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Signup(SignupTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.

    

  def button_1_click(self, **event_args):
    if self.button_1.icon=='fa:eye':
      self.password.hide_text=False
      # self.button_1.text='Hide Password'
      # self.button_1.icon='fa:eye-slash'
    else:
      self.password.hide_text=True
      # self.button_1.text='Show Password'
      # self.button_1.icon='fa:eye'

  def sign_up_email_click(self, **event_args):
    anvil.users.signup_with_email(
      self.email.text, self.password.text, remember=self.remember_checkbox.checked)
    open_form('Homepage')
    
  def sign_up_google_click(self, **event_args):
    anvil.users.signup_with_google(remember=self.check_box_1.checked)
    open_form('Homepage')

  def email_link_click(self, **event_args):
    anvil.users.signup_with_google(remember=self.check_box_1.checked)
    open_form('Homepage')

  def log_in_button_click(self, **event_args):
    open_form('Login')




def error_handler(err):
  Notification(str(err),style='danger').show()
set_default_error_handling(error_handler)