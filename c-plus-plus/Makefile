CXXFLAGS = -O3 --std=c++20 -flto -s
INCLUDES = 
OBJECTS = 
LDFLAGS = 

SCRIPTS = $(wildcard ./src/*/*.cpp)

BINARIES =  $(SCRIPTS:%.cpp=%-clang) \
			$(SCRIPTS:%.cpp=%-clang-static) \
			$(SCRIPTS:%.cpp=%-gcc) \
			$(SCRIPTS:%.cpp=%-gcc-static) \

%-clang: %.cpp
	clang++ $(CXXFLAGS) -o $@ $<

%-clang-static: %.cpp
	clang++ $(CXXFLAGS) -static -o $@ $<

%-gcc : %.cpp
	g++ $(CXXFLAGS) -o $@ $<

%-gcc-static : %.cpp
	g++ $(CXXFLAGS) -static -o $@ $<

%-graalvm : %.cpp
	$${GRAALVM_LLVM_TOOLCHAIN}/clang++ $(CXXFLAGS) -o $@ $<

%-graalvm-static : %.cpp
	$${GRAALVM_LLVM_TOOLCHAIN}/clang++ $(CXXFLAGS) -static -o $@ $<

all: $(BINARIES)

clean:
	rm -f $(BINARIES)

list:
	@echo $(BINARIES)

.PHONY: clean list