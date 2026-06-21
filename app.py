from renderer import Renderer
from widgets.clock_widget import ClockWidget
from drivers.factory import create_driver

clock = ClockWidget()

renderer = Renderer()

img = renderer.render()

# driver = PreviewDriver()
# driver = WaveshareDriver()

driver = create_driver()
driver.show(img)