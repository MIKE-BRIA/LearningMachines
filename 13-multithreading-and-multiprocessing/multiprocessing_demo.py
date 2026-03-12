'''
Multiple Processing allows you to run processes that run in parallel

REASONS TO USE MULTI PROCESSING
1. CPU - Bound Tasks (Tasks that are haevy on CPU usage(e.g mathematical computations, data processing))
2. Parallel execution - Where you use multiple cores of the CPU
'''

import multiprocessing
import time

def square_numbers():
    for i in range(5):
        time.sleep(1)
        print(f'Square: {i * i}')



def cube_number():
    for i in range(5):
        time.sleep(1.5)
        print(f'Cube: {i * i * i}')


if __name__=='__main__':

    ### create 2 Processes
    p1 = multiprocessing.Process(target=square_numbers)
    p2 = multiprocessing.Process(target=cube_number)
    t = time.time()

    ### Start the process
    p1.start()
    p2.start()

    ## Wait for the Process to complete
    p1.join()
    p2.join()


    finished_time = time.time()- t
    print(finished_time)
