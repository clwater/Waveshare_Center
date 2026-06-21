
import os
import sys

# 将 waveshare_epd 目录加入到 Python 的模块搜索路径中
sys.path.append(os.path.join(os.path.dirname(__file__), "waveshare_epd"))

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