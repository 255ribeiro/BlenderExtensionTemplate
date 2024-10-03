import subprocess
from pathlib import Path


from pyuac import main_requires_admin

@main_requires_admin
def main():
    bl_ver = input("type blender version to make symlink\n")

    cwd_path = Path().absolute()
    ext_name = cwd_path.name
    bl_addons_path = Path().home() / 'AppData' / 'Roaming' / 'Blender Foundation' / 'Blender' / bl_ver / 'scripts' / 'addons' / ext_name
    bl_addons_path.symlink_to(cwd_path)


if __name__ == "__main__":
    main()

