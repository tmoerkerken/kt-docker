# %%
import socket

def connect_to_server(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        data = s.recv(1024)
        return data.decode()

# %% Connect to Server 1
server1_data = connect_to_server('localhost', 5000)
print("Received from Server 1:", server1_data)

# %% Connect to Server 2
server2_data = connect_to_server('localhost', 6000)
print("Received from Server 2:", server2_data)
# %%
