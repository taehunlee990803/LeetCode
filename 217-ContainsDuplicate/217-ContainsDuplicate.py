class�Solution:
����def�containsDuplicate(self,�nums:�List[int])�->�bool:
��������nums2�=�set(nums)
��������if�len(nums2)�!=�len(nums):
������������return�True
��������return�False
