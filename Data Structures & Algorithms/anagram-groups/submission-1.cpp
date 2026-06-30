class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> intermediate;

        for (const string& str: strs)
        {
            auto key = getTokenKey(str);
            intermediate[key].push_back(str);
        }

        vector<vector<string>> output;
        for (auto [key, value]: intermediate)
        {
            output.push_back(value);
        }

        return output;
    }

    string getTokenKey(string str)
    {
        int alphabets[26] = {0};
        for (char ch : str) alphabets[ch - 'a']++;

        string key;
        for (int i: alphabets) key += to_string(i) + "#";
        return key;
    }
};
