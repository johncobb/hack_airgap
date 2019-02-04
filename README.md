## Hacking the air gap 
### Merrill Cobb 
### Copy fan_ctl.py to RaspberrPi using scp
```console
# copy fan_ctl.py to home folder
scp fan_ctl.py pi@10.0.0.186:~/
# verify file was copied by logging into pi
ssh pi@10.0.0.186
```

### Run the fan_ctl.py program
```console
python air_gap.py
```

### Autostart on boot
```console
crontab -e
@reboot sudo python /home/po/aig_gap.py
```
 
#### Results
The fan and light will out-pulse HELLO WORLD in morse code.


### Code Editor
#### Visual Studio Code and VIM
### Programming Language
#### Python



### Resources
#### https://www.instructables.com/id/PWM-Regulated-Fan-Based-on-CPU-Temperature-for-Ras/
#### https://learn.adafruit.com/adafruit-arduino-lesson-10-making-sounds/playing-a-scale
#### http://fritzing.org
#### 
