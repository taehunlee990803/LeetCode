#�Definition�for�singly-linked�list.
#�class�ListNode:
#�����def�__init__(self,�val=0,�next=None):
#���������self.val�=�val
#���������self.next�=�next
class�Solution:
����def�getDecimalValue(self,�head:�ListNode)�->�int:
��������ans�=�''
��������if�head�is�None:

������������return�
��������temp�=�head
��������while�temp:
������������ans�=�ans�+�str(temp.val)
������������temp�=�temp.next
��������return�int(ans,2)

[
