CXXFLAGS += -Wall -fPIC -std=c++17 -O3
INCLUDES += -Ilib/regex-boost/include
OBJECTS += 
LDFLAGS += -lstdc++ -lpthread

SCRIPTS = $(wildcard ./src/*/*.cpp)

BINARIES =  $(SCRIPTS:%.cpp=%-clang) \
			$(SCRIPTS:%.cpp=%-clang-static) \
			$(SCRIPTS:%.cpp=%-gcc) \
			$(SCRIPTS:%.cpp=%-gcc-static) \

%-clang: %.cpp
	clang++ $(CXXFLAGS) $(INCLUDES) -o $@ $< $(LDFLAGS)

%-clang-static: %.cpp
	clang++ $(CXXFLAGS) $(INCLUDES) -static -o $@ $< $(LDFLAGS)

%-gcc : %.cpp
	g++ $(CXXFLAGS) $(INCLUDES) -o $@ $< $(LDFLAGS)

%-gcc-static : %.cpp
	g++ $(CXXFLAGS) $(INCLUDES) -static -o $@ $< $(LDFLAGS)

all: libraries $(BINARIES)

libraries:
	cd ./lib/regex-boost && mkdir -p bin && cd bin && cmake -DCMAKE_POSITION_INDEPENDENT_CODE=ON .. && cmake --build .;

clean:
	rm -f $(BINARIES)
	cd ./lib/regex-boost && rm -rf bin;

list:
	@echo $(BINARIES)

.PHONY: clean list all libraries