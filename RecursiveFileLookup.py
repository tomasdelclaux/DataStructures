import os

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    foundFiles = list()
    
    # standarise path; remove trailing / in case it is passed into the function
    if path[-1] == "/":
        path = path[:-1]
    if os.path.isfile(path):
        if path.endswith(suffix):
            return [path]
    elif os.path.isdir(path):
        foundFiles = _find_files(suffix, path, foundFiles)
    else:
        return "Path not found"
    return foundFiles


def _find_files(suffix, path, fileset):
    foundFiles = fileset
    for file in os.listdir(path):
        fpath = path + "/" + file
        if os.path.isfile(fpath):
            if file.endswith(suffix):
                foundFiles.append(fpath)
        elif os.path.isdir(fpath):
            _find_files(suffix, fpath, foundFiles)
        else:
            continue
    return foundFiles


def test1():
    files = find_files(".c", "testdir/")
    assert files == ['testdir/subdir3/subsubdir1/b.c', 'testdir/t1.c', 'testdir/subdir5/a.c', 'testdir/subdir1/a.c']

def test2():
    files = find_files(".xyb", "testdir/")
    assert files == []

def test3():
    files = find_files(".c","no_testdir/")
    assert files == "Path not found"

def test4():
    files = find_files(".c", "testdir/t1.c")
    assert files == ["testdir/t1.c"]

def test5():
    #empty suffix, all files returned
    files = find_files("", "testdir")
    assert files == ['testdir/subdir4/.gitkeep', 'testdir/subdir3/subsubdir1/b.h', 'testdir/subdir3/subsubdir1/b.c', 'testdir/t1.c', 'testdir/subdir2/.gitkeep', 'testdir/subdir5/a.h', 'testdir/subdir5/a.c', 'testdir/t1.h', 'testdir/subdir1/a.h', 'testdir/subdir1/a.c']

test1()
test2()
test3()
test4()
test5()