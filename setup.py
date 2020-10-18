import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(packages=[], excludes=[
], includes=[], include_files=[])

base = None if sys.platform == 'win32' else None

executables = [
    Executable('app.py', base=base, targetName='NBwar-setup')
]

setup(name='NBwar-player-setup',
      version='1.0.0',
      description='Setup mods for NBwar',
      options=dict(build_exe=buildOptions),
      executables=executables)
