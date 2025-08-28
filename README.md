This is SimPlan, a mobile based app that showcases a weekly task layout that automatically changes to the current week. 

The following tools were used: 
- KivyMD library in Python
- Kivy's markup langauge
- SQLite database
- Bash 

All the ".kv" files contains the class attributes specifications of each of the Kivy widgets implemented, which is unique to each widget utilized in each screen. 

The "main.py" is divided into roughly 3 parts: 
1. The first section has all screens of Simplan written in Kivy's markup language. This markup language ensures that the
2. The next section handles the database connection, and ties in each componenet of the UI with the database.
3. The last section uses a loop that generates the a "screen" according to the current week, and adds in the database extraction method that shows the tasks on the screen.
