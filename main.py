from scout import run_recon
from brain import analyze_with_ai
import sys

def start_aegis():
    print("\n" + "="*40)
    print("   AEGIS-GEN v1.2 [2026 EDITION]   ")
    print("="*40)
    
    target = input("[?] Enter Target (e.g., scanme.nmap.org): ")
    if not target:
        print("[!] No target entered. Exiting.")
        sys.exit()

    # Step 1: Recon
    raw_data = run_recon(target)
    
    # Step 2: AI Analysis
    print("[*] Contacting the AI Hivemind...")
    final_report = analyze_with_ai(raw_data)
    
    print("\n" + "!"*40)
    print("      STRATEGIC ATTACK PLAN")
    print("!"*40)
    print(final_report)
    print("\n" + "="*40)

if __name__ == "__main__":
    start_aegis()
