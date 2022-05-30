from time import sleep
from time import time
import psutil
from tqdm import tqdm

print("Enter one of the following numbers matching the corresponding function: \n"
            "1.Show CPU usage\n2.Show RAM usage\n3.Show Network usage\n4.Disks usage")

usrInpt = int(input("User input:"))


if usrInpt == 1:
         with tqdm(total=100, desc='cpu%') as cpubar:
            while True:
                cpu_thresh = 60
                if cpubar.n <= cpu_thresh:
                    cpubar.n = psutil.cpu_percent()
                    cpubar.refresh()
                    sleep(1)


if usrInpt == 2:
    with tqdm(total=100, desc='ram%', position=0) as rambar:  # gives the CPU bar but does not evaluate it.
        while True:
            ram_thresh = 75
            if rambar.n <= ram_thresh:
                rambar.n = psutil.virtual_memory().percent
                rambar.refresh()
                sleep(1)


if usrInpt == 3:
    def net_in(inf="eth0"):  # change the inf variable according to the interface
        net_in_ps = psutil.net_io_counters(pernic=True, nowrap=True)[inf]
        net_in_1 = net_in_ps.bytes_recv
        sleep(1)
        net_in_ps = psutil.net_io_counters(pernic=True, nowrap=True)[inf]
        net_in_2 = net_in_ps.bytes_recv
        net_in_result = net_in_2 - net_in_1
        net_in_result_mbps = net_in_result / 1024 / 1024
        print(net_in_result_mbps)
        net_in_thresh = 1.5
        if net_in_result_mbps <= net_in_thresh:
            print("Network in Speed:", net_in_result_mbps, "mbps")

    # with tqdm(total = 100, desc='net_out%') as netbar_out:


    def net_out(inf="eth0"):  # change the inf variable according to the interface
        net_out_ps = psutil.net_io_counters(pernic=True, nowrap=True)[inf]
        net_out_1 = net_out_ps.bytes_sent
        sleep(1)
        net_out_ps = psutil.net_io_counters(pernic=True, nowrap=True)[inf]
        net_out_2 = net_out_ps.bytes_sent
        net_out_result = net_out_2 - net_out_1
        net_out_result_mbps = net_out_result / 1024 / 1024
        print(net_out_result_mbps)
        net_out_thresh = 1.5
        if net_out_result_mbps <= net_out_thresh:
            print("Network out Speed:", net_out_result_mbps, "mbps")


    while True:
        net_in()
        net_out()

if usrInpt == 4:
    while True:
        diskUsage = psutil.disk_io_counters(perdisk = True)
        print(diskUsage)
        sleep(3)