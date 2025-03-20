import sys

# Make sure the output uses UTF-8 encoding
sys.stdout.reconfigure(encoding='utf-8')

# Force Python to print immediately (sometimes GitHub Actions buffers output)
print("✅ GitHub Actions is executing this Python script successfully!", flush=True)
