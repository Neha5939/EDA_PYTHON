from myhdl import *
def Nor_Gate(a,b,c):
    @always_comb
    def logic():
        c.next= not(a | b)
    return logic

#simulation
def simulate_nor_gate():
    a,b,c=[Signal(bool(0)) for _ in range(3)]
    def bench():
        nor_inst=Nor_Gate(a,b,c)
        @instance
        def stimulus():
            print("a b | c")
            print("-------")
            for i in range(2):
                for j in range(2):
                    a.next, b.next=i,j
                    yield delay(10)
                    print(f'{int(a)} {int(b)} | {int(c)}')
        return nor_inst,stimulus
    #generate vcd
    tb=traceSignals(bench)
    sim=Simulation(tb)
    sim.run()
    print("VCD file generated as bench.vcd ")
#run
def test():
    simulate_nor_gate()
test()