#include<string>
using namespace std;
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int n = s.length();

        int res = 0;
        for (int i = 0; i < n; i++) {
            for (int j = i; j < n; j++) {
                if (checkRepetition(s, i, j)) {
                    res = max(res, j - i + 1);
                }
            }
        }

        return res;
    }

    int checkRepetition(string& s, int i, int j) {
        int check[128]={0};

        for (int k = i; k <= j; k++) {
            char c = s[k];
            check[c]++;
            if (check[c] > 1) {
                return 0;
            }
        }

        return 1;
    }
};