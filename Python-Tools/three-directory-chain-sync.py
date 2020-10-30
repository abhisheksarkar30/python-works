import os
import shutil
import sys
from os import path


# Copy each file or all files recursively from a folder
def copy(src, destination_dir):
    try:
        if os.path.isfile(src):
            shutil.copy2(src, destination_dir)
        else:
            shutil.copytree(src, destination_dir)
    except Exception as e:
        print("Unable to copy: " + str(e))


# Create dir if doesn't exist
def create_dir(destination_dir):
    if not os.path.exists(destination_dir):
        try:
            os.makedirs(destination_dir)
        except Exception as e:
            print("Unable to create target dir: " + str(e))
            sys.exit(-1)


# Decision maker to keep which files and directories
def copy_logic(base_path, target_path, target2_path, destination, x):
    temp_base_path = base_path + "\\" + x
    temp_target_path = target_path + "\\" + x
    temp_target2_path = target2_path + "\\" + x
    temp_destination = destination + "\\" + x

    if not path.exists(temp_target_path) or not path.exists(temp_target2_path):
        copy(temp_base_path, temp_destination)
    else:
        if path.isdir(temp_base_path):
            create_dir(temp_destination)
            helper(temp_base_path, temp_target_path, temp_target2_path, temp_destination)
        elif path.isfile(temp_base_path):
            if (path.getmtime(temp_base_path) > path.getmtime(temp_target_path) and
                    path.getmtime(temp_base_path) > path.getmtime(temp_target2_path)):
                copy(temp_base_path, destination)
            elif (path.getmtime(temp_target_path) > path.getmtime(temp_base_path) and
                    path.getmtime(temp_target_path) > path.getmtime(temp_target2_path)):
                copy(temp_target_path, destination)
            else:
                copy(temp_target2_path, destination)


# Recursive walker to process all files from both the directory structure in nested manner
def helper(base_path, target_path, target2_path, destination):
    processed_dirs = set()
    for x in os.listdir(base_path):
        print("Currently processing: " + x)
        copy_logic(base_path, target_path, target2_path, destination, x)
        processed_dirs.add(x)

    for x in os.listdir(target_path):
        if not processed_dirs.__contains__(x):
            print("Currently processing: " + x)
            copy_logic(target_path, base_path, target2_path, destination, x)
            processed_dirs.add(x)
        else:
            print(x + " already processed")

    for x in os.listdir(target2_path):
        if not processed_dirs.__contains__(x):
            print("Currently processing: " + x)
            copy_logic(target2_path, base_path, target_path, destination, x)
            processed_dirs.add(x)
        else:
            print(x + " already processed")


def main():
    base_path = sys.argv[1]
    if not path.exists(base_path):
        print("Please provide valid base path!")
        exit()
    base_path = path.abspath(base_path)

    target_path = sys.argv[2]
    if not path.exists(target_path):
        print("Please provide valid target path!")
        exit()
    target_path = path.abspath(target_path)

    target2_path = sys.argv[3]
    if not path.exists(target2_path):
        print("Please provide valid target2 path!")
        exit()
    target2_path = path.abspath(target2_path)

    destination = os.getcwd() + "\\merged-dir"
    create_dir(destination)

    helper(base_path, target_path, target2_path, destination)


if __name__ == "__main__":
    main()
