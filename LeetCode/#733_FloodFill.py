image = [[0,0,0],[0,0,0]]
sr, sc, color = 0, 0, 0
queue = []
step = [(-1, 0), (1, 0), (0, -1), (0, 1)]
base = image[sr][sc]
queue.append((sr, sc))
while queue:
    sr, sc = queue.pop()
    if image[sr][sc] == base:
        image[sr][sc] = color
        for pair in step:
            n_sr, n_sc = sr+pair[0], sc+pair[1]
            if 0 <= n_sr < len(image) and 0 <= n_sc < len(image[0]) and image[n_sr][n_sc] != color:
                queue.insert(0, (n_sr, n_sc))
print(image)
