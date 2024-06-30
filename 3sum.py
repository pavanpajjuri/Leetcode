class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        # d = {}
        # for idx,val in enumerate(nums):
        #     d[0-val] = idx
        # # print(d)    
        # for i in range(n):
        #     for j in range(i+1,n):
        #         if nums[i]+nums[j] in d:
        #             lst = sorted([nums[i],nums[j],-(nums[i]+nums[j])])
        #             if lst not in ans and d[nums[i]+nums[j]]>j:
        #                 ans.append(lst) 

        d = {}
        for i in range(n):
            for j in range(i+1,n):
                complement = 0-(nums[i]+nums[j])
                if complement in d:
                    print(i,j,d[complement])
                    print(nums[i],nums[j],complement)
                    print("...")
                    [idx1,idx2] = d[complement]
                    lst = sorted([nums[i],nums[j],complement])
                    if lst not in ans:
                        # print(lst)
                        ans.append(lst)
                else:
                    d[complement]=[i,j]



        # for i in range(n):
        #     for j in range(i+1,n):
        #         for k in range(j+1,n):
        #             if nums[i]+nums[j]+nums[k] == 0 :
        #                 lst = sorted([nums[i],nums[j],nums[k]])
        #                 if lst not in ans:
        #                     ans.append(lst)
        return ans
        