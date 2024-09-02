**Description:**


This project is in Python and Tkinter. TKinter provides the GUI. The GUI consists of a label, and an Entry called entryField.
The entryfield Entry is bound to key presses by the bind function. The bind function takes as input, '<Key>', and a lambda
function. The lambda function is defined such that when text is entered into the entryField by key presses, and after 20000ms 
have elapsed, the clearText() function is called.In the clearText() function, the delete function removes the text entered in 
the entryField.
On the other hand, if the argument to the bind function is '<Return>', upon pressing the 'Enter' key, the text in the entryField
Entry is deleted.


**Requirements:**


TKinter
