using System;

namespace Footprint.Sim;

/// <summary>
/// Seeded random number generator for the simulation (xoshiro256**, seeded with SplitMix64).
/// </summary>
/// <remarks>
/// The sim never uses <see cref="System.Random"/>: its output is not guaranteed to stay the same
/// across .NET versions, and a seed plus a command list must reproduce a run exactly.
/// All results are integers; chances are in basis points (10000 = 100%).
/// </remarks>
public sealed class DeterministicRandom
{
    public const int BasisPointsPerWhole = 10_000;

    private ulong _s0;
    private ulong _s1;
    private ulong _s2;
    private ulong _s3;

    public DeterministicRandom(ulong seed)
    {
        ulong x = seed;
        _s0 = SplitMix64(ref x);
        _s1 = SplitMix64(ref x);
        _s2 = SplitMix64(ref x);
        _s3 = SplitMix64(ref x);
    }

    private DeterministicRandom(RandomState state)
    {
        if ((state.S0 | state.S1 | state.S2 | state.S3) == 0)
        {
            throw new ArgumentException("A xoshiro256** state cannot be all zeros.", nameof(state));
        }

        (_s0, _s1, _s2, _s3) = (state.S0, state.S1, state.S2, state.S3);
    }

    /// <summary>Restores a generator from a saved state.</summary>
    public static DeterministicRandom FromState(RandomState state) => new(state);

    /// <summary>The current state, for saves. Restoring it continues the exact same sequence.</summary>
    public RandomState State => new(_s0, _s1, _s2, _s3);

    /// <summary>Returns the next 64 random bits.</summary>
    public ulong NextUInt64()
    {
        ulong result = RotateLeft(_s1 * 5, 7) * 9;
        ulong t = _s1 << 17;

        _s2 ^= _s0;
        _s3 ^= _s1;
        _s1 ^= _s2;
        _s0 ^= _s3;
        _s2 ^= t;
        _s3 = RotateLeft(_s3, 45);

        return result;
    }

    /// <summary>Returns a uniformly distributed integer in [0, <paramref name="maxExclusive"/>).</summary>
    public int NextInt(int maxExclusive)
    {
        if (maxExclusive <= 0)
        {
            throw new ArgumentOutOfRangeException(nameof(maxExclusive), maxExclusive, "Must be positive.");
        }

        return (int)NextBelow((ulong)maxExclusive);
    }

    /// <summary>Returns a uniformly distributed integer in [<paramref name="minInclusive"/>, <paramref name="maxExclusive"/>).</summary>
    public int NextInt(int minInclusive, int maxExclusive)
    {
        if (maxExclusive <= minInclusive)
        {
            throw new ArgumentOutOfRangeException(nameof(maxExclusive), maxExclusive, "Must be greater than minInclusive.");
        }

        ulong range = (ulong)((long)maxExclusive - minInclusive);
        return (int)(minInclusive + (long)NextBelow(range));
    }

    /// <summary>
    /// Rolls against a chance in basis points: 0 never succeeds, 10000 or more always succeeds.
    /// </summary>
    public bool Roll(int chanceBasisPoints)
    {
        if (chanceBasisPoints <= 0)
        {
            return false;
        }

        if (chanceBasisPoints >= BasisPointsPerWhole)
        {
            return true;
        }

        return NextInt(BasisPointsPerWhole) < chanceBasisPoints;
    }

    // Unbiased: rejects the top partial range so every result is equally likely.
    private ulong NextBelow(ulong bound)
    {
        ulong limit = ulong.MaxValue - (ulong.MaxValue % bound);
        ulong value;
        do
        {
            value = NextUInt64();
        }
        while (value >= limit);

        return value % bound;
    }

    internal static ulong SplitMix64(ref ulong x)
    {
        x += 0x9E3779B97F4A7C15UL;
        ulong z = x;
        z = (z ^ (z >> 30)) * 0xBF58476D1CE4E5B9UL;
        z = (z ^ (z >> 27)) * 0x94D049BB133111EBUL;
        return z ^ (z >> 31);
    }

    private static ulong RotateLeft(ulong value, int count) => (value << count) | (value >> (64 - count));
}

/// <summary>The saved state of a <see cref="DeterministicRandom"/>.</summary>
public readonly record struct RandomState(ulong S0, ulong S1, ulong S2, ulong S3);
