# Goalify
  This is my CS50W Final Project, where I created a webpage/application that gives users an opportunities to journal their thoughts/ideas while not wasting any paper and an option to capture and see their goals.

  Distinctiveness and Complexity

  For this particular project I decided to test myself with the use of Javascript. I believe throughout my coding experience and various bootcamps, Javascript has always been the one language that was tricky since it was so unorthodox and different from the others. 
In this particular project I incorporated things involving the language such as a color panel. When the user creates a journal, they have a decision to pick the color that they want their journal to be and how it will be displayed on their page. This was made mostly by javascript as once the user clicks on a block (which is an image) that displays a color, the preview journal changes as well without needing to submit a form. The preview will constantly change asynchronously while the color blocks are being selected. Not only this, the color block that was clicked will appear with a dark outline to show which block the user selected and this was made possible from javascript as well. 
  Another feature that made this project distinctive and complex was the timer feature. One of the columns in the goal tracker form was a “timer”, once the icon for the timer was clicked the user will be led to a page with the amount of time the goal will take, the name of the goal, and a timer along with a start button. Once the user clicks the start button the time will start counting down until the user completes the goal. If the user needs to take a break they can click a pause button and once they are ready they can click resume. This was very difficult to learn and was much different than what I was accustomed to as cs50w has never given a project that incorporates a countdown clock. I believe that these two features alone make this overall project distinct and more complex than the previous ones and they were both focal points in the creation of this project. 

Breakdown of Files
	
  For the index file, it is the file that includes everything and is serving as the nerve center for the project. It includes a greeting to the user that logged in, the ability to create a journal by choosing its color and name, the journals that were previously created, and the goal tracker table that shows the goals that were entered and the progress of their completion. 
  The history file shows the goals that were already completed. This is like the goal tracker table on the index page but just shows the goal name, time, and frequency of the goal. This page can be accessed by clicking the clock icon in the navbar or when a user completes a goal.
  The entries file displays content that the user wrote in a particular journal. When a journal name is clicked on the home page it is lead to the contents of this file. The user has the ability to write content in the journal that they clicked via the form that is shown at the top. Once the entry is submitted the latest entry will display right under the form and the older entries will be on separate pages. A page will display one entry at a time and an entry consists of the date and time that it was written along with the user that wrote it. 
  Layout file consists of what was used to style the page mainly and the navbar. The sources that were used to style the page include bootstrap and fontawesome. The navbar consists of icons including the home, clock, Goalify logo, and the logout icon.
  Login file is composed of a form that allows the user to enter their username and password. If the person that is on the page is a first time user, there is a link at the bottom of the form that leads the user to the register page. 
  The register page is similarly created as it also has a form but with more fields such as an email address and a confirm password field. If the user already has an account there is a link at the bottom of this form that leads the user to the login page.
  Finally, for the timer file it displays the name of the goal that was clicked. This is followed by the amount of time that was entered by the user for that specific goal and under that is a start button. Once the start button is clicked by the user, the timer begins and the clock runs down until it reaches zero. If the user wants a break from the goal, they have an option to click the pause button. Once the user is ready to start the goal again they click the resume button. 

How to Run Application 
	
  This application is run using the latest version of python and Django. In my personal experience I used VScode and typed in “python3 manage.py runserver” to activate the application and to use it. 


