#!/bin/bash
#example of group plotting
#plot "< awk '$2 == \"12\" {print}' testconv.csv" using 3:6 w lines smooth csplines, "< awk '$2 == \"2\" {print}' testconv.csv" using 3:6 w lines smooth csplines, 'testconv.csv' using 3:5 w points
if [ \( $# -lt 5 -a $# -gt 0 \) ]
then
	name=`find temp/ -name "$1-*conv*.csv" -type f -printf '%T@ %p\n' | sort -n | tail -1 | cut -f2- -d" "`;
	nums=`awk '{print $2}' < $name | sort -n | uniq`
        width=800;
        height=600;
        type="wxt";
        if [ $# -gt 2 ] #3 or more parameters
        then
            width=$2;
            height=$3;
            if [ $# -gt 3 ] #4 parameters
            then
                type="png";
            fi
        fi
	s="set terminal ""$type"" size ""$width"",""$height""; ";
        if [ $# -gt 3 ]
        then
            s=$s"set output \"output.png\"; ";
        fi
	s=$s"set title 'Conversion: simulation vs experiment, iter="$1"';";
	s=$s" plot";
	#for (( i=1; i<=20; i++ ))
	k=0;
	for i in $nums
	do
		(( k++ ));
		if [ $k -gt 1 ]
		then
			s=$s",";
		fi
# shell commands inside gnuplot http://folk.uio.no/hpl/scripting/doc/gnuplot/Kawano/datafile3-e.html#sort
		#s=$s" \"< awk '\$2 == \\\"$i\\\" {print}' $name\" using 3:6 w lines title '$i-sml', \"< awk '\$2 == \\\"$i\\\" {print}' $name\" using 3:5 w points title '$i-exp'";
s=$s" \"< awk '\$2 == \\\"$i\\\" {print}' $name\" using 3:6:2 w lines title '$i-sml' lc variable, \"< awk '\$2 == \\\"$i\\\" {print}' $name\" using 3:5:2 w points title '$i-exp'  lc variable, \"< awk '\$2 == \\\"$i\\\" {print}' $name\" using 3:9:2 w lines title '$i-sml-p2' lc variable, \"< awk '\$2 == \\\"$i\\\" {print}' $name\" using 3:8:2 w points title '$i-exp-p2'  lc variable, \"< awk '\$2 == \\\"$i\\\" {print}' $name\" using 3:12:2 w lines title '$i-sml-p3'  lc variable, \"< awk '\$2 == \\\"$i\\\" {print}' $name\" using 3:11:2 w points title '$i-exp-p3' lc variable";
#s=$s" \"< awk '\$2 == \\\"$i\\\" {print}' $name\" using 3:6 w lines smooth csplines title '$i-sml', \"< awk '\$2 == \\\"$i\\\" {print}' $name\" using 3:5 w points title '$i-exp'";
	done
	#s=$s" \"$name\" using 3:5 w points";
	echo $s > plot1.gp
#call persistent gnuplot http://www.manpagez.com/info/gnuplot/gnuplot-4.4.0/gnuplot_14.php
# (- option instead of --persist do not close gnuplot)
	gnuplot plot1.gp --persist
else
        echo '====================================================='
	echo 'The program requries 1-4 arguments (1st is mandatory,'
        echo ' with iteration number to plot)!'
        echo 'Usage: ./viewconv.sh iter_num [width] [height] [png]'
        echo '====================================================='
fi
