label avg10064:
stop music

play music "ED6103.ogg"
scene avg_bg_038
with fade
play sfx2 "common_menu.ogg"
show oc001_01 1 as c1portrait at leftside(-2), zorder 5
c11 '[textdict[str(1005000)]]'
hide c1portrait
show oc001_01 1 as c1portrait at darkleft(-2), zorder 6
show sc007_01 1 as c15portrait at rightside(-17), zorder 5
c153 '[textdict[str(1005001)]]'
hide c15portrait
hide c1portrait
show oc001_01 1 as c1portrait at darkleft(-2), zorder 6
show oc002_01 2 as c2portrait at rightside(-3), zorder 5
c23 '[textdict[str(1005002)]]'
hide c1portrait
hide c2portrait
show oc002_01 2 as c2portrait at darkright(-3), zorder 5
show oc001_01 7 as c1portrait at leftside(-2), zorder 5
c11 '[textdict[str(1005003)]]'
hide c2portrait
hide c1portrait
show oc001_01 7 as c1portrait at darkleft(-2), zorder 6
show oc004_01 7 as c4portrait at rightside(-5), zorder 5
c43 '[textdict[str(1005004)]]'
hide c4portrait
hide c1portrait
show oc001_01 7 as c1portrait at darkleft(-2), zorder 6
show sc039_01 5 as c46portrait at rightside(-13), zorder 5
c463 '[textdict[str(1005005)]]'
play sfxvoice "avg_vocal_na05.ogg"
hide c1portrait
hide c46portrait
show sc039_01 5 as c46portrait at darkright(-13), zorder 5
show oc001_01 10 as c1portrait at leftside(-2), zorder 5
c11 '[textdict[str(1005006)]]'
hide c46portrait
hide c1portrait
show oc001_01 10 as c1portrait at darkleft(-2), zorder 6
show oc002_01 8 as c2portrait at rightside(-3), zorder 5
c23 '[textdict[str(1005007)]]'
return