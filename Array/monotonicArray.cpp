
#include <iostream>
#include <vector>
#include<stdio.h>
#include<stdlib.h>
using namespace std;


class Solution {
public:

    bool isMonotonic(vector<int>& nums) {
        return decrease(nums) || increase(nums);
    }
        bool increase(vector<int>& nums){
        for(int i=0; i<nums.size()-1;i++){
                if(nums[i]>nums[i+1]) return false;
            }
            return true;
        }    
        
    
    bool decrease(vector<int>& nums){
        for(int j=0; j<nums.size()-1;j++){
                if(nums[j]<nums[j+1]) return false;
            }
            return true;

        }    
    

};



class Solution {
public:
    bool isMonotonic(vector<int>& nums) {

        for(int i=0; i<nums.size();i++){
            for(int j=i+1;j<nums.size()-1;j++){
                cout<<nums[i]<<nums[j]<<nums[j+1];
                if(nums[i]>nums[j] && nums[j]<nums[j+1]) return false;
                if(nums[i]<nums[j] && nums[j]>nums[j+1]) return false;
            }
            
        }    
        return true;
    }

};

int main(){

    vector<int> vect{1,3,2};
    Solution obj = Solution();
    obj.isMonotonic(vect);
}