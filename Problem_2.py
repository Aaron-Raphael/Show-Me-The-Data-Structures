'''
2. Finding Files

For this problem, the goal is to write code for finding all files under a directory (and all directories beneath it) that end with ".c"
'''

import os


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.
    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.
    There are no limit to the depth of the subdirectories can be.
    Args:
      suffix(str): suffix of the file name to be found
      path(str): path of the file system
    Returns:
       a list of paths
    """


    if path is None:
        return "No path specified"
    elif not isinstance(path, str):
        return "Path isn't a valid path"

    files = []

    # If the path is adirectory
    if os.path.isdir(path):
        # For all files in the current directory
        for file in os.listdir(path):

            # Form path by concatination
            file_path = os.path.join(path, file)

            # If file is found with given sufix then append filename to list
            if os.path.isfile(file_path):

                if file.endswith(suffix):
                    files.append((file_path.split('\\'))[-1])

            # If file is a subdirectory use recursion to proceed
            if os.path.isdir(file_path):
                new_files = find_files(suffix, file_path)

                files.extend(new_files)
   
   # If the given path is a file with given extention
    else:
        if path.endswith(suffix):
            files.append((path.split('/'))[-1])
    
    return files

# Testing preparation
path_base = os.getcwd() + '/testdir'

# Normal Cases:
print(find_files(suffix='c', path=path_base))
# ['a.c', 'b.c', 'a.c', 't1.c']

print(find_files(suffix='h', path=path_base))
# ['a.h', 'b.h', 'a.h', 't1.h']

print(find_files(suffix='z', path=path_base))
# []

# Edge Cases:
print(find_files(suffix='', path=path_base))
# ['a.c', 'a.h', '.gitkeep', 'b.c', 'b.h', '.gitkeep', 'a.c', 'a.h', 't1.c', 't1.h']

# Edge case test for revised code
print(find_files(suffix='.c', path='./testdir/subdir1/a.c'))
# ['a.c']