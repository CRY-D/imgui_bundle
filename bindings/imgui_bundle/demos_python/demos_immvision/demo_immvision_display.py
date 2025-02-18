import os.path
import cv2

from imgui_bundle import immvision, immapp, imgui_md
from imgui_bundle.demos_python import demo_utils


@immapp.static(inited=False)
def demo_gui() -> None:
    statics = demo_gui
    image_display_size = (0, int(immapp.em_size(15)))
    if not statics.inited:
        assets_dir = demo_utils.demos_assets_folder() + "/images/"
        statics.bear = cv2.imread(assets_dir + "bear_transparent.png", cv2.IMREAD_UNCHANGED)
        statics.params = immvision.ImageParams()
        statics.params.image_display_size = image_display_size

        statics.tennis = cv2.imread(assets_dir + "tennis.jpg")

        statics.inited = True

    imgui_md.render_unindented("immvision.image_display() will simply display an image")
    immvision.image_display("Tennis", statics.tennis, image_display_size=image_display_size)

    imgui_md.render_unindented(
        """
        immvision.image() will display an image, while providing lots of visualization options.<br>
        Open the options panel by clicking on the settings button at the bottom right corner of the image"""
    )
    immvision.image("Bear", statics.bear, statics.params)


def main():
    demo_utils.set_hello_imgui_demo_assets_folder()
    immapp.run(demo_gui, window_size=(1000, 800), with_markdown=True)

if __name__ == "__main__":
    main()
