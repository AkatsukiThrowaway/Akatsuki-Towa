label avg1010:
stop music

play music "ed7106.ogg"
scene avg_bg_023
with fade
show sc049_01 1 as c56portrait at leftside(-8), zorder 5
c561 '[textdict[str(2100125)]]'
hide c56portrait
show sc049_01 1 as c56portrait at leftside(-8), zorder 5
c561 '[textdict[str(2100126)]]'
hide c56portrait
show sc049_01 1 as c56portrait at leftside(-8), zorder 5
c561 '[textdict[str(2100127)]]'
hide c56portrait
show sc049_01 1 as c56portrait at leftside(-8), zorder 5
c561 '[textdict[str(2100128)]]'
menu:
    "[textdict[str(2100129)]]":
        call avg1011
    "[textdict[str(2100130)]]":
        call avg1012
    "[textdict[str(2100131)]]":
        call avg1013
return