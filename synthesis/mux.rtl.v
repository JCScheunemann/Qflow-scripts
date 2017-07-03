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

	INVX1 INVX1_1 ( .gnd(gnd), .vdd(vdd), .A(sel[1]), .Y(_abc_58_n8_1) );
	NOR2X1 NOR2X1_1 ( .gnd(gnd), .vdd(vdd), .A(i1), .B(_abc_58_n8_1), .Y(_abc_58_n9) );
	MUX2X1 MUX2X1_1 ( .gnd(gnd), .vdd(vdd), .A(i3), .B(i4), .S(sel[1]), .Y(_abc_58_n10) );
	OAI21X1 OAI21X1_1 ( .gnd(gnd), .vdd(vdd), .A(sel[1]), .B(i2), .C(sel[0]), .Y(_abc_58_n11) );
	OAI22X1 OAI22X1_1 ( .gnd(gnd), .vdd(vdd), .A(_abc_58_n11), .B(_abc_58_n9), .C(sel[0]), .D(_abc_58_n10), .Y(out_FF_INPUT) );
	BUFX2 BUFX2_1 ( .gnd(gnd), .vdd(vdd), .A(_auto_iopadmap_cc_164_execute_64), .Y(out) );
	DFFPOSX1 DFFPOSX1_1 ( .gnd(gnd), .vdd(vdd), .CLK(clk), .D(out_FF_INPUT), .Q(_auto_iopadmap_cc_164_execute_64) );
endmodule
