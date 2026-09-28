from PIL import Image, ImageDraw, ImageFont


# =========================
# Watermark settings
# =========================

WATERMARK_TEXT = "©NepaliStamps"

# Custom watermark position
# X = distance from the left
# Y = distance from the top
POSITION_X = 355
POSITION_Y = 500

# Rotation in degrees
ROTATION = 0

# Opacity:
# 0 = invisible
# 255 = fully opaque
OPACITY = 80

# Text size
FONT_SIZE = 40

# Watermark color (RGB)
# White = (255, 255, 255)
# Black = (0, 0, 0)
# Red   = (255, 0, 0)
# Blue  = (0, 0, 255)
WATERMARK_COLOR = (0, 0, 0)


# =========================
# File paths
# =========================

INPUT_IMAGE = "input/test-stamp.jpg"
OUTPUT_IMAGE = "output/test-stamp-watermarked.jpg"


# =========================
# Load image
# =========================

image = Image.open(INPUT_IMAGE).convert("RGBA")

# Create transparent layer for watermark
watermark_layer = Image.new(
    "RGBA",
    image.size,
    (0, 0, 0, 0)
)

draw = ImageDraw.Draw(watermark_layer)


# =========================
# Load font
# =========================

font = ImageFont.truetype("arial.ttf", FONT_SIZE)


# =========================
# Draw watermark
# =========================

draw.text(
    (POSITION_X, POSITION_Y),
    WATERMARK_TEXT,
    font=font,
    fill=(*WATERMARK_COLOR, OPACITY)
)


# =========================
# Rotate watermark
# =========================

if ROTATION != 0:
    watermark_layer = watermark_layer.rotate(
        ROTATION,
        expand=False,
        resample=Image.Resampling.BICUBIC
    )


# =========================
# Combine images
# =========================

image = Image.alpha_composite(
    image,
    watermark_layer
)


# =========================
# Save
# =========================

image.convert("RGB").save(
    OUTPUT_IMAGE,
    quality=95
)


print(f"Watermarked image saved to: {OUTPUT_IMAGE}")
