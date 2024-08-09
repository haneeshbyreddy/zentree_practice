CXX = g++ -std=c++20 -w
TARGET = build/schedule_mettings
SRC = src/*
OBJ = obj/*
INCDIR = inc

all: $(TARGET)

$(TARGET): compile
	$(CXX) $(OBJ) -o $(TARGET)
	./${TARGET}

compile:
	$(CXX) -c $(SRC) -I ${INCDIR}
	mv *.o obj

clean:
	rm -f $(TARGET) $(OBJ)