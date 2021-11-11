# 582
from types import List
from collections import defaultdict

class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        # create new default dict with new list as the default
        cont = defaultdict(list)
        
        # iterate over process, and process parent. 
        for p, pp in zip(pid, ppid):
            # add the process to the parents list of children
            cont[pp].append(p)
        
        # the nodes we are going to kill. Start with the node to kill.
        res = [kill]

        # stack of nodes to iterate through
        st = [kill]

        # while the stack is not empty
        while st:
            # pop the top node off
            node = st.pop()

            # if the node is in our dict 
            if node in cont:
                # add to the stack to traverse
                st.extend(cont[node])

                # add to res to kill
                res.extend(cont[node])
                
        return res