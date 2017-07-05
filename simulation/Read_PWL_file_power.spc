*Power estimation scripts
*Global paremeters defines
.PARAM vdd_value=3v

*DC power supply
vsupply vdd 0 vdd_value

*Output load
Cload out 0 25f

*Inputs sources

v1 in1 0 pulse(0 vdd_value 0 100p 100p 1.9n 3n)
v2 in2 0 pulse(0 vdd_value 0 100p 100p 1.9n 5n)
v3 in3 0 pulse(0 vdd_value 0 100p 100p 1.9n 4n)
v4 in4 0 pulse(0 vdd_value 0 100p 100p 1.9n 4.5n)
v5 clk 0 PWL file="clk.pwl"
v6 sel0 0 pulse(0 vdd_value 0 100p 100p 1.9n 4n)
v7 sel1 0 pulse(0 vdd_value 0 100p 100p 1.9n 3n)

*Device under test
*.subckt mux vdd 0 i1 i2 i3 i4 sel0 sel1 clk out 
xmux_1 vdd 0 in1 in2 in3 in4 sel0 sel1 clk out mux


*Simulation Time interval
*.options method=trap reltol=0.1m
*.tran t0 t1
.tran 10p 12n
.save all @vsupply[p]
.control
	run
	*meas tran iave INTEG i(vsupply) from=tp_start to=tp_stop
	meas tran iave INTEG i(vsupply) from=1n to=12n
	*let power = -iave * vdd_value / (tp_stop-tp_start) ; how to access psu from here?
	let power = -iave * 3 / 11ns ; how to access psu from here?
    print power
	*exit
.endc
