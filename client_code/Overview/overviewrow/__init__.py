from ._anvil_designer import overviewrowTemplate
class overviewrow(overviewrowTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.balance_name.text = self.item['Name']
    self.balance_payment_from.text = self.item['payments_from']
    self.balance_payemnt_to.text = self.item['payments_to']
    self.balance.text = self.item['balance']