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

graph_example: .graph ${SRC}/graph_example.cpp
	@name=graph_example; \
	${CXX} ${FLAG} -I ${INC} -c ${SRC}/$${name}.cpp -o ${OBJ}/$${name}.o; \
	${CXX} ${FLAG} ${OBJ}/$${name}.o ${OBJ}/graph.o -o ${Target}/$${name}; \

hash_example: .hash ${SRC}/hash_example.cpp
	@name=hash_example; \
	${CXX} ${FLAG} -I ${INC} -c ${SRC}/$${name}.cpp -o ${OBJ}/$${name}.o; \
	${CXX} ${FLAG} ${OBJ}/$${name}.o ${OBJ}/hash.o -o ${Target}/$${name}; \

double_linked_example: .double_linked_list ${SRC}/double_linked_example.cpp
	@name=double_linked_example; \
	${CXX} ${FLAG} -I ${INC} -c ${SRC}/$${name}.cpp -o ${OBJ}/$${name}.o; \
	${CXX} ${FLAG} ${OBJ}/$${name}.o ${OBJ}/double_linked_list.o -o ${Target}/$${name}; \

tree_example: .tree ${SRC}/tree_example.cpp
	@name=tree_example; \
	${CXX} ${FLAG} -I ${INC} -c ${SRC}/$${name}.cpp -o ${OBJ}/$${name}.o; \
	${CXX} ${FLAG} ${OBJ}/$${name}.o ${OBJ}/tree.o -o ${Target}/$${name}; \

stack_example: .stack ${SRC}/stack_example.cpp
	@name=stack_example; \
	${CXX} ${FLAG} -I ${INC} -c ${SRC}/$${name}.cpp -o ${OBJ}/$${name}.o; \
	${CXX} ${FLAG} ${OBJ}/$${name}.o ${OBJ}/stack.o -o ${Target}/$${name}; \

queue_example: .queue ${SRC}/queue_example.cpp
	@name=queue_example; \
	${CXX} ${FLAG} -I ${INC} -c ${SRC}/$${name}.cpp -o ${OBJ}/$${name}.o; \
	${CXX} ${FLAG} ${OBJ}/$${name}.o ${OBJ}/queue.o -o ${Target}/$${name}; \

heap_example: .heap ${SRC}/heap_example.cpp
	@name=heap_example; \
	${CXX} ${FLAG} -I ${INC} -c ${SRC}/$${name}.cpp -o ${OBJ}/$${name}.o; \
	${CXX} ${FLAG} ${OBJ}/$${name}.o ${OBJ}/heap.o -o ${Target}/$${name}; \

linked_list_example: .linked_list ${SRC}/linked_list_example.cpp
	name=linked_list_example; \
	${CXX} ${FLAG} -I ${INC} -c ${SRC}/$${name}.cpp -o ${OBJ}/$${name}.o; \
	${CXX} ${FLAG} ${OBJ}/$${name}.o ${OBJ}/linked_list.o -o ${Target}/$${name}; \

.tree: ${LIB}/tree.cpp
	@${CXX} ${FLAG} -I ${INC} -c $< -o ${OBJ}/tree.o;

.stack: ${LIB}/stack.cpp
	@${CXX} ${FLAG} -I ${INC} -c $< -o ${OBJ}/stack.o;

.linked_list: ${LIB}/linked_list.cpp
	${CXX} ${FLAG} -I ${INC} -c $< -o ${OBJ}/linked_list.o;

.heap: ${LIB}/heap.cpp
	@${CXX} ${FLAG} -I ${INC} -c $< -o ${OBJ}/heap.o;

.double_linked_list: ${LIB}/double_linked_list.cpp
	@${CXX} ${FLAG} -I ${INC} -c $< -o ${OBJ}/double_linked_list.o;

.queue: ${LIB}/queue.cpp
	@${CXX} ${FLAG} -I ${INC} -c $< -o ${OBJ}/queue.o;
	
.hash: ${LIB}/hash.cpp
	@${CXX} ${FLAG} -I ${INC} -c $< -o ${OBJ}/hash.o;

.graph: ${LIB}/graph.cpp
	@${CXX} ${FLAG} -I ${INC} -c $< -o ${OBJ}/graph.o;

clean:
	rm -rf ${Target}/*
	rm -rf ${OBJ}/*