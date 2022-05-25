import speedtest as st

print(f'speedtest version {st.__version__}')

test = st.Speedtest()

print("loading server list...")
test.get_servers()

print("Choosing best server...")
best = test.get_best_server()

print(best)
print(f"Found best server. Host: {best['host']}")

print("Performing download test...")
download_result = test.download()
print("Performing upload test...")
upload_result = test.upload()
print("Performing latency test...")
ping_result = test.results.ping

print(f"Download Speed: {(download_result/(1024 * 1024)):.2f} Mbps")
print(f"Upload Speed  : {(upload_result/(1024 * 1024)):.2f} Mbps")
print(f"Latency       : {ping_result:.2f} ms")

