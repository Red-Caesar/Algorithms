n = 1
bad = 4
def isBadVersion(version: int) -> bool:
    if version == 1:
        return True
    else:
        return False


def bin_search(right, left):
    mid = (right + left) // 2
    if isBadVersion(mid) and not isBadVersion(mid-1):
        return mid
    if isBadVersion(mid):
        ans = bin_search(right-1, mid)
    else:
        ans = bin_search(mid, left+1)
    return ans

ans = bin_search(0, n)
print(ans)
