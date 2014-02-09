Rocket Launcher
--------------

Created this script during the FirstFridayHackathon.  It is used to control the DreamCheeky USB rocket launcher.

Run this command to see the rocket in action! 
```
rocket.demo()
```

#Mac OS X Mavericks Setup#
*make sure you have a working homebrew and pip setup first*

Install a usb backend
```
brew install libusb
```

Install a older version of pyusb that works on Mavericks.
```
pip install --pre pyusb
```

#Hackathon#
Most of my time at the hackathon was spent eating delicious pasta and getting my environment to work on 
Mac OS X Mavericks.  During the hackathon I said "screw it" and just booted
into Ubuntu where I had a working dev environment.  

**Pro Tip:** make sure your
dev environment works *before* the hackathon.

This weekend I decided to get it working on my Mac natively.  I use Homebrew and 
pip for development and all that crap was messed up (The mavericks upgrade destroyed site packages).
 It came down to uninstalling
 homebrews packages, homebrew, pip packages, pip, and then reinstalling.  Once 
 that was complete things were back to normal.
 