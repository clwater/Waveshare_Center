from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

WIDTH = 1360
HEIGHT = 480

BASE_DIR = Path(__file__).resolve().parent
FONT_FILE = BASE_DIR / "fonts" / "msyh.ttc"


class Renderer:

    def render(self, data):

        img = Image.new(
            "1",
            (WIDTH, HEIGHT),
            255
        )

        draw = ImageDraw.Draw(img)

        font_big = ImageFont.truetype(
            str(FONT_FILE),
            120
        )

        font_small = ImageFont.truetype(
            str(FONT_FILE),
            40
        )

        draw.text(
            (40, 80),
            data["time"],
            font=font_big,
            fill=0
        )

        draw.text(
            (50, 250),
            data["date"],
            font=font_small,
            fill=0
        )

        return img