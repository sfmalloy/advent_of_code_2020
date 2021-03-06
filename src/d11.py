import fileinput
from copy import deepcopy

grid1 = [[c for c in l.strip()] for l in fileinput.input()]
grid2 = deepcopy(grid1)

def next_seat_p1(r, c, grid):
  if grid[r][c] == '.':
    return '.'
  
  start_row = r-1 if r > 0 else r
  end_row = r+1 if r < len(grid)-1 else r
  start_col = c-1 if c > 0 else c
  end_col = c+1 if c < len(grid[r])-1 else c

  filled = 0
  for R in range(start_row, end_row+1):
    for C in range(start_col, end_col+1):
      if not (R == r and C == c) and grid[R][C] == '#':
        filled += 1
  
  if grid[r][c] == 'L' and filled == 0:
    return '#'
  elif grid[r][c] == '#' and filled >= 4:
    return 'L'
  return grid[r][c]

def next_seat_p2(r, c, grid):
  if grid[r][c] == '.':
    return '.'
  
  start_row = r-1 if r > 0 else r
  end_row = r+1 if r < len(grid)-1 else r
  start_col = c-1 if c > 0 else c
  end_col = c+1 if c < len(grid[r])-1 else c

  filled = 0
  for R in range(start_row, end_row+1):
    for C in range(start_col, end_col+1):
      if R == r and C == c:
        continue
      
      temp_r = R
      temp_c = C
      while (r in [0, len(grid)-1] or 0 < temp_r < len(grid)-1) \
        and (c in [0, len(grid[R])-1] or 0 < temp_c < len(grid[R])-1) \
        and grid[temp_r][temp_c] == '.':
        if temp_r < r:
          temp_r -= 1
        elif temp_r > r:
          temp_r += 1
        if temp_c < c:
          temp_c -= 1
        elif temp_c > c:
          temp_c += 1
      if grid[temp_r][temp_c] == '#':
        filled += 1
  if grid[r][c] == 'L' and filled == 0:
    return '#'
  elif grid[r][c] == '#' and filled >= 5:
    return 'L'
  return grid[r][c]

def next_grid(grid, part2):
  changed = 0
  new_grid = deepcopy(grid)
  for r in range(len(grid)):
    for c in range(len(grid[r])):
      if part2:
        new_grid[r][c] = next_seat_p2(r, c, grid)
      else:
        new_grid[r][c] = next_seat_p1(r, c, grid)
      if grid[r][c] != new_grid[r][c]:
        changed += 1
  return new_grid, changed

def run(grid, part2):
  changed = -1
  while changed != 0:
    grid, changed = next_grid(grid, part2)

  filled = 0
  for r in grid:
    for c in r:
      if c == '#':
        filled += 1
  return filled

print(run(grid1, False))
print(run(grid2, True))
