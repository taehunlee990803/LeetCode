class Solution:
    def simplifyPath(self, path: str) -> str:
        dirOrFiles = []
            if dirOrFiles and elem == "..":
                dirOrFiles.pop()
            elif elem not in [".", "", ".."]:
                dirOrFiles.append(elem)
                
        path = path.split("/")
        for elem in path:
        print(dirOrFiles)
        print(path)
        return "/" + "/".join(dirOrFiles)
"
