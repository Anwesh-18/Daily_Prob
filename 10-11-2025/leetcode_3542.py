def minOperations(nums) -> int:
    stack=[-1]
    count=0
    for x in nums:
        while x<stack[-1]: stack.pop()
        if x>stack[-1]:
            count+=(x>0) 
            stack.append(x)
    return count

arr = [1,2,1,2,1,2]
print(minOperations(arr))