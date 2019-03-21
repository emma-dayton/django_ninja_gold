# Ninja Gold with Django

Here you will find my Coding Dojo assignment to make a simple game app using
Django. The game uses psuedo random numbers from the random module to assign
variable scores to each of the form buttons, and tracks the score, number of attempts,
and an activity log across the session.

Routes:
* / -- home page is the only rendered page, with material conditional depending on game status
* /process_money -- runs the game logic, using session data and request forms, redirects to home
* /reset -- clears session data, redirects to home
