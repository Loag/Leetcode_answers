# 582
from types import List

class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        cont = {}
        for p, pp in zip(pid, ppid):
            if pp in cont:
                cont[pp].append(p)
            else:
                cont[pp] = [p]
                
        res = [kill]
        st = [kill]

        while st:
            node = st.pop()
            if node in cont:
                st.extend(cont[node])
                res.extend(cont[node])
                
        return res