#!/usr/bin/env python3
"""
AMITT.AI Mission Control Dashboard Server
Serves the dashboard at http://localhost:8765
"""

import http.server
import socketserver
import os
import webbrowser
from pathlib import Path

PORT = 8765
DIRECTORY = str(Path(__file__).parent.absolute())

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def log_message(self, format, *args):
        print(f"[DASHBOARD] {args[0]}")

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"""
╔═══════════════════════════════════════════════════╗
║                                                   ║
║   🤖 AMITT.AI Mission Control                     ║
║   Lead Generation Dashboard                       ║
║                                                   ║
║   📊 Dashboard: http://localhost:{PORT}            ║
║                                                   ║
║   Press Ctrl+C to stop                           ║
║                                                   ║
╚═══════════════════════════════════════════════════╝
    """)
    
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        webbrowser.open(f"http://localhost:{PORT}")
        print(f"Serving at http://localhost:{PORT}")
        httpd.serve_forever()
