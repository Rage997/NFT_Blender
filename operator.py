import bpy
from . nft_utils import *


class RenderNFTOperator(bpy.types.Operator):
    bl_idname = "object.generator_nft"
    bl_label = "Addon to help the rendering of NFT"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        print('Rendering all NFTs...')

        try:
            prepare()
            render_all()
            print('Done rendering NFTs!')
        except Exception as e:
            print("An error occured generating NFT!")
        
        return {'FINISHED'}


