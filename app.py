from renderer import Renderer
from widgets.clock_widget import ClockWidget
from drivers.factory import create_driver

clock = ClockWidget()

data = clock.render()

renderer = Renderer()

img = renderer.render(data)

# driver = PreviewDriver()
# driver = WaveshareDriver()

driver = create_driver()
driver.show(img)