import bpy
import numpy as np
import os
import itertools

# This script render a collection of NFT using Blender's native collection.
# To work correctly, you need to specify your NFT featueres in the feature_name variable

# Each blender collection represent a feature of an NFT.
# An NFT is a combination of each one of these
# These names correspond to blender's bult-in collections!
feature_name = ['head', 'body', 'cosmetic']

# Where to render NFT
output_dir = "/home/rage/Desktop/render"

# All NFT are combination of features, for convenience we
# store obj and feature in a mapping where the key is the feature name
# and the objects are the values
feature_to_obj = {}

def toggle_visibility(objs):
    '''Enables or disable obj visiblity'''
    if objs[0].hide_render == False:
        for obj in objs:
            obj.hide_render = True
    else:
        for obj in objs:
            obj.hide_render = False

def render_nft(filename):
    '''Render and save an NFT using current camera configuration'''
    bpy.context.scene.render.filepath = os.path.join(output_dir, (filename + ".jpg"))
    bpy.ops.render.render(write_still=True)
    

def prepare():
    # check if all features are present
    for f in feature_name:
        try:
            c = bpy.data.collections[f]
            feature_to_obj[f] = c.objects
            # set render visibility to false to all objects for later rendering
            toggle_visibility(feature_to_obj[f])

        except:
            print('The feature <{}> has not been found in the collection!'.format(f))
            feature_name.remove(f)


def render_all():
    # render all NFTs
    # TODO save NFT with correct names
    all_NFT = list(itertools.product(*feature_to_obj.values()))
    idx = 0
    for nft in all_NFT:
        toggle_visibility(nft)
        render_nft('nft_'+str(idx))
        toggle_visibility(nft)
        idx += 1
        
    
def main():
    prepare()
    render_all()
    
main()