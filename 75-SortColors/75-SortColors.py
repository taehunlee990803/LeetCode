class�Solution:
����def�sortColors(self,�nums:�List[int])�->�None:
��������"""
��������Do�not�return�anything,�modify�nums�in-place�instead.
��������"""
��������count0�=�0
��������count1�=�0
��������count2�=�0

��������for�num�in�nums:
������������if�num�==�0:�count0�+=�1
������������elif�num�==�1:�count1�+=�1
������������else:�count2�+=�1

��������arr�=�[]
��������for�i�in�range(0,count0):
������������arr.append(0)
��������for�i�in�range(0,count1):
������������arr.append(1)
��������for�i�in�range(0,count2):
������������arr.append(2)


��������for�i�in�range(0,len(arr)):

������������nums[i]�=�arr[i]
�����
[
