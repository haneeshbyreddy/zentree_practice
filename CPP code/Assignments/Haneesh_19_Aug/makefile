CXX = c++ 
FLAGS = -std=c++20 -w
TARGET = build
INC = include
SRC = src
LIB = lib
OBJ = obj

all: ${TARGET}/linked_list

${TARGET}/linked_list: ${OBJ}/linked_list.o ${OBJ}/linked_list_example.o
	${CXX} ${FLAGS} -I ${INC} ${OBJ}/linked_list.o ${OBJ}/linked_list_example.o -o ${TARGET}/linked_list
	./${TARGET}/linked_list

${OBJ}/linked_list.o: ${LIB}/linked_list.cpp
	${CXX} ${FLAGS} -I ${INC} -c ${LIB}/linked_list.cpp -o ${OBJ}/linked_list.o

${OBJ}/linked_list_example.o: ${SRC}/linked_list_example.cpp
	${CXX} ${FLAGS} -I ${INC} -c ${SRC}/linked_list_example.cpp -o ${OBJ}/linked_list_example.o

clean:
	rm -f ${OBJ}/*.o ${TARGET}/linked_list
