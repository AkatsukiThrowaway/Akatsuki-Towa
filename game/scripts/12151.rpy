label avg12151:
stop music

play music "ED6505.ogg"
scene avg_bg_027
with fade
play sfx2 "other_7060.ogg"
show uc004_02 1 as c960portrait at leftside(-9), zorder 5
c9601 '[textdict[str(1128367)]]'
hide c960portrait
show uc004_02 1 as c960portrait at darkleft(-9), zorder 6
show uc004_02 2 as c961portrait at rightside(-9), zorder 5
c9613 '[textdict[str(1128368)]]'
hide c961portrait
hide c960portrait
show uc004_02 1 as c960portrait at darkleft(-9), zorder 6
show oc001_01 1 as c1portrait at rightsideentrance(-2), zorder 5
c13 '[textdict[str(1128369)]]'
hide c1portrait
hide c960portrait
show uc004_02 1 as c960portrait at darkleft(-9), zorder 6
show oc002_01 2 as c2portrait at rightside(-3), zorder 5
c23 '[textdict[str(1128370)]]'
hide c960portrait
hide c2portrait
show oc002_01 2 as c2portrait at darkright(-3), zorder 5
show uc004_02 1 as c960portrait at leftside(-9), zorder 5
c9601 '[textdict[str(1128371)]]'
play music "ED6107.ogg"
scene avg_bg_070
with fade
play sfx2 "other_7021.ogg"
c00 '[textdict[str(1128373)]]'
scene avg_bg_038
with fade
c9621 '[textdict[str(1128374)]]'
c9621 '[textdict[str(1128375)]]'
show oc002_01 2 as c2portrait at rightside(-3), zorder 5
c23 '[textdict[str(1128376)]]'
hide c2portrait
show oc002_01 2 as c2portrait at darkright(-3), zorder 5
c9621 '[textdict[str(1128377)]]'
hide c2portrait
show oc002_01 2 as c2portrait at darkright(-3), zorder 5
c9621 '[textdict[str(1128378)]]'
menu:
    "[textdict[str(1100001)]]":
        call avg12154
    "[textdict[str(1100002)]]":
        call avg12153
return