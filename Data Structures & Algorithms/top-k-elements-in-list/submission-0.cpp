struct Node{
    int key;
    int count;
    Node(int key, int count) : key(key), count(count) {}
    bool operator<(const Node& other) const {
        return count < other.count;
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
        for (const auto& [k, v]: dict){
            pq.emplace(k,v);
        }

        vector<int> result;
        for (int i = 0; i < k; i++)
        {
            Node head = pq.top(); pq.pop();
            result.push_back(head.key);
        }

        return result;
    }
};
