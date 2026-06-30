class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> interim;
        for (string str : strs)
        {
            string key = getKey(str);
            interim[key].push_back(str);
        }

        vector<vector<string>> output;
        for (const auto& [key,value]: interim)
        {
            output.push_back(value);
        }

        return output;
    }



    string getKey(string str)
    {
        int alphabets[26] = {0};
        for (char st: str) alphabets[st - 'a']++;
        string key;
        for (int i = 0; i < 26; i++) key += to_string(alphabets[i]) + "#";
        return key;
    }
};
