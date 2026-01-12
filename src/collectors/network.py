import socket
import urllib.request

def get_network_info(check_public=False):
    """Gets local and optional public IP."""
    local_ip = "Unknown"
    try:
        # Connect into a dummy address to find the interface used for routing
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
    except Exception:
        pass

    public_ip = None
    if check_public:
        try:
            public_ip = urllib.request.urlopen('https://api.ipify.org', timeout=3).read().decode('utf8')
        except:
            public_ip = "Timeout/Error"
            
    return {"local_ip": local_ip, "public_ip": public_ip}

def get_speedtest():
    """Runs a basic internet speed test."""
    try:
        import speedtest
        st = speedtest.Speedtest()
        st.get_best_server()
        ping = st.results.ping
        download_mbs = st.download() / (1024**2)
        return {"ping": f"{ping:.0f} ms", "download": f"{download_mbs:.1f} Mbps"}
    except Exception as e:
        return {"ping": "Error", "download": "Error"}
