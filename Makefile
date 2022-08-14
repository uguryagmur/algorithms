INC="/home/adm1n/Shop/googletest/googletest/include/gtest"


install:
	g++ -pthread -lgtest_main  -lgtest -lpthread test_tree.cc binary_tree.cc -I $(INC) -o program.o

clean:
	rm binary_tree.o program.o
