<<<<<<< HEAD
### Team ACCQT: App for Trivia Generation

 ##### GOALS
 Trivia Generator App as a Team Activity

 Make a trivia app in Python that:
 • Shows local trivia questions and answers
 • Provides trivia questions to other teams via the Flask API and ngrok
 • Utilize object-oriented programming to handle inquiries
 • Trivia and questions can be added locally or using the API.
 • Git and Utlizie Github features
 • Appropriate READMe.md Documentation


 ### The Trivia Generator App
 ##### Overview
 This application uses object-oriented design to create and present trivia questions.  In addition to running locally in the console, it may provide random trivia using a Flask API that can be made public online via ngrok so that other teams can use it.

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
Run **Api.py / API File** and **ngrok http 500** on separate terminals after opening a terminal.

