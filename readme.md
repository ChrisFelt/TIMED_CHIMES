<h4>Welcome to the Timed Chimes GitHub repository!</h4>

---
<br>

Timed Chimes is a simple Windows desktop timer that plays user specified alert sounds on a custom timer.


It is intended to help improve long-term health and productivity by giving the user an audio cue to stand up, move around, or stretch at regular time intervals.


This app is currently under construction. At present, the all buttons on the timer display window and timer functionality are working. The settings window and sounds functionality are in currently a work in progress.


Stay tuned for the User Guide when basic functionality is complete.
<br><br>

---
<br>
Button icon source:
<a href="https://www.flaticon.com/free-icons/ui" title="ui icons">Ui icons created by KP Arts - Flaticon</a>
<br><br>

---
<br>


Current stretch goals:

1. Create Time class to handle timers longer than 24 hours - QTime maxes out at 23h 59m 59s.
Additionally requires replacement of QTimeEdit widget with a widget that can handle times >= 24h.

2. Add smaller secondary lcd screen for seconds portion of timer.

3. Timers can be automated (starts and stops at a user defined time) or chained together.

4. Sound can be played for custom length of time, once, or on a loop. 

5. Controls can be bound to keys on the keyboard for quick access. 

6. Add dark mode.

7. Add visual cue when alarm goes off.

8. Include process killing capability. Automatically kills user defined processes (using command line) if they start up. Can be chained to timers or on its own separate timer.

