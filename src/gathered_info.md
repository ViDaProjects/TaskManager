# Information gathering system

## System CPU info

    cpu_runtime: full system cpu runtime in ms
    cpu_active_time: cpu active time (not in wait or idle)
    proc_count: process count (duhr)
    
    mem_total: All ram (duhr)
    mem_unused: Ram currently unallocated
    mem_available: Usable ram (includes what is reserved from processes)

    swap_total: all swap (duhr)

    swap_free: free swap (duhr)

    thread_count: thread count (duhr)

## Individual processes info

    PID (process id)

    name: name(duhr)

    prio_type: nice/rt

    prio: -20 - 19 for nice and 0 - 100 for rt (100 and -20 are the highest prios)

    proc_cpu_time: time process has spent running on the cpu

    EVERYTHING HERE IS IN KB(except percentages):
    virtual_size: Virtual memory allocated for process
    real_mem_share: Amount of memory actually allocated (including all shared spaces)
    real_mem_not_share: Amount of memory actually allocated (only one process contains a shared space)
    clean_shared_percent: Percent of shared memory that is clean
    clean_private_percent: Percent of private memory that is clean
    in_swap: Size of memory in swap

## Thread info (adjust to choose a process)
