from pathlib import Path
path=Path(r"C:\Program Files")
"""
Path("/usr/local/bin")
Path()
Path("ecommerce/__init__.py")
path()/path("ecommerce/__init__.py")
"""
path.home()
path.exists()
path.is_file()
path.is_dir()
p=path.name
print(p)
print(path.stem)
print(path.suffix)
print(path.parent)
path=path.with_name("workingwithpath.txt")
path=path.with_suffix(".txt")
print(path)
print(path.absolute())
