class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        counter = 0
        ref = {
            "type": 0,
            "color": 1, 
            "name": 2
        }
        
        for i in items:
            if i[ref[ruleKey]] == ruleValue:
                counter += 1
                
        return counter