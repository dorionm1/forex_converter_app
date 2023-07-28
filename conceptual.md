### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?
  
  **Python**: Object Oriented programming langage. Mainly used in server side scripting. Indentation plays a huge part ot how the code is rin. 

  **JavaScript**: Scripting Language. Mainly used for client side scripting. Uses block scoped variables.

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.

  1.) You could use **.get(keyname, value)**. If the Specified key does not exist then the value would be returned.. Default being "None."

  2.) You could use **.setdefault(keyname, value)**. This behaves similarly to .get. 

- What is a unit test?
  
  Unit tests are written by developers to make sure existing fuctionality does not break as they push code. Developers are constantly pushing code to applications. Having unit tests can be very beneficial in that if one of their tests fail, they know they could have caused a regressed issue. 

- What is an integration test?
  
  Intigration testing happens after unit testing and it tests the application/software as a whole instead of indivitual units as unit testing focuses on. 

- What is the role of web application framework, like Flask?

  Most if not all web applications allow for users to be able to navigate to different areas of a site semmlessly. This is made possible by web app frameworks like Flask, Django, etc. 

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?

  I would use the first meathod for a specific web page of an application that might be a page dedicated to pretzels. I would use the second URL query param in the scenario where we may be querying pretselz whether it be a "Pretzels" search, or filter on a site. 

- How do you collect data from a URL placeholder parameter using Flask?

  To do this, you would want to add "<name>" placeholders in the URL and accepting corresponding name arguments in the view function.

- How do you collect data from the query string using Flask?

  You would do this by using request.args and assigning that valu to a variable. After doing so, you can use that variable as needed. 

- How do you collect data from the body of the request using Flask?



- What is a cookie and what kinds of things are they commonly used for?

  Cookies are pieces of code/information saved by websites onto the user's web browser when a session is initiated. The most important ones are session management, user personalization, and tracking.

- What is the session object in Flask?

  A session object is used to track the session data which is a dictionary object that contains a key-value pair of the session variables and their associated values.

- What does Flask's `jsonify()` do?

  It returns a response object in JSON form. 