### Team ACCQT: Trivia Generation Application

##### OBJECTIVES
Collaborative Effort to Create a Trivia Generation Application

Develop a trivia application in Python that:
• Displays local trivia questions and their answers
• Offers trivia questions to other teams through a Flask API and ngrok
• Employs object-oriented programming to manage inquiries
• Allows trivia and questions to be added either locally or through the API
• Implements Git and makes use of GitHub features
• Contains suitable documentation in the README.md file

### The Trivia Generator Application
##### Summary
This application employs object-oriented design to generate and display trivia questions. Besides functioning locally within the console, it can deliver random trivia through a Flask API, which can be made publicly accessible online using ngrok for other teams to utilize.

##### Procedure
 Initially, we used *random* *module* to develop a program.
 The Quote and QuoteManager classes were then developed.
 The Quote class returns a legible **JSON** format after separating the text and author for appropriate labeling.
 Conversely, the QuoteManager gathers quotes and provides a **random quote**.
 This allows the software to run **locally** using console/terminal.
 The application was then transformed into a **API** that could execute over a link using **ngrok** and **FlaskAPI**.
 A random quote in a **JSON** format can be obtained by utilizing the obtained link.  A other software can also utilize this site to obtain a random quote.
  
##### Instructions for Installation and Usage
Install our application and use Vscode to run it.
Run **Api.py / API File** and **https://carapaced-deidre-saleable.ngrok-free.dev/trivia** on separate terminals after opening a terminal.

