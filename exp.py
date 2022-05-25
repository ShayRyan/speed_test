import speedtest as st

test = st.Speedtest()

servers = test.get_servers()

# dict of list of dict
for k in servers:
    for s in servers[k]:
        # list servers in IE
        if s['cc'] == 'IE':
            print(f"{s['name']} : {s['sponsor']} : {s['id']} : {s['host']}")