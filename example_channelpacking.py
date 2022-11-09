import bpy
import os


# -- constants
IN_DIR = 'SourceTextures'
OUT_DIR = 'Output'
RESOLUTION = 1024
FILE_FORMAT = 'TARGA'

# -- make sure an output directory exists
if not os.path.exists(OUT_DIR):
   os.makedirs(OUT_DIR)

# -- set up render settings
bpy.context.scene.render.resolution_x = RESOLUTION
bpy.context.scene.render.resolution_y = RESOLUTION
bpy.context.scene.render.image_settings.file_format = FILE_FORMAT
bpy.context.scene.render.resolution_percentage = 100

# -- image node variables
node_metalness = bpy.context.scene.node_tree.nodes['M']
node_roughness = bpy.context.scene.node_tree.nodes['R']
node_occlusion = bpy.context.scene.node_tree.nodes['AO']

# -- iterate all metalness textures and channel pack a MRO texture
for image_name in os.listdir(IN_DIR):
    if image_name.endswith('_M.jpg'):
        print(f"PROCESSING TEXTURES: {image_name.replace('_M.jpg', '')}")

        # -- texture names
        tex_metalness = image_name
        tex_roughness = image_name.replace('_M.jpg', '_R.jpg')
        tex_occlusion = image_name.replace('_M.jpg', '_AO.jpg')

        # -- update input image nodes texture paths
        node_metalness.image.filepath = f'//{os.path.join(IN_DIR, tex_metalness)}'
        node_roughness.image.filepath = f"//{os.path.join(IN_DIR, tex_roughness)}"
        node_occlusion.image.filepath = f"//{os.path.join(IN_DIR, tex_occlusion)}"

        # -- render MRO texture
        tex_output = image_name.replace('_M.jpg', '_MRO.tga')
        bpy.context.scene.render.filepath = f"//{os.path.join(OUT_DIR, tex_output)}"
        bpy.ops.render.render(write_still=True)
