import sys
import os
from PIL import Image, ImageEnhance, ImageFilter
import numpy as np

def process_image():
    input_path = "assets/jiya_original.png"
    output_png = "assets/jiya_nobg.png"
    output_webp = "assets/jiya_nobg.webp"
    output_legacy = "assets/jiya.png"

    print(f"Reading input image from {input_path}...")
    img = Image.open(input_path).convert("RGBA")

    try:
        from rembg import remove
        print("Removing background with rembg u2net model...")
        out_img = remove(img)
    except Exception as e:
        print(f"rembg failed or model issue: {e}")
        return False

    # Get bounding box of subject
    alpha = out_img.split()[3]
    bbox = alpha.getbbox()
    if bbox:
        # Add slight padding around bounding box if possible
        w, h = out_img.size
        pad = 10
        crop_box = (
            max(0, bbox[0] - pad),
            max(0, bbox[1] - pad),
            min(w, bbox[2] + pad),
            min(h, bbox[3] + pad)
        )
        out_img = out_img.crop(crop_box)
        print(f"Cropped image bounding box to {out_img.size}")

    # Slight color/contrast polish for stunning look
    enhancer = ImageEnhance.Color(out_img)
    out_img = enhancer.enhance(1.05)
    
    contrast = ImageEnhance.Contrast(out_img)
    out_img = contrast.enhance(1.04)

    # Save PNG and WebP formats
    out_img.save(output_png, "PNG", optimize=True)
    out_img.save(output_webp, "WEBP", quality=95, method=6)
    out_img.save(output_legacy, "PNG", optimize=True)

    print(f"Saved background-removed images: {output_png}, {output_webp}, {output_legacy}")
    return True

if __name__ == "__main__":
    process_image()
