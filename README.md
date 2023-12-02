<h1 align="center"> FlyCapture </h1>



***How to use the flycapture camera and install it.***

Recommended:
```
sudo apt update
```
```
 sudo apt install libraw1394-11 libgtkmm-2.4-dev libglademm-2.4-dev libgtkglextmm-x11-1.2-dev libusb-1.0-0
```
```
tar zxvf flycapture2-2.13.3.31-amd64-pkg_Ubuntu18.04.tgz
```

```
sudo sh install_flycapture.sh
```

Finally, the following message will appear:
```
Would you like to add a udev entry to allow access to IEEE-1394 and USB hardware?
If this is not ran then your cameras may be only accessible by running flycap as sudo.
```
This depends on how you use it, but this time we will use y. Enter the necessary user name and enter y for everything else

#

First, select and download the release of the pyflycap2 repository on [Github](https://github.com/matham/pyflycap2/releases) that matches your version of Python. It seems to be available for Python 3.7 to 3.10.
Then install it using pip. For example, in Python 3.7 it would be as follows.

```
pip install pyflycap2-0.3.1-cp37-cp37m-linux_x86_64.whl
```

```
sudo apt install libcanberra-gtk-module
```
