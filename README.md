# Waveshare_Center

## Run

Preview mode on a normal PC:

```bash
python app.py
```

Hardware/self-check without driving the panel:

```bash
python self_test.py
```

On Raspberry Pi:

```bash
python3 app.py
```

If SPI/GPIO is not installed on the Pi, install the common dependencies first:

```bash
sudo apt install -y python3-rpi.gpio python3-spidev
python3 -m pip install pillow
```
