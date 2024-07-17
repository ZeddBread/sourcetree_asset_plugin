import os
from PIL import Image
from subprocess import check_output
from shutil import copyfile

class SourcetreeUI:
    def __init__(self):
        # Initialize the UI component
        self.sections = {}

    def add_section(self, name):
        # Add a new section to the UI
        self.sections[name] = []

    def add_asset_thumbnail(self, section_name, thumbnail_path, original_file_path):
        # Add a thumbnail to the specified UI section
        if section_name in self.sections:
            self.sections[section_name].append((thumbnail_path, original_file_path))
        else:
            print(f"Section {section_name} does not exist")

    def render_ui(self):
        # Placeholder for rendering the UI sections with thumbnails
        for section, assets in self.sections.items():
            print(f"Section: {section}")
            for thumbnail, original in assets:
                print(f"Thumbnail: {thumbnail}, Original: {original}")
                # Placeholder for actual thumbnail rendering logic

def generate_thumbnail(file_path):
    image = Image.open(file_path)
    image.thumbnail((128, 128))
    thumbnail_path = os.path.join("assets", os.path.basename(file_path))
    image.save(thumbnail_path)
    return thumbnail_path

def get_changed_files():
    # Fetch the list of changed files using Git command
    output = check_output(["git", "diff", "--name-only", "HEAD~1..HEAD"]).decode("utf-8")
    changed_files = output.strip().split("\n")
    return changed_files

def main():
    # Ensure assets directory exists
    if not os.path.exists("assets"):
        os.makedirs("assets")

    ui = SourcetreeUI()
    ui.add_section("Assets")

    # Fetch the list of changed files
    changed_files = get_changed_files()

    for file in changed_files:
        if file.endswith((".png", ".jpg", ".jpeg")):
            thumbnail = generate_thumbnail(file)
            ui.add_asset_thumbnail("Assets", thumbnail, file)
    
    # Render the UI (Placeholder for actual UI rendering in Sourcetree)
    ui.render_ui()

if __name__ == "__main__":
    main()
