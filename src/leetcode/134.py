class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        extra = 0
        req = 0
        s = 0

        for i in range(len(gas)):
            extra += gas[i] - cost[i];

            if (extra < 0):
                req += extra;
                extra = 0;
                s = i + 1;

        return s if extra + req >= 0 else -1;

