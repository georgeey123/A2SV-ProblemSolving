class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def is_valid_state(state):
            return len(state) == len(nums)

        def get_candidates(state):
            # if len(state) == 0:
            candidate = [i for i in nums]
            # else:
            #     candidate = [i for i in nums if i > max(state)]

            return set(nums) - set(state)

        def search(state, solutions):
            if is_valid_state(state):
                solutions.append(state.copy())

            for candidate in get_candidates(state):
                state.append(candidate)
                search(state, solutions)
                state.remove(candidate)

            
        solutions = []
        state = []
        search(state,  solutions)
        return solutions