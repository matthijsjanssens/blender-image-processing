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
node_alpha = bpy.context.scene.node_tree.nodes['A']
node_diffuse = bpy.context.scene.node_tree.nodes['D']

# -- iterate all metalness textures and channel pack a MRO texture
for image_name in os.listdir(IN_DIR):
    if image_name.endswith('_A.jpg'):
        print(f"PROCESSING TEXTURES: {image_name.replace('_A.jpg', '')}")

        # -- texture names
        tex_alpha = image_name
        tex_diffuse = image_name.replace('_A.jpg', '_D.jpg')

        # -- update input image nodes texture paths
        node_alpha.image.filepath = f'//{os.path.join(IN_DIR, tex_alpha)}'
        node_diffuse.image.filepath = f"//{os.path.join(IN_DIR, tex_diffuse)}"

        # -- render MRO texture
        tex_output = image_name.replace('_A.jpg', '_D.tga')
        bpy.context.scene.render.filepath = f"//{os.path.join(OUT_DIR, tex_output)}"
        bpy.ops.render.render(write_still=True)
