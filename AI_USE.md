Yasser Assi

1) __pycache__ and .gitignore (Feature 1)

Tool used: ChatGPT

Question asked: What is the '__pycache__' folder, should we exclude it from GitHub, and how can we do that?

Help received: ChatGPT explained that Python creates this folder automatically and that we don't need to upload it since Python can recreate it. It also showed how to exclude it using .gitignore.

Work done ourselves: Added .gitignore to exclude __pycache__/ and *.pyc files.

2) Loading JSON Files (Feature 1)

Question asked: How can I read saved data from a JSON file and convert it back into Sample objects?

Help received: ChatGPT explained how to use 'json.loads()' to convert JSON text into a Python dictionary, then use the saved attributes to recreate the Sample objects. ChatGpt also provided an example of how to do this.

Work done ourselves: I chose to use 'try' and 'except FileNotFoundError' since we learned them (in the "files" lecture you gave us). The "with open" was also done by me, although it wasn't explained in class but after the "files" lecture I reviewed it with chat gpt which in turn taught me this method which automatically closes the file after using it


Melissa Mourad

I did not use AI tools