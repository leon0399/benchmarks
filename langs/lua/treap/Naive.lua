math.randomseed(os.time())

Node = {}
Node.__index = Node

function Node:new(x)
    local instance = setmetatable({}, self)
    instance.x = x
    instance.y = math.random()
    instance.left = nil
    instance.right = nil
    return instance
end

function merge(lower, greater)
    if lower == nil then
        return greater
    end

    if greater == nil then
        return lower
    end

    if lower.y < greater.y then
        lower.right = merge(lower.right, greater)
        return lower
    else
        greater.left = merge(lower, greater.left)
        return greater
    end
end

function splitBinary(orig, value)
    if orig == nil then
        return nil, nil
    end

    if orig.x < value then
        local rightLower, rightGreater = splitBinary(orig.right, value)
        orig.right = rightLower
        return orig, rightGreater
    else
        local leftLower, leftGreater = splitBinary(orig.left, value)
        orig.left = leftGreater
        return leftLower, orig
    end
end

function merge3(lower, equal, greater)
    return merge(merge(lower, equal), greater)
end

SplitResult = {}
SplitResult.__index = SplitResult

function SplitResult:new(lower, equal, greater)
    local instance = setmetatable({}, self)
    instance.lower = lower
    instance.equal = equal
    instance.greater = greater
    return instance
end

function split(orig, value)
    local lower, equalGreater = splitBinary(orig, value)
    local equal, greater = splitBinary(equalGreater, value + 1)
    return SplitResult:new(lower, equal, greater)
end

Tree = {}
Tree.__index = Tree

function Tree:new()
    local instance = setmetatable({}, self)
    instance.root = nil
    return instance
end

function Tree:hasValue(x)
    local splited = split(self.root, x)
    local res = splited.equal ~= nil
    self.root = merge3(splited.lower, splited.equal, splited.greater)
    return res
end

function Tree:insert(x)
    local splited = split(self.root, x)
    if splited.equal == nil then
        splited.equal = Node:new(x)
    end
    self.root = merge3(splited.lower, splited.equal, splited.greater)
end

function Tree:erase(x)
    local splited = split(self.root, x)
    self.root = merge(splited.lower, splited.greater)
end

function main()
    local tree = Tree:new()
    local cur = 5
    local res = 0

    for i = 1, 999999 do
        local a = i % 3
        cur = (cur * 57 + 43) % 10007

        if a == 0 then
            tree:insert(cur)
        elseif a == 1 then
            tree:erase(cur)
        elseif a == 2 then
            res = res + (tree:hasValue(cur) and 1 or 0)
        end
    end

    print(res)
end

local startTimeMs = math.floor(os.clock() * 1000)
main()
local endTimeMs = math.floor(os.clock() * 1000)
local durationMs = endTimeMs - startTimeMs

print("Execution time: " .. durationMs .. "ms")
