import sys
import os
from cx_Freeze import setup, Executable

# ADD FILES
files = ['icon.ico','haarcascade_frontalface_default.xml','encodings.pickle','dataset/']

# TARGET
target = Executable(
    script="face_rec.py",
    base="Win32GUI",
    icon="icon.ico"
)

# SETUP CX FREEZE
setup(
    name = "FaceRec",
    version = "1.0",
    description = "Modern GUI for Python applications",
    author = "Firdaus Nuur Rhamadhan",
    options = {'build_exe' : {'include_files' : files}},
    executables = [target]   
)
