import subprocess

def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        raise ValueError("Tidak boleh bagi nol")
    return a / b

def run_command_safe(cmd):
    args = shlex.split(cmd) if isinstance(cmd, str) else cmd
    allowed = {'echo', 'ls', 'date'}
    if not args or args[0] not in allowed:
        raise ValueError("Perintah tidak diizinkan")

    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout.strip()
