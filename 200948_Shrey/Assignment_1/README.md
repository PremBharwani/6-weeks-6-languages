I have implemented all the functions asked and  hard-coded data of **3** *'Members'* which can be accessed one-by-one (or all of it at the same time) by running the script and displays the use of all functions except 1 (*update_by_info*).

To invoke *update_by_info* the following lines can be uncommented one-by-one. 

>**Line 135:**   Member.update_info_by_id(100900,"who","who",8090980089,dt.date(1976,9,22)) *###Invalid INPUT*
>
>**Line 136:**   Member.update_info_by_id(100000,"who","who",8090980089,dt.date(1976,9,22)) *### Valid INPUT*