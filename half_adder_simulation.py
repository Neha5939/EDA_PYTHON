from myhdl import *
def Half_adder(a,b,c,d):
    @always_comb
    def logic():
        c.next= a ^ b
        d.next= a and b
    return logic

#simulation
def simulate_half_adder():
    a,b,c,d=[Signal(bool(0)) for _ in range(4)]
    def bench():
        hadder_inst=Half_adder(a,b,c,d)
        @instance
        def stimulus():
            print("a b | c")
            print("-------")
            for i in range(2):
                for j in range(2):
                    a.next, b.next=i,j
                    yield delay(10)
                    print(f'{int(a)} {int(b)} | {int(c)} | {int(d)}')
        return hadder_inst,stimulus
    #generate vcd
    tb=traceSignals(bench)
    sim=Simulation(tb)
    sim.run()
    print("VCD file generated as bench.vcd")
#run
def test():
    simulate_half_adder()
test()