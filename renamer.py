import os
import pandas as pd
from pathlib import Path as path


path_to_shp = os.path.dirname(os.path.abspath('__file__'))
path_to_input_dir = os.path.join(path_to_shp, 'ssa1')
path_to_input_dir_2 = path('haz_test')
input_files = os.listdir(path_to_input_dir)
# print(path_to_pwd)

df = pd.read_csv('prov_code.csv')
df = df.set_index('Name_2')

for file in input_files:
    # print(file)
    # if file.endswith(".shp"):
    filename_without_ext = os.path.splitext(file)[0] 
    print(filename_without_ext)
    extension = os.path.splitext(file)[1]
    print(extension)
    # shname = file.stem
    # print(file)
    src=file
    split_string = file.split("_")
    substring = split_string[0]
    # print(substring)
    fname = df.loc[substring, 'PHCode_Pro_SS']
    # print(fname)
    new_filename = fname + extension
    print(src)
    os.rename(os.path.join(path_to_input_dir, file), os.path.join(path_to_input_dir, new_filename))