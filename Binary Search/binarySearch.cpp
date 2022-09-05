// Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

// You must write an algorithm with O(log n) runtime complexity.

 

// Example 1:

// Input: nums = [-1,0,3,5,9,12], target = 9
// Output: 4
// Explanation: 9 exists in nums and its index is 4
// Example 2:

// Input: nums = [-1,0,3,5,9,12], target = 2
// Output: -1
// Explanation: 2 does not exist in nums so return -1
class Solution {
public:
    int binarySearch(int l, int r, vector<int>& nums, int target){
        int m;
        if(r>=l){
            m = l+ (r-l)/2;
            cout<<m<<endl;
            if(target == nums[m]){
                return m;
            } 
            if(target > nums[m]) return binarySearch(m+1, r, nums, target);
            else{
                return binarySearch(l, m-1, nums, target);
            }
        }
        else{
            return -1;        
        }
    }
    int search(vector<int>& nums, int target) {
        
        int l = 0;
        int r = nums.size()-1;
        return binarySearch(l,r,nums,target);
 
    }
};