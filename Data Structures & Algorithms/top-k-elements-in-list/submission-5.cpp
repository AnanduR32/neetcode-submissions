struct Node{
    int key;
    int count;
    Node(int key, int count) : key(key), count(count) {}
    bool operator<(const Node& other) const {
        // if (count == other.count) return key > other.key;
        return count > other.count;
    }
};

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> dict;
        priority_queue<Node> pq; 
        for (int n : nums){
            dict[n]++;
        }
        for (const auto& [key, v]: dict){
            pq.emplace(key,v);
            if (pq.size() > k) pq.pop();
        }

        vector<int> result;
        while (!pq.empty())
        {
            result.push_back(pq.top().key);
            pq.pop();
        }

        return result;
    }
};
