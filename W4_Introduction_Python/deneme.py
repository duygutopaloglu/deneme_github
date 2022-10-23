def success():
    print("Define your dedication level (0-100)")
    dedication = int(input())  # dedicate yourself
    print("Define your persistence level (0-100)")
    persistence = int(input())  # be persistence
    print("Do you have passion to achive this goal Please input True or False")
    passion = bool(input())  # have passion True or False
    if passion == True:
        a = dedication * 0.5 + persistence * 0.5
        magic = "Your speed is %s please keep try until you get your goals" % a
        return magic
    else:
        magic = "Success could not happen if there is no passion. Motivate yourself !"
        return magic


duygu = success()

a = bool(input())

b = a


#