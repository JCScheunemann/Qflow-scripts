module mux ( gnd, vdd, i1, i2, i3, i4, sel, clk, lol, out);

input gnd, vdd;
input i1;
input i2;
input i3;
input i4;
input clk;
output out;
input [1:0] sel;
input [1:0] lol;

	OAI22X1 OAI22X1_1 ( .gnd(gnd), .vdd(vdd), .A(_2_), .B(_4_), .C(sel[0]), .D(_1_), .Y(_0_) );
	BUFX2 BUFX2_1 ( .gnd(gnd), .vdd(vdd), .A(_5_), .Y(out) );
	DFFPOSX1 DFFPOSX1_1 ( .gnd(gnd), .vdd(vdd), .CLK(clk), .D(_0_), .Q(_5_) );
	INVX1 INVX1_1 ( .gnd(gnd), .vdd(vdd), .A(sel[1]), .Y(_3_) );
	NOR2X1 NOR2X1_1 ( .gnd(gnd), .vdd(vdd), .A(i1), .B(_3_), .Y(_4_) );
	MUX2X1 MUX2X1_1 ( .gnd(gnd), .vdd(vdd), .A(i3), .B(i4), .S(sel[1]), .Y(_1_) );
	OAI21X1 OAI21X1_1 ( .gnd(gnd), .vdd(vdd), .A(sel[1]), .B(i2), .C(sel[0]), .Y(_2_) );
endmodule