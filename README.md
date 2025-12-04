# PyPortScanner

😁 A typical port scanner but a huge deal for me personally as my first ever cybersecurity project ! This fast and multi-threaded port scanner detects open ports and grabs service banners with the results being automatically saved in another folder for easy-viewing.   


📃 Table of Contents

    🚀 Features  
  
    💻 Installations  
  
    👤 Usage  
  
    🗃️ Result storing   
  
    🕸️ Project Structure  
  
    🛠 Technologies used   
  
    ⚠️ Disclaimer   
  

🚀 Features  

  
    🔍 Scans any host (IP or domain)   
    
    🏃‍♀️‍➡️ Multi-threaded scanning for high speed  
    
    🏷️ Banner grabbing (HTTP banners, service identification)  
    
    🎨 Colored terminal output (using Colorama)  
    
    📁 Auto-created scan_results/ folder  
    
    💾 Saves scan results as:  
        scan_results/port_scan_results_<host>.txt  


💻 Installations
  
   
   1. Clone or download this project  

      git clone https://github.com/pixel-sneha/PyPortScaner.git
      cd PyPortScanner


   3. Install required modules   

      pip install -r requirements.txt
         

👤 Usage    


  Basic scan:   
  python scanner.py 1 1024 --host 127.0.0.1   

  Parameters:    
  
  | Flag | Description |
  | :------- | :------: |
  | --host or -t  | Target host (IP or domain)  | 
  | end_port  | Ending port number  |
  | --threads or -n  | Number of threads (default: 100)  |

  
  Example scans  

  Scan localhost from port 1 to 65535  
  
    use: python scanner.py 1 65535 -t 127.0.0.1
  
  Scan Google (ports 20–200)   
  
    use: python scanner.py 20 200 --host google.com



🗃️ Result Storing   

  
  Every scan creates a file:   

  scan_results/port_scan_results_<host>.txt   


  Each file includes:   

  1. Target 
  2. Timestamp 
  3. List of open ports 
  4. Banners (if available)



🕸️ Project Structure  

    
    ├── scanner.py  
    ├── requirements.txt   
    ├── README.md  
    └── scan_results/   


🛠 Technologies Used  

  
    Python 3.14.0
  
    Sockets
    
    Threads
    
    Colorama

  
⚠️ Disclaimer

  This tool is for educational and cybersecurity learning purposes only.
  Do NOT scan systems you do not own or have permission to test.
  

  
  




