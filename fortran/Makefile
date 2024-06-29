FFLAGS = -O3 -Wall -Wextra -Wpedantic

SCRIPTS = $(wildcard **/*.f90)

BINARIES =  $(SCRIPTS:%.f90=%-gfortran) \
			$(SCRIPTS:%.f90=%-gfortran-static) \
			# $(SCRIPTS:%.f90=%-ifort) \
			# $(SCRIPTS:%.f90=%-ifort-static) \

%-gfortran: %.f90
	gfortran $(FFLAGS) -o $@ $<

%-gfortran-static: %.f90
	gfortran $(FFLAGS) -static -o $@ $<

%-ifort : %.f90
	ifort $(FFLAGS) -o $@ $<

%-ifort-static : %.f90
	ifort $(FFLAGS) -static -o $@ $<

all: $(BINARIES)

.PHONY: clean

clean:
	rm -f $(BINARIES)
