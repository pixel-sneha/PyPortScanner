import argparse
import socket
from queue import Queue
from colorama import init, Fore
from threading import Thread, Lock
from datetime import datetime

init()
GREEN = Fore.GREEN
RESET = Fore.RESET
GRAY = Fore.LIGHTBLACK_EX
q = Queue()
print_lock = Lock()
TARGET_HOST = None
open_ports = []

def grab_banner(s,port):
    try:
        if port in(80,443,8080):
            s.sendall(b"HEAD / HTTP/1.0\r\n\r\n")
        banner = s.recv(1024)
        return banner.decode(errors="ignore").strip()
    except Exception as e:
        return f"Error grabbing banner: {e}"
    
def worker():
    while not q.empty():
        port = q.get()
        scan_port_with_banner(TARGET_HOST,port)
        q.task_done()

def run_threads(start_port,end_port):
    for port in range(start_port,end_port+1):
        q.put(port)
    for i in range(N_THREADS):
        t = Thread(target=worker)
        t.daemon = True
        t.start()
    q.join()

def scan_port_with_banner(host,port):
    try:
        s = socket.socket()
        s.settimeout(1)
        result = s.connect_ex((host,port))
        
        if result == 0:
            banner = grab_banner(s,port)
            
            with print_lock:
                print(f"{GREEN}[+] Port {port} is open{RESET}")
                print(f"{GREEN}  Banner: {banner}{RESET}")
                open_ports.append((port,banner))
        else:
            with print_lock:
                print(f"{GRAY} Port {port} is closed{RESET}")
    except:
        pass
    finally:
        s.close()

def save_results_to_file():
    folder = "scan_results"
    filename = f"port_scan_results_{TARGET_HOST}.txt"
    filepath = f"{folder}/{filename}"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(filepath,"w") as f:
        f.write(f"Port Scan Results for {TARGET_HOST}\n")
        f.write(f"Scan Time: {timestamp}\n\n")
        f.write("Open Ports:\n")
        if open_ports:
            for port,banner in open_ports:
                f.write(f"Port {port}: {banner}\n")
        else:
            f.write("No open ports found.\n")
    return filepath


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Port Scanner with Banner Grabbing")
    parser.add_argument("--host","-t",help="Host to scan",default="127.0.0.1")
    parser.add_argument("start_port",type=int,nargs='?',default=1,help="Starting port number")
    parser.add_argument("end_port",type=int,nargs='?',default=1024,help="Ending port number") 
    parser.add_argument("--threads","-n", dest="n_threads", type=int,default=100,help="Number of threads to use, default is 100")
    args = parser.parse_args()
    

    if not(1<=args.start_port<=65535) or not(1<=args.end_port<=65535):
        parser.error("Port number must be between 1 and 65535")
    if args.start_port>args.end_port:
        parser.error("Starting port number must be less than or equal to ending port number")
    
    TARGET_HOST = args.host 
    total_ports = args.end_port - args.start_port + 1
    N_THREADS = max(1, min(args.n_threads,total_ports))
    ip = socket.gethostbyname(TARGET_HOST)
    print("Port Scanner using Banner Grabbing")
    print(f"Scanning host: {TARGET_HOST} ({ip})")
    print(f"Scanning ports from {args.start_port} to {args.end_port} using {args.n_threads} threads\n")
    
    try:
        run_threads(args.start_port,args.end_port)
        result_file = save_results_to_file()
        print(f"\n Scanning completed. Results saved to {result_file}")
    except Exception as KeyboardInterrupt:
        print("\nScan interrupted. Exiting program.") 
