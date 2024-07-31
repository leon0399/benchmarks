use strict;
use warnings;
use Time::HiRes qw(time);

sub tak {
    my ($x, $y, $z) = @_;
    return $y < $x
        ? tak(tak($x - 1, $y, $z), tak($y - 1, $z, $x), tak($z - 1, $x, $y))
        : $z;
}

sub main {
    my $startTimeMs = int(time * 1000);

    print tak(30, 22, 12), "\n";

    my $endTimeMs = int(time * 1000);
    my $durationMs = $endTimeMs - $startTimeMs;

    print "Execution time: " . $durationMs . "ms\n";
}

main();
