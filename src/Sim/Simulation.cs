namespace Footprint.Sim;

/// <summary>
/// The root of a running simulation. Placeholder for M0: it only owns the seed and the tick count.
/// </summary>
/// <remarks>
/// Commands, the mission RNG (<see cref="DeterministicRandom"/>), truth versus player knowledge and
/// save data arrive in M1 (see CLAUDE.md, Architecture rules).
/// Presentation code steps it at a fixed tick rate; speed controls change how many ticks run per second.
/// </remarks>
public sealed class Simulation
{
    public Simulation(ulong seed)
    {
        Seed = seed;
    }

    public ulong Seed { get; }

    /// <summary>The number of ticks run so far.</summary>
    public long Tick { get; private set; }

    /// <summary>Advances the simulation by one tick.</summary>
    public void Step()
    {
        Tick++;
    }
}
