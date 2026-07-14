#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int maxArea(vector<int>& height) {
        int l = 0, r = height.size() - 1;
        int maxArea = 0;
        
        while (l < r) {
            int width = r - l;
            int h = min(height[l], height[r]);
            maxArea = max(maxArea, width * h);
            
            // Move the smaller height pointer
            if (height[l] < height[r])
                l++;
            else
                r--;
        }
        return maxArea;
    }
};
