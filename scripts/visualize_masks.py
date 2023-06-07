import json
from PIL import Image

with open('output/scenes/clevr_ref+_cogent_valA_scenes.json') as f:
    data = json.load(f)
    scenes = data['scenes']
    scenes = scenes[:1]

    for scene in scenes:
        print(scene['obj_mask'])
        print(scene['image_filename'])
        # open the associated image and display it
        img = Image.open('output/images/valA/' + scene['image_filename'])
        img.show()