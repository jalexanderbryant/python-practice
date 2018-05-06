from time import time
start_time = time()
for i in range(0, 10):
	print(i)
end_time = time()
elapsed = end_time - start_time

print(elapsed)
