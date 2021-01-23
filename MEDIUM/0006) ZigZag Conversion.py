"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);


Example 1:
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I

Example 3:
Input: s = "A", numRows = 1
Output: "A"
"""

def convert(self, s: str, numRows: int) -> str:
    length = s.__len__()

    li = [[] for _ in range(numRows)]

    count = 0
    while (count < length):
        for i in range(numRows):
            if (count < length):
                li[i].append(s[count])
                count += 1
            else:
                break

        for j in range(numRows - 2, 0, -1):
            if (count < length):
                li[j].append(s[count])
                count += 1

                temp_len = li[0].__len__()

                for k in range(numRows):
                    if (li[k].__len__() is temp_len):
                        li[k].append(" ")
            else:
                break

    ans = [val for temp in li for val in temp if val is not " "]
    ans = "".join(ans)

    return ans