def current_beats():
    nums = (1,2,3,4)
    i = 0
    while True:
        if i >= len(nums): i = 0
        yield nums[i]
        i += 1 


i =1
counter = current_beats()
while i < 20:
    if(next(counter) <= 2):
        print(f"{i} Beat")
    i += 1