I set this script up to run on some windows machines using task scheduler.
What it does is, ping the ip addresses listed in the ip address txt file and if any of them return a "not reachable" response an email is sent automatically to the people of your choosing. 
I also included host names for whatever you are testing in the text file CamName.txt that way its easy to dynamically change the names to whatever you are testing. 
Its important to keep in mind that the items listed in the ip address and cam name text files are being used as a parallel list so if you change one make sure to change the other.
When setting this up with task scheduler make sure you have it set to run the executable in the same location as where the text files are located and that you run the program as administator 
(make sure you check the box to run with highest priveleges) 
Feel free to let me know if you find any way I can improve this script. Enjoy!
