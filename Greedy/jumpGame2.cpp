// Given an array of non-negative integers nums, you are initially positioned at the first index of the array.

// Each element in the array represents your maximum jump length at that position.

// Your goal is to reach the last index in the minimum number of jumps.

// You can assume that you can always reach the last index.


// Example 1:

// Input: nums = [2,3,1,1,4]
// Output: 2
// Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
// Example 2:

// Input: nums = [2,3,0,1,4]
// Output: 2


class Solution {
public:
    int jump(vector<int>& nums) {
        int n=nums.size()-1,end=0,count=0;
        while(end<n){
            count++;
            int maxend = end + 1;
            for(int i=0; i<=end; i++){
                if(nums[i]+i >= n) return count;
                    maxend=max(maxend,nums[i]+i);
                // cout<<maxend<<endl;
            }
            end = maxend;
        }
        return count;
    }  
};