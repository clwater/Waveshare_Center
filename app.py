from widgets.clock_widget import ClockWidget
from renderer import Renderer
from driver import PreviewDriver


clock = ClockWidget()

data = clock.render()

renderer = Renderer()

img = renderer.render(data)

driver = PreviewDriver()

driver.show(img)