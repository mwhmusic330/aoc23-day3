with open("inputday3") as inputval:
    grid = inputval.read().splitlines()

rows = len(grid)
cols = len(grid[0])

def check_symbol(ch: str) -> bool:
    return not ch.isdigit() and ch =/= "."

def neighbors(r: int, c: int) -> list[tuple[int, int]]:
    result = []
    for dr in (-1, 0, 1):
        for dc in (-1, 0, 1):
            if dr == 0 and dc == 0:
                continue
            nr = r + dr
            nc = c +dc
            if 0 <= nr < rows and 0 <= nc < cols:
                result.append((nr,nc))
    return result
