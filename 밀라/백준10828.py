import sys
input = sys.stdin.read

def main():
    data = input().strip().split('\n')
    N = int(data[0])
    commands = data[1:]

    stack = []
    results = []
    
    for command in commands:
        if command.startswith("push"):
            _, x = command.split()
            stack.append(int(x))
        elif command == "pop":
            if stack:
                results.append(stack.pop())
            else:
                results.append(-1)
        elif command == "size":
            results.append(len(stack))
        elif command == "empty":
            results.append(1 if not stack else 0)
        elif command == "top":
            if stack:
                results.append(stack[-1])
            else:
                results.append(-1)

    # Print all results
    sys.stdout.write("\n".join(map(str, results)) + "\n")

if __name__ == "__main__":
    main()
