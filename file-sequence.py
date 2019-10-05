
import os 

directory = 'Path to the directory'
i = 0

os.chdir(directory)  

for f in os.listdir():
    f_name, f_ext = os.path.splitext(f)
    dst = str(i) + f_ext
    os.rename(f, dst) 
    i += 1 