## Time and Space Complexity Analysis for the recursive find file method

Consider a path as an object of length n, where n is the number of files and directories inside the path:

Time complexity is O(n) because every file must be checked.

Space complexity in the worst case would be O(n), this would be the case, where all the files in a given path have the same ending. 

The first bit of the code is meant to standarise the input of the path and remove a possible trailing edge '/' at the end of the path. By doing this, paths "example" and "example/" can be handled consistently through the rest of the function
Also, before running the recursion, whether the path is a file or a valid path must be checked. In this case, if the path is a file the suffix check is done. If the path is not valid a string "Path not found" is returned.

