namespace Footprint.Sim.Tests;

public class SimulationTests
{
    [Fact]
    public void NewSimulation_StartsAtTickZeroWithItsSeed()
    {
        var sim = new Simulation(seed: 1234);
        Assert.Equal(1234UL, sim.Seed);
        Assert.Equal(0, sim.Tick);
    }

    [Fact]
    public void Step_AdvancesOneTick()
    {
        var sim = new Simulation(seed: 1);
        for (int i = 0; i < 5; i++)
        {
            sim.Step();
        }

        Assert.Equal(5, sim.Tick);
    }
}
