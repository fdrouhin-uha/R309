import sys,threadDLimg, time,statistics 
import multiprocess, poolThread


def main():
    time_thread = []
    time_pool = []
    time_process = []
    x= int(input('nb de test: '))
    for i in range(x):

        start = time.perf_counter()
        multiprocess.main()
        end = time.perf_counter()
        print(f"Tasks ended in {round(end - start, 2)} second(s)")
        time_process.append(round(end - start, 2))

        start = time.perf_counter()
        threadDLimg.main()
        end = time.perf_counter()
        print(f"Tasks ended in {round(end - start, 2)} second(s)")
        time_thread.append(round(end - start, 2))

        start = time.perf_counter()
        poolThread.main()
        end = time.perf_counter()
        print(f"Tasks ended in {round(end - start, 2)} second(s)")
        time_pool.append(round(end - start, 2))

        print(f"temps moyen de la pool de thread {round(statistics.mean(time_pool),2)}s\n"
              f"temps moyen des thread {round(statistics.mean(time_thread),2)}s\n"
              f"temps moyen des processus {round(statistics.mean(time_process),2)}s")

if __name__=="__main__":
    sys.exit(main())