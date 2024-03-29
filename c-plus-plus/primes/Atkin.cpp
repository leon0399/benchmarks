#include <iostream>
#include <memory>
#include <queue>
#include <sstream>
#include <unistd.h>
#include <map>
#include <utility>
#include <vector>
#include <chrono>

static const auto UPPER_BOUND = 5'000'000;
static const auto PREFIX = 32'338;

struct Node {
  std::map<char, std::shared_ptr<Node>> children{};
  bool terminal = false;
};

class Sieve {
  int limit;
  std::vector<bool> prime;

  Sieve& omit_squares() {
    for (auto r = 5; r * r < limit; ++r) {
      if (prime[r]) {
        for (auto i = r * r; i < limit; i += r * r) {
          prime[i] = false;
        }
      }
    }
    return *this;
  }

  void step1(int x, int y) {
    const auto n = (4 * x * x) + (y * y);
    if (n <= limit && (n % 12 == 1 || n % 12 == 5)) {
      prime[n] = !prime[n];
    }
  }

  void step2(int x, int y) {
    const auto n = (3 * x * x) + (y * y);
    if (n <= limit && n % 12 == 7) {
      prime[n] = !prime[n];
    }
  }

  void step3(int x, int y) {
    const auto n = (3 * x * x) - (y * y);
    if (x > y && n <= limit && n % 12 == 11) {
      prime[n] = !prime[n];
    }
  }

  void loop_y(int x) {
    for (auto y = 1; y * y < limit; ++y) {
      step1(x, y);
      step2(x, y);
      step3(x, y);
    }
  }

  void loop_x() {
    for (auto x = 1; x * x < limit; ++x) {
      loop_y(x);
    }
  }

public:
  Sieve(int limit): limit(limit), prime(limit + 1, false) {}

  std::vector<int> to_list() const {
    std::vector<int> result({2, 3});
    for (auto p = 5; p <= limit; ++p) {
      if (prime[p]) {
        result.push_back(p);
      }
    }
    return result;
  }

  Sieve& calc() {
    loop_x();
    return omit_squares();
  }
};

std::shared_ptr<Node> generate_tree(const std::vector<int>& l) {
  auto root = std::make_shared<Node>();
  for (const auto el : l) {
    auto head = root;
    for (const auto ch: std::to_string(el)) {
      head->children.emplace(ch, std::make_shared<Node>());
      head = head->children[ch];
    }
    head->terminal = true;
  }
  return root;
}

std::vector<int> find(int upper_bound, int prefix) {
  const auto primes = Sieve(upper_bound).calc();
  const auto& str_prefix = std::to_string(prefix);
  auto head = generate_tree(primes.to_list());

  for (const auto ch : str_prefix) {
    head = head->children[ch];
  }

  std::queue<std::pair<std::shared_ptr<Node>, std::string>> queue(
    { std::make_pair(head, str_prefix) }
  );
  std::vector<int> result;
  while (!queue.empty()) {
    const auto& [top, prefix] = queue.front();
    queue.pop();
    if (top->terminal) {
      result.push_back(std::stoi(prefix));
    }
    for (const auto& [ch, v] : top->children) {
      queue.push(std::make_pair(v, prefix + ch));
    }
  }
  return result;
}

std::string to_string(const std::vector<int>& a) {
  std::stringstream ss;
  ss << "[";
  auto first = true;
  for (const auto el : a) {
    if (!first) {
      ss << ", ";
    }
    ss << el;
    first = false;
  }
  ss << "]";
  return ss.str();
}

int main() {
  const auto start_time = std::chrono::high_resolution_clock::now();

  std::cout << to_string(find(UPPER_BOUND, PREFIX)) << std::endl;
  
  const auto end_time = std::chrono::high_resolution_clock::now();
  const auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(end_time - start_time).count();

  std::cout << "Execution time: " << duration << "ms" << std::endl;
}