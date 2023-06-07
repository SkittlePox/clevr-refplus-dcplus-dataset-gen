import json
# read a json file from the scenes directory and print the number of objects in every scene
with open('output/scenes/CLEVR_trainA_scenes.json') as f:
    data = json.load(f)
    scenes = data['scenes']
    cumulative_object_count = 0
    total_scenes_with_duplicates = 0

    for scene in scenes:
        objs = scene['objects']
        cumulative_object_count += len(objs)
        obj_strings = set()
        for obj in objs:
            obj_string = obj['shape'] + ' ' + obj['size'] + ' ' + obj['material'] + ' ' + obj['color']
            if obj_string in obj_strings:
                total_scenes_with_duplicates += 1
                break
            else:
                obj_strings.add(obj_string)

    
    print("Average number of objects: " + str(cumulative_object_count/len(scenes)))
    print("Total scenes with duplicates: " + str(total_scenes_with_duplicates))