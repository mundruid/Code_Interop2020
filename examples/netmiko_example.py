from netmiko import ConnectHandler, file_transfer


def connect_to_arista_eos(host, user, password):
    arista = {
        "device_type": "arista_eos",
        "host": host,
        "username": user,
        "password": password,
        "file_system": "/mnt/flash",
    }
    ssh_conn = ConnectHandler(**arista)

    return ssh_conn


def file_transfer_arista(conn, source_file, dest_file):

    transfer_dict = file_transfer(
        conn,
        source_file=source_file,
        dest_file=dest_file,
        file_system="/mnt/flash",
        direction="put",
        overwrite_file=True,
    )

    return transfer_dict
