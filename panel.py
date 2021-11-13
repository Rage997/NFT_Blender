import bpy


class NFTGEN_PT_Panel(bpy.types.Panel):
    bl_idname = "NFTGEN_PT_Panel"
    bl_label = "GUI Panel for NFT generator addon"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "NFT"
    bl_context = "objectmode"

    def draw(self, context):

        layout = self.layout

        row = layout.row()
        row.label(text="NFT Generator Addon")


        box = layout.box()
        box.label(text="Render All NFT!")
        box.operator("object.generator_nft")