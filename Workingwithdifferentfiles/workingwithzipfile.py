from pathlib import Path
from zipfile import zipfile
#zip= zipfile("files.zip", "w")
#for path in Path("ecommerce").rglob("*.*"):
#    zip.write(path)
#zip.close() 
with zipfile("files.zip") as zip:
     print(zip.namelist())
     info=zip.getinfo(r"C:\Users\nakul\OneDrive\Documents\pythonprogrammes\pythonresume\parentpackage\__init__.py")
     print(info.file_size)
     print(info.compress_size)
     zip.extractall()
