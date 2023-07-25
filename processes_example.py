from multiprocessing import shared_memory, Process

def task(shared_mem):
    shared_mem.buf[:24] = b'Hello from child process'

if __name__ == '__main__':
    shared_mem = shared_memory.SharedMemory(name='MyMemory', size=1024, create=True)
    process = Process(target=task, args=(shared_mem,))
    # start the child process
    process.start()
    # wait for the child process to finish
    process.join()
    # report the shared memory
    data = bytes(shared_mem.buf[:24]).decode()
    print(data)
    # close the shared memory
    shared_mem.close()
    # release the shared memory
    shared_mem.unlink()