import time
start_time = time.time()

exec(open("p1.py").read())
exec(open("p2.py").read())

print("--- %s seconds ---" % (time.time() - start_time))