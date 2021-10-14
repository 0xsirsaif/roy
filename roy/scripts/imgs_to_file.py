from PIL import Image
import os


def pngs_to_pdf(src: str, destination: str) -> None:
    len_files = len([img for img in os.listdir(src) if "png" in img])
    images = [
        image.convert("RGB")
        for i in range(1, len_files)
        if (image := Image.open(os.path.join(src, f"{i}.png")))
    ]
    img_1 = Image.open(os.path.join(src, "0.png")).convert("RGB")

    file_name = src.split("/")[-2] + ".pdf"  # TODO
    img_1.save(
        os.path.join(destination, file_name), save_all=True, append_images=images
    )
