import os

from cx_Freeze import setup, Executable

path = "./assets"
asset_list = os.listdir(path)
asset_list_completa = [os.path.join(path, asset).replace("\\", "/") for asset in asset_list]
print(asset_list_completa)

executables = [Executable("main.py")]
files = {"include_files": asset_list_completa, "packages": ["pygame"]}

setup(
    name="InvadersZone",
    version="0.1",
    description="Invaders Zone app",
    options={"build_exe": files},
    executables=executables
)