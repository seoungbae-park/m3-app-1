from ._anvil_designer import Form2Template
from anvil import *
import anvil.server


class Form2(Form2Template):
  def __init__(self, captured_image, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.image_1.source = captured_image
    # Any code you write here will run before the form opens.

  def form_show(self, **event_args):
    """This method is called when the form is shown on the page"""
    pass
