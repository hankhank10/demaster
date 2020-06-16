# demaster music tracks from streaming services

Is it just me that finds those pointless "(Remastered 2015)" additions that you get on music track names incredibly annoying? You're trying to see the track name and it's endlessly scrolling pointless information.

Like, hey dude, I'm just trying to listen to Hey Jude, I don't really care that you put it into stereo in 2011.

Don't even get me started on Simon & Garfunkel's classic "The 59th Street Bridge Song (Feelin’ Groovy) - Live at Southern Illinois University Carbondale, IL - November 1969" which is a genuine track name on Spotify.

So I wrote a script to fix it, which I'm calling demaster. It looks for the nonsense at the end of a song name and strips it right out.

## Installation

No installations or libraries should be required. Runs on Python3.

demaster.py is the script which you can incorporate into your projects.

example.py is an example of how to call it and what it does using a looping command line