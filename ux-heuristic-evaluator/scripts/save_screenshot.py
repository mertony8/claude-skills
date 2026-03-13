"""
Screenshot saver utility for the UX Heuristic Evaluator skill.

Usage from bash:
  echo "<base64_data>" | python save_screenshot.py <output_path>

Or from Python:
  python save_screenshot.py <output_path> <base64_data>

The base64 data should NOT include the data URL prefix (data:image/jpeg;base64,).
"""

import sys
import base64
import os

def save_base64_image(b64_data, output_path):
    """Save base64-encoded image data to a file."""
    os.makedirs(os.path.dirname(output_path) or '.', exist_ok=True)
    
    # Remove data URL prefix if present
    if ',' in b64_data:
        b64_data = b64_data.split(',', 1)[1]
    
    # Remove whitespace/newlines
    b64_data = b64_data.strip().replace('\n', '').replace('\r', '')
    
    with open(output_path, 'wb') as f:
        f.write(base64.b64decode(b64_data))
    
    size = os.path.getsize(output_path)
    print(f"Saved: {output_path} ({size} bytes)")
    return output_path

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python save_screenshot.py <output_path> [base64_data]")
        print("       echo '<base64>' | python save_screenshot.py <output_path>")
        sys.exit(1)
    
    output_path = sys.argv[1]
    
    if len(sys.argv) >= 3:
        b64_data = sys.argv[2]
    else:
        b64_data = sys.stdin.read()
    
    save_base64_image(b64_data, output_path)
