class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        def getCharDist(s:str, data_1:dict=None) -> Optional[dict]:
            data:dict = dict()
            for char in s:
                if data_1 and char not in data_1:
                    return None
                data[char] = data.get(char, 0) + 1
            return data

        data_1 = getCharDist(s)
        data_2 = getCharDist(t, data_1)

        if data_2 is None:
            return False
        
        for k,v in data_1.items():
            if k not in data_2 or (k in data_2 and v != data_2[k]):
                return False
        
        return True

