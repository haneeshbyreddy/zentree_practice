CXX = g++
FLAGS = -std=c++20 -w
TARGET = build
INC = include
SRC = src
LIB = lib
OBJ = obj

all: ${TARGET}/p_lru

${TARGET}/p_lru: ${OBJ}/cache.o ${OBJ}/cache_example.o
	@${CXX} ${FLAGS} -I ${INC} ${OBJ}/cache.o ${OBJ}/cache_example.o -o ${TARGET}/p_lru
	${TARGET}/p_lru

${OBJ}/cache.o: ${LIB}/cache.cpp ${INC}/cache.h
	@${CXX} ${FLAGS} -I ${INC} -c ${LIB}/cache.cpp -o ${OBJ}/cache.o

${OBJ}/cache_example.o: ${SRC}/cache_example.cpp ${INC}/cache.h
	@${CXX} ${FLAGS} -I ${INC} -c ${SRC}/cache_example.cpp -o ${OBJ}/cache_example.o

clean:
	@rm -rf ${OBJ}/*.o ${TARGET}/build
