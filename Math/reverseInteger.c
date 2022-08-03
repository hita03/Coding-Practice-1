// Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

// Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

// Example 1:

// Input: x = 123
// Output: 321
// Example 2:

// Input: x = -123
// Output: -321
// Example 3:

// Input: x = 120
// Output: 21


int reverse(int x){
        int pop=0,temp=0,rev=0;

        while(x!=0){
            pop=x%10;
            x/=10;
            
            
            if(rev > INT_MAX/10 || (rev == INT_MAX/10 && pop>7)) return 0;
            else if(rev < INT_MIN/10 || (rev == INT_MIN/10 && pop<-8)) return 0;
            else{
                temp=rev*10+pop;
                rev=temp;
                
            }

            // printf("%d ",INT_MIN);
            
            
        }
    return rev;
            
}