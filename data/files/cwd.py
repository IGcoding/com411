# program to show current working directory and list of files
print ("Processing...")
import os
path = os.getcwd()
print(f"The Current Working Directory is {path}")
for file in os.listdir(path):
  print(f"The directory contains the following files: {file}")