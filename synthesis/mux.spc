*SPICE netlist created from BLIF module mux by blif2BSpice
.include /usr/local/share/qflow/tech/osu035/osu035_stdcells.sp
.subckt mux vdd gnd i1 i2 i3 i4 sel<0> sel<1> clk lol<0> lol<1> out 
XOAI22X1_1 gnd vdd _1_ sel<0> _2_ _4_ _0_ OAI22X1
XBUFX2_1 vdd gnd _5_ out BUFX2
XDFFPOSX1_1 vdd _0_ gnd _5_ clk DFFPOSX1
XINVX1_1 sel<1> _3_ vdd gnd INVX1
XNOR2X1_1 vdd _3_ gnd _4_ i1 NOR2X1
XMUX2X1_1 sel<1> vdd gnd _1_ i3 i4 MUX2X1
XOAI21X1_1 gnd vdd sel<1> i2 _2_ sel<0> OAI21X1
.ends mux
 