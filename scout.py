import subprocess

def run_recon(target):
    print(f"[*] SCOUT: Scanning {target}...")
    # -sV finds versions, -T4 makes it fast
    try:
        result = subprocess.run(['nmap', '-sV', '-T4', target], capture_output=True, text=True)
        if result.returncode == 0:
            return result.stdout
        else:
            return "Scan failed. Check if Nmap is installed."
    except Exception as e:
        return f"Error: {str(e)}"
