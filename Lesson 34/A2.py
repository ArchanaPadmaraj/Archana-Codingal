i = 1
while (i<=10):
    print(f"counter is at {i}")
    i +=1


count = 1
while True:
    print("the value of count is",count)
    if count ==10:
        break
    count +=1


while True:
    ans = input("enter q to stop")
    if ans.lower() == ("q"):
        print("exiting loop")
        break
    else:
        print("You have entered something else")
