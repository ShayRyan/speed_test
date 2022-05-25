import speedtest as st
from time import sleep

def report():
    pass

print(f'speedtest version {st.__version__}')

# get all speedtest servers in IE
s1 = st.Speedtest()
servers = s1.get_servers()
server_IDs = []

# dict of list of dict
for k in servers:
    for s in servers[k]:
        if s['cc'] == 'IE':
            server_IDs.append(int(s['id']))
print(f"Server IDs: {server_IDs}")

# test against each server
threads = 1
for sid in server_IDs:
    servers =[sid]
    s = st.Speedtest()
    s.get_servers(servers)
    s.get_best_server()
    s.download(threads=threads)
    s.upload(threads=threads)

    results_dict = s.results.dict()
    print(results_dict)
    print()
    print(f"Timestamp     : {results_dict['timestamp']}")
    print(f"Sponsor       : {results_dict['server']['sponsor']}")
    print(f"Server        : {results_dict['server']['url']}")
    print(f"My IP         : {results_dict['client']['ip']}")
    print(f"My ISP        : {results_dict['client']['isp']}")
    print(f"Download Speed: {(results_dict['download']/(1024 * 1024)):.2f} Mbps")
    print(f"Upload Speed  : {(results_dict['upload']/(1024 * 1024)):.2f} Mbps")
    print(f"Latency       : {results_dict['ping']:.2f} ms")

    print("***\n")
    sleep(3)