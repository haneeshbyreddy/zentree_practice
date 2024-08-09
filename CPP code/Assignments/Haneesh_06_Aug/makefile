CXX = g++ -std=c++20 -w
SRC = src 
INC = include
TARGET = build

all: array_duplicates majority_element array_leader count_inversion array_search

array_duplicates: 
	${CXX} src/array_duplicates.cpp -o ${TARGET}/array_duplicates -I ${INC}
	@echo "array_duplicates"
	./${TARGET}/array_duplicates

majority_element:
	${CXX} src/majority_element.cpp -o ${TARGET}/majority_element -I ${INC}
	@echo "majority_element"
	./${TARGET}/majority_element

array_leader:
	${CXX} src/array_leader.cpp -o ${TARGET}/array_leader -I ${INC}
	@echo "array_leader"
	./${TARGET}/array_leader

count_inversion:
	${CXX} src/count_inversion.cpp -o ${TARGET}/count_inversion -I ${INC}
	@echo "count_inversion"
	./${TARGET}/count_inversion

array_search:
	${CXX} src/array_search.cpp -o ${TARGET}/array_search -I ${INC}
	@echo "array_search"
	./${TARGET}/array_search

clean:
	rm ${TARGET}/*