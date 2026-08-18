class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # h hours to complete all piles
        # find speed -> bananas eaten per hour
        # speed can range from 1 to max(piles),
        # i.e either just eat 1 per hour or one pile per hour
        # as, in an hour can only eat from one pile, max speed is pile per hour
        # perform binary search to find ideal speed between 1..max(piles) 

        lower = 1
        upper = max(piles)
        lastIdealSpeed = upper
        while lower <= upper:
            speed = (lower + upper) // 2

            # Check if can consume all bananas in each pile in h time
            time = sum(int(math.ceil(pile/speed)) for pile in piles)
            if time <= h:
                lastIdealSpeed = speed
                upper = speed - 1
            else:
                lower = speed + 1            

            
        
        return lastIdealSpeed