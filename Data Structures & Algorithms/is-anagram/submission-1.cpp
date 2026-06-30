class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int> s_chars = getCountChars(s);
        unordered_map<char, int> t_chars = getCountChars(t);
        return areTokensSame(s_chars, t_chars); 
    }

    unordered_map<char, int> getCountChars(const string& s)
    {
        unordered_map<char, int> result;
        for (char ch: s){
            result[ch]++;
        }
        return result;
    } 

    bool areTokensSame(
        const unordered_map<char,int>& a, 
        const unordered_map<char,int>& b)
    {
        return a == b;
    }
};
