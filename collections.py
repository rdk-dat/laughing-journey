# Lists
servers = ["web1", "web2", "db1"]

# Tuples
ip_range = ("192.168.1.10", "192.168.1.50")

# Sets (remove duplicates)
open_ports = {22, 80, 443, 80}

# Dictionaries
process_info = {
    "nginx": "running",
    "mysql": "stopped",
    "ssh": "running"
}

print("Servers:", servers)
print("IP Range:", ip_range)
print("Unique Ports:", open_ports)
print("Process Info:", process_info)