class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        def search(idx):
            nonlocal ans
            if idx==len(cookies):
                ans = min(ans, max(state))
                return

            if len(state)<k:
                state.append(cookies[idx])
                search(idx+1)
                state.pop()

            for i in range(len(state)):
                if state[i]+cookies[idx] < ans:
                    state[i] += cookies[idx]
                    search(idx+1)
                    state[i] -= cookies[idx]

        state = []
        ans = float("inf")
        search(0)
        return ans


        
