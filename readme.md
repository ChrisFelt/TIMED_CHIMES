Program that plays custom sounds based on user defined timers. 
Includes a play/pause button, a reset button, and a timer field that can be clicked on and modified by the user to change the time. 

Also includes a settings button that opens a separate window with settings and sounds options.
Settings: modify behaviors
Sounds: import new and manage current sounds

Playing audio files with python:
- https://stackoverflow.com/questions/74083314/playing-sound-using-python
- Options: pydub or pygame

Includes Tibetan singing bowl and Buddhist temple gong sounds. 
- Downloaded royalty-free samples from: https://pixabay.com/sound-effects/search/tibetan-bowl/
- See license summary: https://pixabay.com/service/license-summary/

Icon source:
<a href="https://www.flaticon.com/free-icons/ui" title="ui icons">Ui icons created by KP Arts - Flaticon</a>


Stretch goals:

Create Time class to handle timers longer than 24 hours - QTime maxes out at 23h 59m 59s
Additionally requires replacement of QTimeEdit widget with a widget that can handle times >= 24h.

Sound can be played for custom length of time, once, or on a loop. 

Controls can be bound to keys on the keyboard for quick access. 

Timers can be automated (starts and stops at a user defined time) or chained together.

Include process killing capability? Automatically kills user defined processes (using command line) if they start up. Can be chained to timers or on its own separate timer.

Add smaller secondary lcd screen for seconds portion of timer
