import json
import numpy as np
# generate training data for the 96 primitive classifiers for a propositional logic experiment

# generate classifier list
SHAPES = ['cube', 'cylinder', 'sphere']
SIZES = ['small', 'large']
MATERIALS = ['rubber', 'metal']
COLORS = ['gray', 'blue', 'brown', 'yellow', 'green', 'red', 'purple', 'cyan']
primitive_list = []

for shape in SHAPES:
    for size in SIZES:
        for material in MATERIALS:
            for color in COLORS:
                primitive_list.append(size + ' ' + color + ' ' + material + ' ' + shape)

# print(primitive_list)
# print(len(primitive_list))

files = ['clevr_ref+_cogent_trainA_scenes.json', 'clevr_ref+_cogent_valA_scenes.json', 'clevr_ref+_cogent_valB_scenes.json']

for file in files:
    with open(f'output/scenes/{file}') as f:
        data = json.load(f)
        scenes = data['scenes'][:5]
        labels = dict()

        for scene in scenes:
            fname = scene['image_filename']
            objs = scene['objects']
            label = np.zeros(len(primitive_list))
            for obj in objs:
                obj_string = obj['size'] + ' ' + obj['color'] + ' ' + obj['material'] + ' ' + obj['shape']
                label[primitive_list.index(obj_string)] += 1
            # print(label)
            assert(np.sum(label) == len(objs))

            labels[fname] = {"96count": label.tolist()}
        
        with open(f'output/labels/{file[:-11]}labels.json', 'w') as outfile:
            json.dump(labels, outfile)
        
