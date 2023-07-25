from multiprocessing import shared_memory, Process
import time 

shared_mem = shared_memory.SharedMemory(name='MyMemory', size=24, create=True)
buffer = shared_mem.buf
shared_mem.buf[:24] = b'Hello from child process'
# print( len(buffer) ) -> 24

input("Press any key to EXIT!")