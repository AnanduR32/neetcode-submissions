#include <unordered_set>
using namespace std;

class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> set(nums.begin(), nums.end());
        if (set.size() == nums.size())
        {
            return false;
        }
        return true;
    }
};
