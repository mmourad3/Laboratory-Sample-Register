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

1) Save method:

Tool used: ChatGPT

Question asked: If write() only accepts strings then how can I write a dictionary in a json file?

Help received: ChatGPT explained that we can use 'json.dump()' or 'json.dumps()' since they can take dictionaries and other basic data types (but not objects of our own classes directly). It also explained the difference between them and how we use 'json.dump()' to write directly to the file, while 'json.dumps()' only converts the data into a JSON string. If we used 'json.dumps()' then we would have to use '.write()' after it. So using 'json.dump()' is simpler here. It also mentioned that we can use 'indent' with both functions to make our data more readable. 

Work done ourselves: I added the Save method to the SampleRegister class and added the Save option to the menu

2) Testing

Tool used: ChatGPT

Question asked: Writing everything for each test on seperate lines will make the file too long so is there a way to make it shorter while still being readable and if yes then how?

Help received: ChatGPT explained how to make a table in a .md file using | and - and gave me an example.

Work done ourselves: I used what I learned to set up the tables in the test record file