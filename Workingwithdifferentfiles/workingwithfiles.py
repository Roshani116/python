from pathlib import Path
from time import ctime
import shutil
path = Path(r"C:\Users\nakul\OneDrive\Documents\pythonprogrammes\pythonresume\parentpackage\__init__.py")
path.exists()
#path.rename("init.txt")
#path.unlink()
print(ctime(path.stat().st_ctime))
print(path.stat())
#with open ("__init__.py","r") as file:
print(path.read_text())
path.write_text("...")



#new code 
#source = Path(r"C:\Users\nakul\OneDrive\Documents\pythonprogrammes\pythonresume\parentpackage\package.py")
#target= path/"init.txt"
#target.write_text(source.read_text())
#above code  is tidious for that  we have wrritten below code.
#shutil.copy(source,target)
#target.write_text(source.read_text)
