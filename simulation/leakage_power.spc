*Power estimation scripts
*Global paremeters defines
.PARAM vdd_value=3v

*DC power supply
vsupply vdd 0 vdd_value

*Output load
Cload out 0 25f

*Inputs sources

v1 in1 0 pulse(0 vdd_value 0 100p 100p 19.9n 40n)
v2 in2 0 pulse(0 vdd_value 5.01 100p 100p 19.9n 45n)
v3 in3 0 pulse(0 vdd_value 10.01 100p 100p 19.9n 50n)
v4 in4 0 pulse(0 vdd_value 15.01 100p 100p 19.9n 40n)
v5 clk 0 pulse(0 vdd_value 0 100p 100p 4.9n 10n)
v6 sel0 0 pulse(0 vdd_value 20.01 100p 100p 19.9n 45n)
v7 sel1 0 pulse(0 vdd_value 25.01 100p 100p 19.9n 45n)

*Device under test
*.subckt mux vdd 0 i1 i2 i3 i4 sel0 sel1 clk out 
xmux_1 vdd 0 in1 in2 in3 in4 sel0 sel1 clk out mux


*Simulation Time interval
*.options method=trap reltol=0.1m
*.tran t0 t1
.tran 10p 20n
.save all @vsupply[p]
.control
	run
	write inverter.raw
	plot -i(vsupply)
	*meas tran iave INTEG i(vsupply) from=tp_start to=tp_stop
	*let power = -iave * vdd_value / (tp_stop-tp_start) ; how to access psu from here?
	meas tran iave1 INTEG i(vsupply) from=1n to=5n
	let power1 = -iave1 * 3 / 4ns 
    print power1
	meas tran iave2 INTEG i(vsupply) from=6n to=10n
	let power2 = -iave2 * 3 / 4ns 
    print power2
	meas tran iave3 INTEG i(vsupply) from=11n to=15n
	let power3 = -iave3 * 3 / 4ns 
    print power3
	meas tran iave4 INTEG i(vsupply) from=16n to=20n
	let power4 = -iave4 * 3 / 4ns 
    print power4
	*exit
.endc
