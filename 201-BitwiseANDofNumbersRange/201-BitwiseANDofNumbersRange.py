class�Solution:
����def�rangeBitwiseAnd(self,�left:�int,�right:�int)�->�int:
��������shift�=�0
��������while�left�<�right:
������������left�>>=�1
������������right�>>=1
������������shift�+=�1
��������print(left,�right,�shift�)
��������return�left�<<�shift
5
