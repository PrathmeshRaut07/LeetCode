class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time=0
        flag=0
        while tickets[k]!=0:
            for i in range(len(tickets)):
                if tickets[i]!=0:
                    time=time+1
                    tickets[i]=tickets[i]-1
                    if tickets[i]==0 and i==k:
                        break
                else:
                    continue
        return time               




        
