class Solution {
public:
    string encodingSymbol = "!#1$#!";
    string encode(vector<string>& strs) {
        string result;
        for (string str: strs)
        {
            result += str + encodingSymbol;
        }
        return result;
    }

    vector<string> decode(string s) 
    {
        vector<string> result;
        string temp;
        int pattern_ptr = 0;
        int string_ptr_start = 0;
        int string_ptr_end = 0;
        for(int string_ptr_end = 0; string_ptr_end <= s.size(); string_ptr_end++)
        {
            if (pattern_ptr == encodingSymbol.size())
            {
                auto word = s.substr(string_ptr_start, (string_ptr_end - string_ptr_start - pattern_ptr));
                result.push_back(word);
                string_ptr_start = string_ptr_end;
                pattern_ptr = 0;
            }
            else 
            {
                if (s[string_ptr_end] == encodingSymbol[pattern_ptr]) pattern_ptr++;
                else pattern_ptr = 0;
            }
        }

        return result;
    }
};
