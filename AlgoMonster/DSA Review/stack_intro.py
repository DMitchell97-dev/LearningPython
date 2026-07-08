
def execute(program: list[str]) -> list[int]:
    #Initialize the stack
    stack: list[int] = []
    for instruction in program:
        if instruction == "peek":
            # print out the top item in the stack
            print(stack[-1])
        elif instruction == "pop":
            # pop the top item in stack
            stack.pop()
        else:
            # get the data in the "push" instruction
            data = int(instruction[5:])
            # push data to the top of stack
            stack.append(data)
    return stack

if __name__ == "__main__":
    program = [input() for _ in range(int(input()))]
    res = execute(program)
    print(" ".join(map(str, res)))