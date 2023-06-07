if __name__ == '__main__':
    N = int(input())
    list_ = []
    
    for i in range(N):
        command, *args = input().split()
        
        if command == 'insert':
            index = int(args[0])
            element = int(args[1])
            list_.insert(index, element)
        elif command == 'print':
            print(list_)
        elif command == 'remove':
            element = int(args[0])
            list_.remove(element)
        elif command == 'append':
            element = int(args[0])
            list_.append(element)
        elif command == 'sort':
            list_.sort()
        elif command == 'pop':
            list_.pop()
        elif command == 'reverse':
            list_.reverse()
