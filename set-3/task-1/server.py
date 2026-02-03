import http.server
import socketserver

# Define the port you want to use
PORT = 8000

# SimpleHTTPRequestHandler serves files from the current directory
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Server started at http://localhost:{PORT}")
    print("Press Ctrl+C to stop the server.")
    # Keep the server running until you interrupt it
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
        httpd.server_close()