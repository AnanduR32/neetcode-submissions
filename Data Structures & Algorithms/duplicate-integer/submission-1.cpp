class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::unordered_map<int,int> dict;
        for (int i : nums)
        {
            dict[i]++;
            if (dict[i] > 1) return true;
        }
        return false;
    }
};