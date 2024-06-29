#!/usr/bin/env perl

use strict;
use warnings;
use Time::HiRes qw(time);
use POSIX qw(floor);

use constant NUMBER => 100000;

sub get_last_prime {
    my ($count) = @_;
    my $last_prime = 2;

    for (my $i = 2; $i <= $count; $i++) {
        my $is_prime = 1;

        for (my $j = 2; $j <= $i / 2; $j++) {
            if ($i % $j == 0) {
                $is_prime = 0;
                last;
            }
        }

        if ($is_prime) {
            $last_prime = $i;
        }
    }

    return $last_prime;
}

sub main {
    my $start_time_ms = floor(time() * 1000);

    my $last_prime = get_last_prime(NUMBER);
    print "Last prime: $last_prime\n";

    my $end_time_ms = floor(time() * 1000);
    my $duration_ms = $end_time_ms - $start_time_ms;

    print "Execution time: ${duration_ms}ms\n";
}

main();
