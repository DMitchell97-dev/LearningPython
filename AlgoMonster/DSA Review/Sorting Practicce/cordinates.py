def robot_return_to_origin(moves: str) -> bool:
    vertical, horizontal = 0, 0
    for move in moves.lower():
        if move == "u":
            vertical += 1
        elif move == "d":
            vertical -= 1
        elif move == "r":
            horizontal += 1
        elif move == 'l':
            horizontal -= 1

    return horizontal == 0 == vertical


if __name__ == "__main__":
    moves = input()
    res = robot_return_to_origin(moves)
    print("true" if res else "false")
