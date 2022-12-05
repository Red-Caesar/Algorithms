from typing import List
class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties = sorted(properties, key=lambda x: (x[0], x[1]))
        cnt = 0
        local_maximum = -1
        maximum = -1
        prev_num = -1
        i = len(properties)-1
        while i > -1:
            if properties[i][0] != prev_num:
                maximum = local_maximum
                prev_num = properties[i][0]
                if maximum < properties[i][1]:
                    local_maximum = properties[i][1]
                    continue    
            if properties[i][0] == prev_num:
                if properties[i][1] < maximum:
                    cnt += 1 
            i -= 1
        return cnt

s = Solution()
print(s.numberOfWeakCharacters([[5,5],[6,3],[3,6]]))
print(s.numberOfWeakCharacters([[2,2],[3,3]]))
print(s.numberOfWeakCharacters([[1,5],[10,4],[4,3]]))
print(s.numberOfWeakCharacters([[4,5],[1,1],[2,3]]))
print(s.numberOfWeakCharacters([[1,1],[2,1],[2,2],[1,2]]))
print(s.numberOfWeakCharacters([[7,9],[10,7],[6,9],[10,4],[7,5],[7,10]]))
