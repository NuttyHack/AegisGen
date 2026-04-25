from google import genai
import os
from dotenv import load_dotenv

# Load your API key from .env
load_dotenv()

# Setup the new 2026 Client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def analyze_with_ai(scan_data):
    print("[*] BRAIN: Analyzing data with the 2026 Gemini 3 Engine...")
    
    prompt = f"""
    You are a Senior Penetration Tester. Analyze this Nmap scan:
    {scan_data}
    
    Provide:
    1. TOP 2 CRITICAL VULNERABILITIES.
    2. EXACT KALI COMMANDS TO TEST THEM.
    3. PROFESSIONAL REMEDIATION STEPS.
    """
    
    try:
        # The new 2026 syntax
        response = client.models.generate_content(
            model='gemini-2.5-flash', # Using the current stable 2026 workhorse
            contents=prompt
        )
        return response.text
    except Exception as e:
        return f"Brain Error: {str(e)}"
