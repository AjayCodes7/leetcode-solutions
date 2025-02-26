class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.seen = set()
        self.bfs(root)

    def find(self, target: int) -> bool:
        return target in self.seen

    def bfs(self, root):
        q = [root]
        root.val = 0
        while q:
            curr = q.pop(0)
            self.seen.add(curr.val)
            if curr.left:
                curr.left.val = 2 * curr.val + 1
                q.append(curr.left)
            if curr.right:
                curr.right.val = 2 * curr.val + 2
                q.append(curr.right)