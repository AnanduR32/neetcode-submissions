class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> complementDict;
        int complement;
        for (int i = 0; i < nums.size(); i++)
        {
            complement = target - nums[i];
            if (complementDict.find(complement) != complementDict.end()){
                return {complementDict[complement], i};
            }
            complementDict[nums[i]] = i;
        }
        return vector<int>();
    }
};
