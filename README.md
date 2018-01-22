## Family Friday

Family Friday is a web app for divvying your colleagues into small groups suitably sized for enjoying an afternoon meal together. Enter your teammates' names into the database and continue using it as your team grows. Teammates are assigned to groups randomly to facilitate new connections and variety, and groups always include no fewer than three teammates and no more than five. No one gets left out, but no group is so large that they would have trouble finding a table in a crowded lunch room or getting seated at a busy restaurant.

#### Built with...

* Python 2.7
* Flask
* PostgreSQL
* Flask SQLAlchemy
* JavaScript
* jQuery
* Bootstrap

#### Installation

To run Family Friday locally, clone the repository. Then, I recommend creating a virtual environment and using pip to install the dependencies. Also, you'll need to create a "SECRET_KEY" environment variable. It can be any string, but is preferably randomly generated and cryptographically strong. If you'll be using this tool regularly, it's best to go ahead and store this in a secrets.sh file. 

First, navigate to the directory with the copied files and create a secrets.sh file. Then, copy the below text into the file, replacing the X's with the string of your choosing:

```
export SECRET_KEY="XXXXXXXXXXXXXXXXXXXXX"
```

Then, create and activate a virtual environment:
```
virtualenv env
```
```
source env/bin/activate
```
Then you can install the dependencies using pip and export your environment variable:

```
pip install -r requirements.txt
```
```
source secrets.sh
```
Next, if you haven't already, install PostgreSQL. You'll need to create a database called "staff\_directory". In a shell, enter: 
```
createdb staff_directory
```
Finally, build the schema from the model file:
```
python -i model.py
```
```
staff_directory = db.create_all()
```
At this point, you should be ready to run the server and start adding your teammates and sorting them into groups!
```
python server.py
```
To run tests, use this command:
```
python tests.py
```

Enjoy dining in good company!