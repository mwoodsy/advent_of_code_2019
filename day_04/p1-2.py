import time
start_time = time.time()

## Data Range from AoC
current = 236491
end = 713787


part1 = 0
part2 = 0
passwords = [] # store potential passwords from part 1, speeds up part two

## Part 1
## check each value to see if it meet part 1 criteria
while current < end:
    #convert to string, makes it easy to sort
    num = str(current)
    if num == ''.join(sorted(num)): # if sorted num == orig_num, then number is in increasing order
        for x in num:
            if num.count(x) > 1: 
                part1 += 1
                passwords.append(num)
                break
    current += 1    
## End of Part 1   

## Part 2
for num in passwords:
    for x in num:
        if num.count(x) == 2:
            part2 += 1
            break


print("Part 1:", part1)
print("Part 2:", part2)

print("--- %s seconds ---" % (time.time() - start_time))