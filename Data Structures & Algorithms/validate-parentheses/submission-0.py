class Solution:
    def isValid(self, s: str) -> bool:
        # 建立配對字典，Key 為右括號，Value 為對應的左括號
        mapping = {")": "(", "}": "{", "]": "["}
        stack = []

        for char in s:
            # 如果是右括號
            if char in mapping:
                # 彈出堆疊最上方的元素（如果堆疊是空的，給個佔位符 '#'）
                top_element = stack.pop() if stack else '#'
                
                # 檢查彈出的左括號是否跟目前的右括號配對
                if mapping[char] != top_element:
                    return False
            else:
                # 如果是左括號，就推入堆疊
                stack.append(char)

        # 最後如果堆疊是空的，代表全部配對成功
        return len(stack) == 0