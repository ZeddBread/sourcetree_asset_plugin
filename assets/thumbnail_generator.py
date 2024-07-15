from PIL import Image

def generate_thumbnail(image_path, thumbnail_path, size=(128, 128)):
    image = Image.open(image_path)
    image.thumbnail(size)
    image.save(thumbnail_path)
