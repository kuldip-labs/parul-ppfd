## Building a simple web server 
* in Python is surprisingly straightforward. While you could use a heavy-duty framework like Django or Flask, Python has a built-in module called http.server that is perfect for serving static files without any external dependencies.
#### How to Run It
* Open your terminal or command prompt.

* Navigate to the directory containing both files.

* Run the script: python server.py.

* Open your web browser and go to http://localhost:8000.

#### If you just want to serve a folder quickly without writing a .py script, you can run this command directly in your terminal:
`python -m http.server 8000`

+ This triggers the same built-in logic and immediately serves every file in your current directory.