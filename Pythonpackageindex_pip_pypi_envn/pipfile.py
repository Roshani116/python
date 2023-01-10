#when we install package using pip env , two files automatically get created pip file and piffle.lock
#this 2 files is used to keep dependandacies of our project and their version 
#Pip can export a list of all installed packages and their versions using the freeze command:
#py -m pip freeze
This is useful for creating Requirements Files that can re-create the exact versions of all packages installed in an environment.
“Requirements files” are files containing a list of items to be installed using pip install like so:
py -m pip install -r requirements.txt
py -m pip freeze > requirements.txt
py -m pip install -r requirements.txt
Requirements File Format
Requirements files serve as a list of items to be installed by pip, when using pip install. Files that use this format are often called “pip requirements.txt files”, since requirements.txt is usually what these files are named (although, that is not a requirement).
