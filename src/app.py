import subprocess
import shlex

def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        raise ValueError("Tidak boleh bagi nol")
    return a / b

def run_command_safe(cmd):
    #Pastikan cmd jadi list yang aman
    if isinstance(cmd, str):
        args = shlex.split(cmd)
    else:
        args = cmd  # diasumsikan list jika bukan str

    #Perintah yang diizinkan (whitelist)
    allowed_bins = {'echo', 'ls', 'date'}
    if args and args[0] not in allowed_bins:
        raise ValueError("Perintah tidak diizinkan")

    #Jalankan command dengan aman (tanpa shell)
    result = subprocess.run(args, capture_output=True, text=True, shell=False)
    return result.stdout.strip()
