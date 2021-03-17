# Made by https://github.com/flarfmatter
# Maintained at https://github.com/flarfmatter/spleeteryeeter

import os
import config
import random
import subprocess

# Variables
filepath = ""
stem_count = None
waitMessages = [*(line.strip() for line in open("./other/waitMessages.txt",).readlines() if line[0] != '#' and len(line) > 1)]

# Setting path of input file
while True:
    filepath = input("Please type in the full path of the file you wanna split:\n\t")
    if os.path.exists(filepath): break
    print(f"Path \"{filepath}\" doesn't exist.")


# Getting amount of stems
while True:
    stem_count = input("How many stems do you wanna extract? (4),5,2: ")
    if stem_count in ['4', '5', '2']: break
    print("Only 4, 5, and 2 are valid numbers.")
if stem_count == "" or stem_count is None:
    stem_count = '4'

print(f"\nPlease wait..\n{random.choice(waitMessages)}..")
path = config.output_path if config.output_path is not None else os.path.join(
    os.path.join(os.path.dirname(os.path.abspath(__file__))), "exports"
)

if not os.path.isdir(path):
    os.mkdir(path)

out = subprocess.run(
    f"\"{config.python}\" -m spleeter separate \"{filepath}\" -p spleeter:{stem_count}stems -o \"{path}\"",
    shell=True, capture_output=True
)
lines = out.stdout.decode().split("\n")
for i in range(len(lines)):
    words = lines[i].split(' ')
    if i+1 <= int(stem_count):
        if config.debug:
            print(lines[i])
        else:
            if "succes" in lines[i]:
                print(f"{i+1}/{stem_count} succeeded.")
            else:
                print(f"An error might've happened at {i+1}/{stem_count}")
