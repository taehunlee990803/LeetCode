class�Solution:
����def�longestPalindrome(self,�s:�str)�->�str:
��������if�len(s)�<=�1:
������������return�s
��������max_len�=�1
��������max_str�=�s[0]
��������#�for�i�in�range(len(s)-1):
��������#�����for�j�in�range(i,�len(s)):
��������#���������if�j-i+1�>�max_len�and�s[i:j+1]�==�s[i:j+1][::-1]:
��������#�������������max_len�=�j-i+1
��������#�������������max_str�=�s[i:j+1]
��������#�return�max_str

��������dp�=�[[False�for�_�in�range(len(s))]�for�_�in�range(len(s))]

��������for�i�in�range(len(s)):
������������
������������dp[i][i]�=�True
������������for�j�in�range(i):
����������������if�s[j]�==�s[i]�and�(i-j<=2�or�dp[j+1][i-1]):
��������������������dp[j][i]�=�True
��������������������if�i-j+1�>�max_len:
������������������������max_len�=�i-j+1
������������������������max_str�=�s[j:i+1]
��������return�max_str
"
"
