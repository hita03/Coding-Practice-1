#include <bits/stdc++.h>
class Solution {
   public:
   // void printVector(vector <int> v){
   //    for(int i = 0; i < v.size(); i++)cout << v[i] << " ";
   //    cout << endl;
   // }
   bool repeatedSubstringPattern(string s) {
      int n = s.size();
      vector <int> dp(n);
      int i = 1;
      int j = 0;
      while(i < n){
         if(s[i] == s[j]){
            dp[i] = j+1;
            i++;
            j++;
         } else {
            if(j > 0){
               j = dp[j-1];
            } else {
               dp[i] = 0;
               i++;
            }
         }
      }
      return dp[n - 1] && n % (n - dp[n-1]) == 0;
   }
};
