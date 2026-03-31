class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # max_reach 記錄目前能到達的最遠位置
        max_reach = 0
        
        for i, jump in enumerate(nums):
            # 如果目前的位置已經超過了最遠射程，代表跳不到了
            if i > max_reach:
                return False
            
            # 更新最遠射程：目前的射程 vs 從當前位置起跳的新距離
            max_reach = max(max_reach, i + jump)
            
            # 如果射程已經覆蓋了最後一個位置，直接提早收工
            if max_reach >= len(nums) - 1:
                return True
                
        return True