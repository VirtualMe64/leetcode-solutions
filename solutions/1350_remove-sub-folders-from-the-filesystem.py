# Problem: https://leetcode.com/problems/remove-sub-folders-from-the-filesystem
# Runtime: 80 ms

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        tree = (False, {})

        for f in folder:
            curr = tree[1]
            parts = f.split("/")[1:]
            for i, part in enumerate(parts):
                last = i == len(parts) - 1
                if part in curr:
                    if curr[part][0]:
                        break
                    if last:
                        curr[part] = (True, {})
                        break
                    curr = curr[part][1]
                else:
                    curr[part] = (last, {})
                    curr = curr[part][1]

        out = []
        frontier = [(tree, "")]
        while len(frontier) > 0:
            (last, currNode), currPath = frontier.pop(-1)
            # print(currNode, currPath)

            if last:
                out.append(currPath)
                continue
            else:
                for key in currNode:
                    frontier.append((currNode[key], currPath + "/" + key))

        return out