# Problem: Leetcode 2265 - Count nodes equal to average of subtree
# Difficulty: Medium
# Link: https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/description/
# Time Complexity: O(n) as we iterate through the the tree nodes
# Space Complexity: O(1)
# Approach: For each node we recurse into its left and right subtree till we reach the end when the DFS return 0,0
# then the left sum and right sum for each subtree are calculated and added to subtree sum and subtree count\
# and then we will be able to check if the average is same as node.val


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        def dfs(node:TreeNode):
            if not node:
                return 0, 0
            left_sum,left_count = dfs(node.left)
            right_sum,right_count = dfs(node.right)
            subtree_sum = left_sum+right_sum + node.val
            subtree_count = left_count+right_count + 1

            if subtree_sum//subtree_count == node.val:
                nonlocal result
                result+=1
            return subtree_sum,subtree_count
        result = 0
        dfs(root)
        return result