CXX = c++
STANDARD_FLAGS = -std=c++20 -w
DEBUG_FLAGS = -g
TARGET = build
LIB = lib
OBJ = obj
SRC = src
INC = include

ifdef DEBUG
	FLAGS = ${STANDARD_FLAGS} ${DEBUG_FLAGS}
else
	FLAGS = ${STANDARD_FLAGS}
endif


all: ${TARGET}/double_linked_list

${TARGET}/double_linked_list: ${OBJ}/double_linked_list.o ${OBJ}/double_linked_list_example.o
	${CXX} ${FLAGS} -I ${INC} ${OBJ}/double_linked_list.o ${OBJ}/double_linked_list_example.o -o ${TARGET}/double_linked_list_example 

${OBJ}/double_linked_list.o: ${LIB}/double_linked_list.cpp
	${CXX} ${FLAGS} -I ${INC} -c ${LIB}/double_linked_list.cpp -o ${OBJ}/double_linked_list.o

${OBJ}/double_linked_list_example.o: ${SRC}/double_linked_list_example.cpp
	${CXX} ${FLAGS} -I ${INC} -c ${SRC}/double_linked_list_example.cpp -o ${OBJ}/double_linked_list_example.o

clean:
	rm -f ${OBJ}/* ${TARGET}/*