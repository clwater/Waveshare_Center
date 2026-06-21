from PIL import Image, ImageDraw, ImageFont


WIDTH = 1360
HEIGHT = 480


class Renderer:

    def render(self, data):

        img = Image.new(
            "1",
            (WIDTH, HEIGHT),
            255
        )

        draw = ImageDraw.Draw(img)

        font_big = ImageFont.truetype(
            "C:/Windows/Fonts/msyh.ttc",
            120
        )

        font_small = ImageFont.truetype(
            "C:/Windows/Fonts/msyh.ttc",
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