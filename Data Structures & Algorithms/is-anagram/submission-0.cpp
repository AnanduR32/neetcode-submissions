#include <algorithm>
class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size())
        {
            return false;
        }
        unordered_map<char, int> dict;

        for (int i = 0; i < s.size(); i++)
        {
            if (dict.find(s[i]) != dict.end())
            {
                dict[s[i]]++;
            }
            else
            {
                dict[s[i]] = 1;
            }
        }

        for (int i = 0; i < t.size(); i++)
        {
            if (dict.find(t[i]) != dict.end())
            {
                dict[t[i]]--;
            }
            else
            {
                dict[t[i]] = -1;
            }
        }

        bool result = std::all_of(dict.begin(), dict.end(), [](const auto& kv) { return kv.second == 0; });
        return result;
    }
};
