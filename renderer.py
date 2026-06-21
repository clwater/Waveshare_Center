import os
import threading
from collections import deque
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageOps

WIDTH = 1360
HEIGHT = 480

# --- PATHS ---

BASE_DIR = Path(__file__).resolve().parent
FONT_FILE = BASE_DIR / "fonts" / "msyh.ttc"
ICON_DIR = os.path.join(BASE_DIR, 'icons')

icon_cache = {}


def _load_font(size: int):
    try:
        return ImageFont.truetype(str(FONT_FILE), size)
    except Exception:
        return ImageFont.load_default()


fonts = {
    '28': _load_font(28),
    '20': _load_font(20),
}

# --- GLOBAL DATA STORE ---
class DataStore:
    def __init__(self):
        self.lock = threading.Lock()
        self.sysload = {'cpu': 0, 'ram_free': 0, 'history': deque(maxlen=30)}

data_store = DataStore()


class Renderer:

    def render(self):
        Himage = Image.new('1', (WIDTH, HEIGHT), 255)
        draw = ImageDraw.Draw(Himage)

        if not data_store.lock.acquire(timeout=2.0): return Himage
        try:
            sysload = data_store.sysload.copy()
        finally:
            data_store.lock.release()

        col_w = WIDTH// 3
        col1_x = 20
        y1 = 20

        draw_icon(draw, col1_x, y1, "icon_cpu", (50, 50))
        draw.text((col1_x + 60, y1), f"SYSTEM LOAD: {sysload['cpu']}%", font=fonts['28'], fill=0)
        draw.text((col1_x + 60, y1 + 35), f"RAM Free: {sysload['ram_free']} MB", font=fonts['20'], fill=0)

        return Himage


# --- GRAPHICS FUNCTIONS ---
def draw_icon(draw, x, y, name, size=(40, 40), is_white=False):
    icon = get_cached_icon(name, size, is_white)
    if icon:
        draw.bitmap((x, y), icon, fill=255 if is_white else 0)
    else:
        draw.rectangle((x, y, x + size[0], y + size[1]), outline=255 if is_white else 0)

def get_cached_icon(name, size, is_white=False):
    key = f"{name}_{size[0]}x{size[1]}_{'white' if is_white else 'black'}"
    if key not in icon_cache:
        path = os.path.join(ICON_DIR, f"{name}.bmp")
        if os.path.exists(path):
            try:
                with Image.open(path) as f_img:
                    img = f_img.convert("L").resize(size)
                    img = ImageOps.invert(img)
                    icon_cache[key] = img.convert("1")
            except:
                return None
        else:
            icon_cache[key] = None
    return icon_cache.get(key)