class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        vector<int> merged = nums1;
        merged.insert(merged.end(), nums2.begin(), nums2.end());

        sort(merged.begin(), merged.end());

        int n = merged.size();
        double med;

        if (n % 2 == 0)
        {
            med = (merged[n / 2 - 1] + merged[n / 2]) / 2.0;
        }
        else
        {
            med = merged[n / 2];
        }

        return med;
    }
};