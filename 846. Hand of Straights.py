class Solution(object):
    def isNStraightHand(self, hand, W):
        """
        :type hand: List[int]
        :type W: int
        :rtype: bool
        """
        if len(hand)%W: return False
        
        #O(n)
        counts = collections.Counter(hand)
        
        #O(k) < O(n)
        uniques = sorted(counts.keys())
        
        #O(n)
        for card in uniques:
            while counts[card]>0:
                for i in range(W):
                    if counts[card+i]>0:
                        counts[card+i] -=1
                    elif sum(counts.values())==0:
                        return True
                    else:
                        return False

                
        return sum(counts.values())==0
         
            
        
        
         
            
        
        
