CXXFLAGS = --std=c++17 -flto -s

SCRIPTS = $(wildcard **/*.cpp)

BINARIES =  $(SCRIPTS:%.cpp=%-clang) \
			$(SCRIPTS:%.cpp=%-clang-static) \
			$(SCRIPTS:%.cpp=%-gcc) \
			$(SCRIPTS:%.cpp=%-gcc-static) \
			# $(SCRIPTS:%.cpp=%-graalvm) \
			# $(SCRIPTS:%.cpp=%-graalvm-static) \


%-clang: %.cpp
	clang++ -O3 $(CXXFLAGS) -o $@ $<

%-clang-static: %.cpp
	clang++ -O3 $(CXXFLAGS) -static -o $@ $<

%-gcc : %.cpp
	g++ -O3 $(CXXFLAGS) -o $@ $<

%-gcc-static : %.cpp
	g++ -O3 $(CXXFLAGS) -static -o $@ $<

%-graalvm : %.cpp
	$${GRAALVM_LLVM_TOOLCHAIN}/clang++ -O3 $(CXXFLAGS) -o $@ $<

%-graalvm-static : %.cpp
	$${GRAALVM_LLVM_TOOLCHAIN}/clang++ -O3 $(CXXFLAGS) -static -o $@ $<

all: $(BINARIES)

.PHONY: clean
clean:
	rm -f $(BINARIES)