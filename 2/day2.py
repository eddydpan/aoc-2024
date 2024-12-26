import time

start = time.time()

# num_safe = 0

# with open("day2_input.txt", "r") as f:
#     for line in f:
#         lst = line.split(" ")
#         report = [int(x) for x in lst]

#         prev = report[0]
#         safe = True
#         direction = 0 # this is a counting variable
#         for i in range(1, len(report)):
#             cur = report[i]
#             if abs(cur - prev) > 3: # this is bad
#                 safe = False 
            
           
#             if cur > prev:
#                 direction += 1
#             elif cur < prev:
#                 direction -= 1
#             else: # must be the same, which is bad
#                 safe = False

            
#             prev = cur
#         if abs(direction) != len(report) - 1:
#             safe = False
#         if safe:
#             num_safe += 1
        
#     print(f"The total number of safe reports is: {num_safe}")
#     print(f"This code took a computation time of {time.time() - start} seconds")
######################################################

"""PART 2"""

num_safe = 0

with open("day2_input.txt", "r") as f:
    for line in f:
        lst = line.split(" ")
        report = [int(x) for x in lst]

        prev = report[0]
        safe = True
        direction = 0 # this is a counting variable
        damper = True

        for i in range(1, len(report)):
            cur = report[i]
            if abs(cur - prev) > 3: # this is bad
                safe = False 
            
           
            if cur > prev:
                direction += 1
            elif cur < prev:
                direction -= 1
            else: # must be the same, which is bad
                safe = False
            
            if abs(direction) != i - 1:
                safe = False
            
            if not safe and damper:
                report.pop(i)
                damper = False
            prev = cur
        
        if safe:
            num_safe += 1
        
    print(f"The total number of safe reports is: {num_safe}")
    print(f"This code took a computation time of {time.time() - start} seconds")

