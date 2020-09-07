from netmiko import ConnectHandler, NetmikoTimeoutException


def connect_to_arista(device_type, host, username, password):
    arista = {
        "device_type": "arista_eos",
        "host": host,
        "username": username,
        "password": password,
    }

    try:
        ssh_conn = ConnectHandler(**arista)
        return ssh_conn
    except NetmikoTimeoutException:
        return None


if __name__ == "__main__":
    pass
