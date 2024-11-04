import multiprocessing as mp
import numpy as np

def parallel_sum(data, output, idx):
    """Sum elements of the array and store in output list at index idx."""
    total = np.sum(data)
    output[idx] = total

def main():
    # Create a large array of random numbers
    data_size = 10**6
    num_processes = 4
    data = np.random.rand(data_size)
    
    # Divide the data into chunks for each subprocess
    chunk_size = data_size // num_processes
    processes = []
    manager = mp.Manager()
    output = manager.list([0]*num_processes)  # Shared list to store results from processes

    # Create and start processes
    for i in range(num_processes):
        start_index = i * chunk_size
        end_index = None if i+1 == num_processes else (i+1) * chunk_size
        process_data = data[start_index:end_index]
        p = mp.Process(target=parallel_sum, args=(process_data, output, i))
        processes.append(p)
        p.start()

    # Ensure all processes complete
    for p in processes:
        p.join()

    # Aggregate results
    total_sum = sum(output)
    print(f'Total sum of elements: {total_sum}')

if __name__ == '__main__':
    main()
