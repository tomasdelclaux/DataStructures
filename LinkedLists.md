# Time and Space Complexity for Intersection and Union Methods in Linked Lists with potential duplicates

Important considerations:

    - Sets only contain unique values, but since linked lists can contain duplicates I assumed that such a count would need to be taken into consideration for union and intersection operations on linked lists.

Time & Space Complexity:
    Union:
        - The time complexity is O(n1+n2), where n1 and n2 are the lengths of each linked linked list, since an iteration must be done over each linked list.
        - For the space complexity, a dictionary was instantiated to keep track of the count (repeted values) in each linked list. The key for this dictionary is the value from the linked list and the value is a helper class called _count that contains attributes count1 and count2
          to keep track of the number of times a value is repeated in a linked list. The reason for this, is that if linkedList1 has X repeated 3 times, and linkedList2 has X repeated 2 times, then in the union Linked List x should appear repeated 3 times. Thus, the space complexity 
          would be the space complexity of the created union linked list and additonally the created dictionary. The worst case of the union linked list and the dictionary is that it contains all values from both linked lists. Hence, space complexity is O(2*(n1+n2))

    Intersection:
        - The time complexity is O(n1+n2), where n1 and n2 are the lengths of each linked linked list, since an iteration must be done over each linked list. This is higher than the time complexity of doing the same operation in sets, since these datastructures benefit from hashing
          to have O(1) lookups, and hence if this operation was done on a set the time complexity would be the same as the time complexity to traverse the smaller set. Creating a set for each linked list and then running the operation was discarded as repeated are considered important
          in the union and intersection operations between linked lists
        - For the space complexity, a dictionary was instantiated to keep track of the count (repeted values) in each linked list. The key for this dictionary is the value from the linked list and the value is a helper class called _count that contains attributes count1 and count2
          to keep track of the number of times a value is repeated in a linked list. The reason for this, is that if linkedList1 has X repeated 3 times, and linkedList2 has X repeated 2 times, then in the intersection Linked List x should appear repeated 2 times. Thus, the space complexity 
          would be the space complexity of the created intersection linked list and additonally the created dictionary. The worst case of the intersection linked list and the dictionary is that it contains all values from largest linked list. Hence, space complexity is O(max(n1,n2))

The function largest_shortest was created to obtain the largest and shortest of both linked lists. This was done in order to traverse first the shortest linked list, and hence reduce the space used when doing the intersection operation, since if a value is not in the dictionary it is
skipped.


