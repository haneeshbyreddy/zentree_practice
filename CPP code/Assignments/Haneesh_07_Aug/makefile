CXX = g++
FLAGS = -std=c++20 -w
SRC = src
INC = include
TARGET = build
FILES = election_winner equal_01 license_formating modified_string string_rotation 

all: ${FILES}

election_winner:
	@${CXX} ${FLAGS} ${SRC}/election_winner.cpp -o ${TARGET}/election_winner -I ${INC}; \
	./${TARGET}/election_winner

equal_01:
	@${CXX} ${FLAGS} ${SRC}/equal_01.cpp -o ${TARGET}/equal_01 -I ${INC}; \
	./${TARGET}/equal_01

license_formating:
	@${CXX} ${FLAGS} ${SRC}/license_formating.cpp -o ${TARGET}/license_formating -I ${INC}; \
	./${TARGET}/license_formating

modified_string:
	@${CXX} ${FLAGS} ${SRC}/modified_string.cpp -o ${TARGET}/modified_string -I ${INC}; \
	./${TARGET}/modified_string

string_rotation:
	@${CXX} ${FLAGS} ${SRC}/string_rotation.cpp -o ${TARGET}/string_rotation -I ${INC}; \
	./${TARGET}/string_rotation

clean:
	rm -rf ${TARGET}/*