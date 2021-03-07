# One way to serialize a binary tree is to use pre-order traversal. When we encounter a non-null node, we record the node's value. If it is a null node, we record using a sentinel value such as #.

#      _9_
#     /   \
#    3     2
#   / \   / \
#  4   1  #  6
# / \ / \   / \
# # # # #   # #
# For example, the above binary tree can be serialized to the string "9,3,4,#,#,1,#,#,2,#,6,#,#", where # represents a null node.

# Given a string of comma separated values, verify whether it is a correct preorder traversal serialization of a binary tree. Find an algorithm without reconstructing the tree.

# Each comma separated value in the string must be either an integer or a character '#' representing null pointer.

# You may assume that the input format is always valid, for example it could never contain two consecutive commas such as "1,,3".


class Solution:
    def isValidSerialization(self, preorder: '') -> bool:
        ## APPROACH : GREEDY ##
		## LOGIC ##
		#	1. we start with root node, so slots = 1
		#	2. Each node consumes 1 slot and adds 2 slots so. -1 + 2
		#	3. Null node consumes 1 slot
		## TIME COMPLEXICITY : O(N) ##
		## SPACE COMPLEXICITY : O(1) ##
        
        nodes = 1
        for node in preorder.split(','):
            nodes -= 1
            if nodes < 0:
                return False
            if node != '#':
                nodes += 2
        
        print(nodes == 0)
        return nodes == 0

sol = Solution()
sol.isValidSerialization("9,3,4,#,#,1,#,#,2,#,6,#,#")