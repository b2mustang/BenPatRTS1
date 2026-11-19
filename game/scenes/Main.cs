using System.Linq;
using Footprint.Sim;
using Godot;

namespace Footprint;

/// <summary>
/// Placeholder main scene for M0: shows that the game can create and step the sim.
/// Run with <c>-- --smoke-test</c> to step a fixed number of ticks and quit with an exit code.
/// </summary>
public partial class Main : Node
{
    private const string SmokeTestArgument = "--smoke-test";
    private const int SmokeTestTicks = 100;

    private Simulation _sim = null!;
    private Label _status = null!;

    public override void _Ready()
    {
        _sim = new Simulation(seed: 1);
        _status = new Label { Position = new Vector2(16, 16) };
        AddChild(_status);

        if (OS.GetCmdlineUserArgs().Contains(SmokeTestArgument))
        {
            RunSmokeTest();
        }
    }

    public override void _PhysicsProcess(double delta)
    {
        // Placeholder: one sim tick per physics frame. M1 sets the real tick rate and speed controls.
        _sim.Step();
        _status.Text = $"Footprint - sim tick {_sim.Tick}";
    }

    private void RunSmokeTest()
    {
        for (int i = 0; i < SmokeTestTicks; i++)
        {
            _sim.Step();
        }

        bool passed = _sim.Tick == SmokeTestTicks;
        GD.Print($"Smoke test {(passed ? "passed" : "FAILED")}: sim reached tick {_sim.Tick}.");
        GetTree().Quit(passed ? 0 : 1);
    }
}
