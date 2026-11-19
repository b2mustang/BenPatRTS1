namespace Footprint.Sim.Tests;

public class DeterministicRandomTests
{
    [Fact]
    public void SplitMix64_MatchesReferenceOutput()
    {
        // Reference output of SplitMix64 starting from 0 (Vigna, prng.di.unimi.it).
        ulong x = 0;
        Assert.Equal(0xE220A8397B1DCDAFUL, DeterministicRandom.SplitMix64(ref x));
        Assert.Equal(0x6E789E6AA1B965F4UL, DeterministicRandom.SplitMix64(ref x));
        Assert.Equal(0x06C45D188009454FUL, DeterministicRandom.SplitMix64(ref x));
    }

    [Fact]
    public void Xoshiro256StarStar_MatchesReferenceOutput()
    {
        // Reference output of xoshiro256** from the state {1, 2, 3, 4}.
        var random = DeterministicRandom.FromState(new RandomState(1, 2, 3, 4));
        Assert.Equal(11520UL, random.NextUInt64());
        Assert.Equal(0UL, random.NextUInt64());
        Assert.Equal(1509978240UL, random.NextUInt64());
        Assert.Equal(1215971899390074240UL, random.NextUInt64());
    }

    [Fact]
    public void SameSeed_GivesSameSequence()
    {
        var a = new DeterministicRandom(42);
        var b = new DeterministicRandom(42);
        for (int i = 0; i < 1000; i++)
        {
            Assert.Equal(a.NextUInt64(), b.NextUInt64());
        }
    }

    [Fact]
    public void DifferentSeeds_GiveDifferentSequences()
    {
        var a = new DeterministicRandom(1);
        var b = new DeterministicRandom(2);
        Assert.NotEqual(Draw(a, 8), Draw(b, 8));
    }

    [Fact]
    public void RestoredState_ContinuesTheSameSequence()
    {
        var original = new DeterministicRandom(7);
        Draw(original, 100);

        var restored = DeterministicRandom.FromState(original.State);
        Assert.Equal(Draw(original, 100), Draw(restored, 100));
    }

    [Fact]
    public void AllZeroState_IsRejected()
    {
        Assert.Throws<ArgumentException>(() => DeterministicRandom.FromState(new RandomState(0, 0, 0, 0)));
    }

    [Theory]
    [InlineData(1)]
    [InlineData(6)]
    [InlineData(10_000)]
    [InlineData(int.MaxValue)]
    public void NextInt_StaysInRange(int maxExclusive)
    {
        var random = new DeterministicRandom(3);
        for (int i = 0; i < 10_000; i++)
        {
            int value = random.NextInt(maxExclusive);
            Assert.InRange(value, 0, maxExclusive - 1);
        }
    }

    [Theory]
    [InlineData(-5, 5)]
    [InlineData(10, 11)]
    [InlineData(int.MinValue, int.MaxValue)]
    public void NextIntWithMinimum_StaysInRange(int minInclusive, int maxExclusive)
    {
        var random = new DeterministicRandom(4);
        for (int i = 0; i < 10_000; i++)
        {
            int value = random.NextInt(minInclusive, maxExclusive);
            Assert.InRange(value, minInclusive, maxExclusive - 1);
        }
    }

    [Fact]
    public void NextInt_HitsEveryValueOfASmallRange()
    {
        var random = new DeterministicRandom(5);
        var seen = new bool[6];
        for (int i = 0; i < 1000; i++)
        {
            seen[random.NextInt(6)] = true;
        }

        Assert.All(seen, Assert.True);
    }

    [Theory]
    [InlineData(0)]
    [InlineData(-1)]
    public void NextInt_RejectsEmptyRanges(int maxExclusive)
    {
        var random = new DeterministicRandom(6);
        Assert.Throws<ArgumentOutOfRangeException>(() => random.NextInt(maxExclusive));
        Assert.Throws<ArgumentOutOfRangeException>(() => random.NextInt(5, 5 + maxExclusive));
    }

    [Theory]
    [InlineData(0, false)]
    [InlineData(-100, false)]
    [InlineData(10_000, true)]
    [InlineData(25_000, true)]
    public void Roll_AtTheExtremes_IsCertain(int chanceBasisPoints, bool expected)
    {
        var random = new DeterministicRandom(8);
        for (int i = 0; i < 1000; i++)
        {
            Assert.Equal(expected, random.Roll(chanceBasisPoints));
        }
    }

    [Theory]
    [InlineData(3_000)]
    [InlineData(5_000)]
    [InlineData(8_000)]
    public void Roll_SucceedsAtRoughlyTheGivenRate(int chanceBasisPoints)
    {
        const int rolls = 100_000;
        var random = new DeterministicRandom(9);
        int successes = 0;
        for (int i = 0; i < rolls; i++)
        {
            if (random.Roll(chanceBasisPoints))
            {
                successes++;
            }
        }

        // Fixed seed, so this is exact on every run; the tolerance only guards against a broken roll.
        int expected = rolls / DeterministicRandom.BasisPointsPerWhole * chanceBasisPoints;
        Assert.InRange(successes, expected - 1000, expected + 1000);
    }

    private static ulong[] Draw(DeterministicRandom random, int count)
    {
        var values = new ulong[count];
        for (int i = 0; i < count; i++)
        {
            values[i] = random.NextUInt64();
        }

        return values;
    }
}
