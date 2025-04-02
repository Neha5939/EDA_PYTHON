COCOTB:= $(shell python3 -c 'import cocotb; print(cocotb.__path__[0])')
VERILOG_SOURCES := nand_gate.v
TOPLEVEL := nand_gate
MODULE := test_nand_cocotb
SIM := icarus


include $(COCOTB)/share/makefiles/Makefile.sim