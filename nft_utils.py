import bpy
import numpy as np
import os
import itertools
import json
#from sklearn.model_selection import ParameterGrid

# This script render a collection of NFT using Blender's native collection.
# To work correctly, you need to specify your NFT featueres in the feature_name variable

# Each blender collection represent a feature of an NFT.
# An NFT is a combination of each one of these
# These names correspond to blender's bult-in collections!
feature_name = ['head', 'body', 'cosmetic']

# Where to render NFT
output_dir = "/Users/pietrobianco/Desktop/NFT_Blender/render"

# All NFT are combination of features, for convenience we
# store obj and feature in a mapping where the key is the feature name
# and the items are arrays of blender's object
feature_to_obj = {}

# An array of json to keep track of each generated NFT
# Each element has the structure:
# {'feature_1': name,
#    'feature_2' : name.
#    'feature_x' : name,
#    'src' : filepath
#    }
nft_log = []

def toggle_visibility(objs):
    '''Enables or disable obj visiblity of an array of object''' 
    if objs[0].hide_render == False:
        for obj in objs:
            obj.hide_render = True
    else:
        for obj in objs:
            obj.hide_render = False

def render_save(filename):
    '''Render and save an NFT using current camera configuration'''
    render_path = os.path.join(output_dir, (filename + ".jpg"))
    bpy.context.scene.render.filepath = render_path
    bpy.ops.render.render(write_still=True)
    return render_path

def prepare():
    '''
     Creates a mapping for each feature of the correspoing objects
    
    '''
    for f in feature_name:
        try:
            c = bpy.data.collections[f]
            feature_to_obj[f] = c.objects
            # set render visibility to false to all objects for later rendering
            toggle_visibility(feature_to_obj[f])

        except:
            print('The feature <{}> has not been found in the collection!'.format(f))
            feature_name.remove(f)
    if len(feature_to_obj.items()) == 0:
        raise Exception('Error')

def generate_permutations(my_dict):
    """Generates all the permutations key/item of a dictionary.See: 
        https://stackoverflow.com/questions/38721847/how-to-generate-all-combination-from-values-in-dict-of-lists-in-python

    Args:
        my_dict ([any]): Input dictionary. Each key corresponds to an array of objects

    Returns:
        dict([]): Return a dictionary (? check)
    """    ''''''

    keys, values = zip(*my_dict.items())
    permutations_dicts = [dict(zip(keys, v)) for v in itertools.product(*values)]
    return permutations_dicts

def render_all():
    # render all NFTs
    # TODO save NFT with correct names
#    all_NFT = list(itertools.product(*feature_to_obj.values()))
    all_NFT = generate_permutations(feature_to_obj)
    idx = 0
    for nft in all_NFT:
        nft_name = ''
        nft_json = {}
        for feature in nft.keys():
            nft_json[feature] = nft[feature].name_full
        nft_name = '_'.join(nft_json.values())
        print('Rendering NFT {}'.format(nft_name))
        
        objs = list(nft.values())
        toggle_visibility(objs)
        rdr_path = render_save(nft_name)
        toggle_visibility(objs)
        nft_json['src'] = rdr_path
        
        print(nft_json)
        nft_log.append(nft_json)
        with open('nfts.json', 'w', encoding='utf-8') as f:
            json.dump(nft_log, f, ensure_ascii=False, indent=4)
            
if __name__ == "__main__":
    prepare()
    render_all()