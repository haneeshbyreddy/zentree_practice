CXX = g++
STANDARD_FLAGS = -std=c++20 -w
DEBUG_FLAGS = -g
Target = build
SRC = src
OBJ = obj
INC = include
LIB = lib

ifdef DEBUG
    FLAG = $(STANDARD_FLAGS) $(DEBUG_FLAGS)
else
    FLAG = $(STANDARD_FLAGS)
endif

all: heap_example linked_list_example

heap_example: .heap
	@name=heap_example; \
	${CXX} ${FLAG} -I ${INC} -c ${SRC}/$${name}.cpp -o ${OBJ}/$${name}.o; \
	${CXX} ${FLAG} ${OBJ}/$${name}.o ${OBJ}/heap.o -o ${Target}/$${name}; \
	${Target}/$${name};

linked_list_example: .linked_list
	@name=linked_list_example; \
	${CXX} ${FLAG} -I ${INC} -c ${SRC}/$${name}.cpp -o ${OBJ}/$${name}.o; \
	${CXX} ${FLAG} ${OBJ}/$${name}.o ${OBJ}/linked_list.o -o ${Target}/$${name}; \
	${Target}/$${name};

.stack:
	@name=stack; \
	${CXX} ${FLAG} -I ${INC} -c ${SRC}/$${name}.cpp -o ${OBJ}/$${name}.o;

.linked_list: 
	@name=linked_list; \
	${CXX} ${FLAG} -I ${INC} -c ${LIB}/$${name}.cpp -o ${OBJ}/$${name}.o;

.heap: 
	@name=heap; \
	${CXX} ${FLAG} -I ${INC} -c ${LIB}/$${name}.cpp -o ${OBJ}/$${name}.o;

.double_linked_list: 
	@name=double_linked_list; \
	${CXX} ${FLAG} -I ${INC} -c ${LIB}/$${name}.cpp -o ${OBJ}/$${name}.o;

.queue: 
	@name=queue; \
	${CXX} ${FLAG} -I ${INC} -c ${SRC}/$${name}.cpp -o ${OBJ}/$${name}.o;

clean:
	rm -rf ${Target}/*
	rm -rf ${OBJ}/*