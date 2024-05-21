from ._anvil_designer import Form1Template
from anvil import *
import anvil.server


class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Display inital image 
    self.image_element = anvil.js.window.document.createElement("img")
    self.image_element.src = "_/theme/Screenshot 2024-05-21 at 5.14.45 PM.png"
    self.image_element.setAttribute("width", "640")
    self.image_element.setAttribute("height", "480")
    self.image_element.style.display = "block"
    anvil.js.window.document.body.appendChild(self.image_element)
    
    # Any code you write here will run before the form opens.
    self.video = anvil.js.window.document.createElement('video')
    self.video.setAttribute("autoplay", "true")
    self.video.setAttribute("width", "640")
    self.video.setAttribute("height", "480")
    anvil.js.window.document.body.appendChild(self.video)
        # Create a canvas element for capturing images
    self.canvas = anvil.js.window.document.createElement("canvas")
    self.canvas.setAttribute("width", "640")
    self.canvas.setAttribute("height", "480")
    self.canvas.style.display = "none"  # Hide the canvas element
    anvil.js.window.document.body.appendChild(self.canvas)
  
  def image_1_show(self, **event_args):
    """This method is called when the Image is shown on the screen"""
    
    pass

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    # JavaScript to access the webcam
    js_code = """
    var video = document.querySelector('video');
    var canvas = document.querySelector('canvas');
    var context = canvas.getContext('2d');
    context.drawImage(video, 0, 0, canvas.width, canvas.height);
    
    // Create an image element to display the captured frame
    var img = document.createElement('img');
    img.src = canvas.toDataURL('image/png');
    document.body.appendChild(img);
    """
    anvil.js.window.eval(js_code)

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    js_code = """
    navigator.mediaDevices.getUserMedia({ video: true })
      .then(function(stream) {
        var video = document.querySelector('video');
        video.srcObject = stream;
        video.onloadedmetadata = function(e) {
          video.play();
        };
      })
      .catch(function(err) {
        console.log("An error occurred: " + err);
      });
    """
    anvil.js.window.eval(js_code)
    from .Form2 import Form2
    open_form(Form2(captured_image))
