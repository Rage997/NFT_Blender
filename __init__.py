import bpy
from . operator import RenderNFTOperator, PrepareNFTOperator
from . panel import NFTGEN_PT_Panel

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name" : "NFTGEN",
    "author" : "Rage",
    "description" : "",
    "blender" : (2, 80, 0),
    "version" : (0, 0, 1),
    "location" : "",
    "warning" : "",
    "category" : "Generic"
}

def register():
    bpy.utils.register_class(NFTGEN_PT_Panel)
    bpy.utils.register_class(RenderNFTOperator)
    bpy.utils.register_class(PrepareNFTOperator)

    bpy.types.Scene.theChosenObject = bpy.props.PointerProperty(type=bpy.types.Collection)

def unregister():
    bpy.utils.unregister_class(NFTGEN_PT_Panel)
    bpy.utils.unregister_class(RenderNFTOperator)
    bpy.utils.unregister_class(PrepareNFTOperator)

    del bpy.types.Object.theChosenObject
