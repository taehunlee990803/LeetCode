#�Definition�for�a�binary�tree�node.
#�class�TreeNode:
#�����def�__init__(self,�val=0,�left=None,�right=None):
#���������self.val�=�val
#���������self.left�=�left
#���������self.right�=�right
class�Solution:
����def�findTarget(self,�root:�Optional[TreeNode],�k:�int)�->�bool:
��������num_set�=�set()
��������queue�=�deque([root])

��������while�queue:
������������if�(k�-�node.val)�in�num_set:
����������������return�True
������������else:
����������������num_set.add(node.val)
����������������if�node.left:
��������������������queue.append(node.left)
����������������if�node.right:
��������������������queue.append(node.right)
��������return�False�
������������node�=�queue.popleft()
������������#�print(num_set,�node.val)

������������
