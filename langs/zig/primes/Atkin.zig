const std = @import("std");

const UPPER_BOUND = 5000000;
const PREFIX = 32338;

const Node = struct {
    children: std.StringHashMap(*Node),
    terminal: bool,
    allocator: std.mem.Allocator,

    fn init(allocator: std.mem.Allocator) !*Node {
        const node = try allocator.create(Node);
        node.* = Node{
            .children = std.StringHashMap(*Node).init(allocator),
            .terminal = false,
            .allocator = allocator,
        };
        return node;
    }

    fn deinit(self: *Node) void {
        var iter = self.children.valueIterator();
        while (iter.next()) |child| {
            child.*.deinit();
        }
        self.children.deinit();
        self.allocator.destroy(self);
    }
};

const Sieve = struct {
    limit: i32,
    prime: []bool,
    allocator: std.mem.Allocator,

    fn init(allocator: std.mem.Allocator, limit: i32) !Sieve {
        const prime = try allocator.alloc(bool, @intCast(limit + 1));
        @memset(prime, false);
        return Sieve{
            .limit = limit,
            .prime = prime,
            .allocator = allocator,
        };
    }

    fn deinit(self: *Sieve) void {
        self.allocator.free(self.prime);
    }

    fn toList(self: *Sieve, allocator: std.mem.Allocator) !std.ArrayList(i32) {
        var result = std.ArrayList(i32).init(allocator);
        try result.append(2);
        try result.append(3);

        var p: i32 = 5;
        while (p <= self.limit) : (p += 1) {
            if (self.prime[@intCast(p)]) {
                try result.append(p);
            }
        }

        return result;
    }

    fn omitSquares(self: *Sieve) *Sieve {
        var r: i32 = 5;
        while (r * r < self.limit) : (r += 1) {
            if (self.prime[@intCast(r)]) {
                var i: i32 = r * r;
                while (i < self.limit) : (i += r * r) {
                    self.prime[@intCast(i)] = false;
                }
            }
        }
        return self;
    }

    fn step1(self: *Sieve, x: i32, y: i32) void {
        const n = (4 * x * x) + (y * y);
        if (n <= self.limit and (@mod(n, 12) == 1 or @mod(n, 12) == 5)) {
            self.prime[@intCast(n)] = !self.prime[@intCast(n)];
        }
    }

    fn step2(self: *Sieve, x: i32, y: i32) void {
        const n = (3 * x * x) + (y * y);
        if (n <= self.limit and @mod(n, 12) == 7) {
            self.prime[@intCast(n)] = !self.prime[@intCast(n)];
        }
    }

    fn step3(self: *Sieve, x: i32, y: i32) void {
        const n = (3 * x * x) - (y * y);
        if (x > y and n <= self.limit and @mod(n, 12) == 11) {
            self.prime[@intCast(n)] = !self.prime[@intCast(n)];
        }
    }

    fn loopY(self: *Sieve, x: i32) void {
        var y: i32 = 1;
        while (y * y < self.limit) : (y += 1) {
            self.step1(x, y);
            self.step2(x, y);
            self.step3(x, y);
        }
    }

    fn loopX(self: *Sieve) void {
        var x: i32 = 1;
        while (x * x < self.limit) : (x += 1) {
            self.loopY(x);
        }
    }

    fn calc(self: *Sieve) *Sieve {
        self.loopX();
        return self.omitSquares();
    }
};

fn generateTree(allocator: std.mem.Allocator, l: std.ArrayList(i32)) !*Node {
    const root = try Node.init(allocator);

    for (l.items) |el| {
        var head = root;
        var buf: [32]u8 = undefined;
        const str = try std.fmt.bufPrint(&buf, "{d}", .{el});

        for (str) |ch| {
            const key = try allocator.alloc(u8, 1);
            key[0] = ch;
            
            const existing = head.children.get(key);
            if (existing) |node| {
                allocator.free(key);
                head = node;
            } else {
                const new_node = try Node.init(allocator);
                try head.children.put(key, new_node);
                head = new_node;
            }
        }

        head.terminal = true;
    }

    return root;
}

fn find(allocator: std.mem.Allocator, upper_bound: i32, prefix: i32) !?std.ArrayList(i32) {
    var sieve = try Sieve.init(allocator, upper_bound);
    defer sieve.deinit();
    
    _ = sieve.calc();
    var primes_list = try sieve.toList(allocator);
    defer primes_list.deinit();

    var buf: [32]u8 = undefined;
    const str_prefix = try std.fmt.bufPrint(&buf, "{d}", .{prefix});

    const tree_root = try generateTree(allocator, primes_list);
    defer tree_root.deinit();

    var head = tree_root;
    for (str_prefix) |ch| {
        const key = try allocator.alloc(u8, 1);
        key[0] = ch;
        defer allocator.free(key);
        
        const next = head.children.get(key);
        if (next) |node| {
            head = node;
        } else {
            return null;
        }
    }

    const QueueItem = struct {
        node: *Node,
        prefix: []const u8,
    };

    var queue = std.ArrayList(QueueItem).init(allocator);
    defer {
        for (queue.items) |item| {
            allocator.free(item.prefix);
        }
        queue.deinit();
    }

    const initial_prefix = try allocator.dupe(u8, str_prefix);
    try queue.append(QueueItem{ .node = head, .prefix = initial_prefix });

    var result = std.ArrayList(i32).init(allocator);

    while (queue.items.len > 0) {
        const top = queue.pop();
        
        if (top.node.terminal) {
            const value = try std.fmt.parseInt(i32, top.prefix, 10);
            try result.append(value);
        }

        // Collect keys and sort them to maintain consistent order
        var keys = std.ArrayList([]const u8).init(allocator);
        defer keys.deinit();
        
        var iter = top.node.children.keyIterator();
        while (iter.next()) |key| {
            try keys.append(key.*);
        }
        
        // Sort keys in ascending order to match C++ std::map behavior
        std.mem.sort([]const u8, keys.items, {}, struct {
            fn lessThan(_: void, a: []const u8, b: []const u8) bool {
                return std.mem.order(u8, a, b) == .lt;
            }
        }.lessThan);
        
        for (keys.items) |ch| {
            const v = top.node.children.get(ch).?;
            const new_prefix = try std.fmt.allocPrint(allocator, "{s}{s}", .{ top.prefix, ch });
            try queue.insert(0, QueueItem{ .node = v, .prefix = new_prefix });
        }

        allocator.free(top.prefix);
    }

    return result;
}

pub fn main() anyerror!void {
    var gpa = std.heap.GeneralPurposeAllocator(.{}){};
    defer _ = gpa.deinit();
    const allocator = gpa.allocator();

    const stdout = std.io.getStdOut().writer();

    const start_time = std.time.milliTimestamp();

    const result = try find(allocator, UPPER_BOUND, PREFIX);
    if (result) |res| {
        defer res.deinit();
        
        try stdout.print("[", .{});
        for (res.items, 0..) |value, i| {
            if (i > 0) {
                try stdout.print(", ", .{});
            }
            try stdout.print("{d}", .{value});
        }
        try stdout.print("]\n", .{});
    } else {
        try stdout.print("null\n", .{});
    }

    const end_time = std.time.milliTimestamp();
    const duration = end_time - start_time;

    try stdout.print("Execution time: {}ms\n", .{duration});
}
