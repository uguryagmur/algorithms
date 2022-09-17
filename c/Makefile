build_test: graph.o
	cc test/test_graph.c build/graph.o -o build/test/test_graph.o

graph.o: create_dirs
	cc -c src/graph.c -o build/graph.o

create_dirs:
	if [ -d ./build ]; then if [[ ! -d ./build/test ]]; then mkdir build/test; fi; else mkdir build; mkdir build/test; fi

clean:
	rm -rf ./build

