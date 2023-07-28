import os
from pathlib import Path

# main_path = os.path.dirname(__file__)
# print('path1',main_path)
# file_path = os.path.join(main_path, 'public\index.html')
# print('filepath-1',file_path)
# # f = open(file_path)


# var = os.path.join(os.path.dirname(__file__), 'public\index.html')
# print(var)

BASE_DIR = Path(__file__).resolve().parent.parent
print('BASE_DIR', BASE_DIR)
BASE_DIR2 = os.path.dirname(os.path.abspath(__file__))
print('BASE_DIR2', BASE_DIR2)
TEMPLATE_DIR= os.path.join(BASE_DIR,'public\index.html')
print(type(TEMPLATE_DIR))
print('TEMPLATE_DIR', TEMPLATE_DIR)
STATIC_DIR = os.path.join(BASE_DIR,'node_modules')
print('STATIC_DIR', STATIC_DIR)
