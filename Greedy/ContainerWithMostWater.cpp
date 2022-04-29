// You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
// Find two lines that together with the x-axis form a container, such that the container contains the most water.
// Return the maximum amount of water a container can store.
// Input: height = [1,8,6,2,5,4,8,3,7]
// Output: 49
// Start with the maximum width container and go to a shorter width container if there is a vertical line longer than the current containers shorter line. This way we are compromising on the width but we are looking forward to a longer length container.
// The aim is to maximize the area formed between the vertical lines. The area of any container is calculated using the shorter line as length and the distance between the lines as the width of the rectangle.
// Area = length of shorter vertical line * distance between lines
// We can definitely get the maximum width container as the outermost lines have the maximum distance between them. However, this container might not be the maximum in size as one of the vertical lines of this container could be really short.
#include<iostream>
#include<stdio.h>
using namespace std;
class Solution
{
public:
    int maxArea(vector<int> &height)
    {
        int i = 0, n = height.size(), j = n - 1, m = 0;
        for (int c = 0; c < n - 1; c++)
        {
            m = max(m, (j - i) * min(height[i], height[j]));
            if (height[i] < height[j])
                i++;
            else
                j--;
        }
        return m;
    }
};