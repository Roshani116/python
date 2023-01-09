import sys

if len(sys.argv) == 1:
    print("USAGE: python commandlinearegument.py <password>")
else:
    password = sys.argv[1]
    print("password", password)
print(sys.argv)
#python commandlinearegument.py 1234  provide password as 1234
#type ls command directory from the current directory.
