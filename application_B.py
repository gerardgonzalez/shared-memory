from multiprocessing import shared_memory

shared_mem = shared_memory.SharedMemory('MyMemory')

data = bytes(shared_mem.buf[:24]).decode()
print(data)

shared_mem.close()
shared_mem.unlink()