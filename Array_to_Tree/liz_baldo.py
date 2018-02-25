"""
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

Source: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/#/description
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


#DO NOT CHANGE THIS CLASS
class Solution(object):
    def sortedArrayToBST(self, nums):
        
        if not nums:
            return None

        mid = len(nums) // 2

        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])

        return root
        """
        :type nums: List[int]
        :rtype: TreeNode
        """

def dummy(nums):
	return treeNodeToString(Solution().sortedArrayToBST(nums))
	
def treeNodeToString(root):
    if not root:
        return "[]"
    output = ""
    queue = [root]
    current = 0
    while current != len(queue):
        node = queue[current]
        current = current + 1
        if not node:
            output += "null, "
            continue
        output += str(node.val) + ", "
        queue.append(node.left)
        queue.append(node.right)
    return "[" + output[:-2] + "]"

#test cases
def main():
    nums = [-10,-3,0,5,9,4,7,12]
    print ("expected result is [0,-3,9,-10,null,5]")
    print ("your output is {}".format(dummy(nums)))

if __name__ == "__main__":
    main()
