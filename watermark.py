from PIL import Image, ImageDraw, ImageFont


# =========================
# Watermark settings
# =========================

WATERMARK_TEXT = "©NepaliStamps"

# Position options:
# "top-left"
# "top-center"
# "top-right"
# "center"
# "bottom-left"
# "bottom-center"
# "bottom-right"
POSITION = "bottom-right"

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
WATERMARK_COLOR = (255, 0, 0)

# Distance from image edges
MARGIN = 30


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
watermark_layer = Image.new("RGBA", image.size, (0, 0, 0, 0))

draw = ImageDraw.Draw(watermark_layer)


# =========================
# Load font
# =========================

font = ImageFont.truetype("arial.ttf", FONT_SIZE)


# =========================
# Get text dimensions
# =========================

bbox = draw.textbbox(
    (0, 0),
    WATERMARK_TEXT,
    font=font
)

text_width = bbox[2] - bbox[0]
text_height = bbox[3] - bbox[1]


# =========================
# Position
# =========================

if POSITION == "bottom-right":
    x = image.width - text_width - MARGIN
    y = image.height - text_height - MARGIN

elif POSITION == "bottom-left":
    x = MARGIN
    y = image.height - text_height - MARGIN

elif POSITION == "bottom-center":
    x = (image.width - text_width) // 2
    y = image.height - text_height - MARGIN

elif POSITION == "top-right":
    x = image.width - text_width - MARGIN
    y = MARGIN

elif POSITION == "top-left":
    x = MARGIN
    y = MARGIN

elif POSITION == "top-center":
    x = (image.width - text_width) // 2
    y = MARGIN

elif POSITION == "center":
    x = (image.width - text_width) // 2
    y = (image.height - text_height) // 2

else:
    raise ValueError(f"Unknown position: {POSITION}")


# =========================
# Draw watermark
# =========================

draw.text(
    (x, y),
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
    