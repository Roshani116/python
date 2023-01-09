from pathlib import Path

path=Path("C:\\")
print(path.exists)
print(path.iterdir())
#[p for p in path.iterdir() if p.is_dir()] this code is list comprehension expression useful to get the files and directories
#limitations of list comprehension we cannot search by pattern or we cannot search recurssively.
paths=[p for p in path.iterdir() if p.is_dir()]
#for that we used glob method 
py_files=[p for p in path.glob("*.py")]
#py_files1=[p for p in path.rglob("*.py")]
print(paths)
print(py_files)
#print(py_files1)
