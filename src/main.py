import os
from PIL import Image
from sourcetree_ui import SourcetreeUI  # Hypothetical import, replace with actual API

def generate_thumbnail(file_path):
    image = Image.open(file_path)
    image.thumbnail((128, 128))
    thumbnail_path = os.path.join("assets", os.path.basename(file_path))
    image.save(thumbnail_path)
    return thumbnail_path

def main():
    ui = SourcetreeUI()
    ui.add_section("Assets")

    # Fetch the list of changed files
    changed_files = get_changed_files()  # Implement this function to get changed files

    for file in changed_files:
        if file.endswith((".png", ".jpg", ".jpeg")):
            thumbnail = generate_thumbnail(file)
            ui.add_asset_thumbnail(thumbnail, file)

if __name__ == "__main__":
    main()
