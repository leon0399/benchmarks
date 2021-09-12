SCRIPTS = $(wildcard **/*.cpp)

BINARIES = $(SCRIPTS:%.cpp=%-clang) $(SCRIPTS:%.cpp=%-clang-static) $(SCRIPTS:%.cpp=%-gcc) $(SCRIPTS:%.cpp=%-gcc-static)

%-clang: %.cpp
	clang++ -O3 --std=c++17 -flto -s -o $@ $<

%-clang-static: %.cpp
	clang++ -O3 --std=c++17 -flto -s -static -o $@ $<

%-gcc : %.cpp
	g++ -O3 --std=c++17 -flto -s -o $@ $<

%-gcc-static : %.cpp
	g++ -O3 --std=c++17 -flto -s -static -o $@ $<

all: $(BINARIES)

.PHONY: clean
clean:
	rm -f $(BINARIES)