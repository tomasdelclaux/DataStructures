# Active Directory Lookup Time and Space complexity using recursion

Recursion was chosen for the lookup function to leverage faster lookups.

Since the execution ends when a user is found and no data is added to a given data structure the space complexity is O(1)

The worst case time scenario for the lookup would be if all the sub_groups must be searched to see if the user is in one of them. The time complexity of each recusion stack is O(n) since iteration must have in each subgroup of a particular group.

Before running the recursion, whether the group is valid group class must be checked, this is done with the isinstance function.