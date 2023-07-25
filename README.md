# SHARED MEMORY WITH PYTHON

If you want to share information between different applications, one of the most efficient ways to do so is by using shared memory.

In Python, you can store data in shared memory using the multiprocessing library.

## Application A:

```python
from multiprocessing import shared_memory

shared_mem = shared_memory.SharedMemory(name='MyMemory', size=1024, create=True)
buffer = shared_mem.buf
shared_mem.buf[:24] = b'Hello from child process'
input("Press any key to close Aplicacion 1...")
```

In the above example, we are creating a shared memory space with a size of 1024 bytes called '*MyMemory*'.
Then, we assign the string 'Hello from child process' to the first 24 bytes, adding 'b' in front to encode the string to bytes.

This way, we can read that information from an Application B:

## Application B:

```python
from multiprocessing import shared_memory

shared_mem = shared_memory.SharedMemory('MyMemory')
data = bytes(shared_mem.buf[:24]).decode()
print(data)
```

You could also do it within the same application, using separate processes.

In the function **task(*shared_mem*)**, we store our string in the shared memory through a child process.
Later, in the main thread, we can read the string stored in the shared memory.

The example would look something like this:

```python
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
```

Note that, to close the shared_mem instance, we are using:

```python
shared_mem.close()
```

Additionally, to ensure proper cleanup of resources, you should release the shared memory using the unlink method:

```python
shared_mem.unlink()
```

# Take into consideration

You should be aware that when *Application A* terminates, the shared memory will be automatically released and no longer accessible for *Application B*. If you try to access it, it will result in an error.

If you want to keep the shared memory persistently even after the application has finished, you will need to explore other alternatives, depending on your operating system.

One possible alternative could be using file-based shared memory mapped (mmap), which is a form of persistent shared memory that may offer better performance in certain cases.

**I recommend you to further investigate this topic!**
