import cocotb
from cocotb.triggers import Timer
from cocotb.result import TestFailure
@cocotb.test()
async def test_nand_gate(dut):
    test_cases=[
        (0,0,1),
        (0,1,1),
        (1,0,1),
        (1,1,0)
    ]
    for a,b,expected in test_cases:
        dut.A.value=a
        dut.B.value=b
        await Timer(10,units='ns')
        if dut.Y.value !=expected:
            raise TestFailure(f"Failed for A={a}, B={b}, Expected={expected},Got={int(dut.Y.value)}")
