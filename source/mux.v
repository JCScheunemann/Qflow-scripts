module mux(
		i1,
		i2,
		i3,
		i4,
		sel,
		out,
		clk,
		lol
		);
input i1,i2,i3,i4,clk;
input [1:0] sel;
input [2:1] lol;
output out;

always @(posedge clk) begin
	out= sel[0] ? (sel[1] ? i1:i2) : (sel[1] ? i3:i4); 
	end
//assign out= sel[0] ? (sel[1] ? i1:i2) : (sel[1] ? i3&i4:i4);
endmodule
