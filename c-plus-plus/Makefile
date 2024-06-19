CXXFLAGS = --std=c++17 -flto -s

SCRIPTS = $(wildcard ./source/*/*.cpp)

BINARIES =  $(SCRIPTS:%.cpp=%-clang) \
			$(SCRIPTS:%.cpp=%-clang-static) \
			$(SCRIPTS:%.cpp=%-gcc) \
			$(SCRIPTS:%.cpp=%-gcc-static) \

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

clean:
	rm -f $(BINARIES)

list:
	@echo $(BINARIES)

.PHONY: clean list