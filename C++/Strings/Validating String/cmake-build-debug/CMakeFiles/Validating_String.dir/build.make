# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.17

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Disable VCS-based implicit rules.
% : %,v


# Disable VCS-based implicit rules.
% : RCS/%


# Disable VCS-based implicit rules.
% : RCS/%,v


# Disable VCS-based implicit rules.
% : SCCS/s.%


# Disable VCS-based implicit rules.
% : s.%


.SUFFIXES: .hpux_make_needs_suffix_list


# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /Applications/CLion.app/Contents/bin/cmake/mac/bin/cmake

# The command to remove a file.
RM = /Applications/CLion.app/Contents/bin/cmake/mac/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = "/Users/shubhangigupta/Documents/GitHub/Data-Structures-and-Algorithms/C++/Strings/Validating String"

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = "/Users/shubhangigupta/Documents/GitHub/Data-Structures-and-Algorithms/C++/Strings/Validating String/cmake-build-debug"

# Include any dependencies generated for this target.
include CMakeFiles/Validating_String.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/Validating_String.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/Validating_String.dir/flags.make

CMakeFiles/Validating_String.dir/main.cpp.o: CMakeFiles/Validating_String.dir/flags.make
CMakeFiles/Validating_String.dir/main.cpp.o: ../main.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir="/Users/shubhangigupta/Documents/GitHub/Data-Structures-and-Algorithms/C++/Strings/Validating String/cmake-build-debug/CMakeFiles" --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/Validating_String.dir/main.cpp.o"
	/Library/Developer/CommandLineTools/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/Validating_String.dir/main.cpp.o -c "/Users/shubhangigupta/Documents/GitHub/Data-Structures-and-Algorithms/C++/Strings/Validating String/main.cpp"

CMakeFiles/Validating_String.dir/main.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/Validating_String.dir/main.cpp.i"
	/Library/Developer/CommandLineTools/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E "/Users/shubhangigupta/Documents/GitHub/Data-Structures-and-Algorithms/C++/Strings/Validating String/main.cpp" > CMakeFiles/Validating_String.dir/main.cpp.i

CMakeFiles/Validating_String.dir/main.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/Validating_String.dir/main.cpp.s"
	/Library/Developer/CommandLineTools/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S "/Users/shubhangigupta/Documents/GitHub/Data-Structures-and-Algorithms/C++/Strings/Validating String/main.cpp" -o CMakeFiles/Validating_String.dir/main.cpp.s

# Object files for target Validating_String
Validating_String_OBJECTS = \
"CMakeFiles/Validating_String.dir/main.cpp.o"

# External object files for target Validating_String
Validating_String_EXTERNAL_OBJECTS =

Validating_String: CMakeFiles/Validating_String.dir/main.cpp.o
Validating_String: CMakeFiles/Validating_String.dir/build.make
Validating_String: CMakeFiles/Validating_String.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir="/Users/shubhangigupta/Documents/GitHub/Data-Structures-and-Algorithms/C++/Strings/Validating String/cmake-build-debug/CMakeFiles" --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable Validating_String"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/Validating_String.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/Validating_String.dir/build: Validating_String

.PHONY : CMakeFiles/Validating_String.dir/build

CMakeFiles/Validating_String.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/Validating_String.dir/cmake_clean.cmake
.PHONY : CMakeFiles/Validating_String.dir/clean

CMakeFiles/Validating_String.dir/depend:
	cd "/Users/shubhangigupta/Documents/GitHub/Data-Structures-and-Algorithms/C++/Strings/Validating String/cmake-build-debug" && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" "/Users/shubhangigupta/Documents/GitHub/Data-Structures-and-Algorithms/C++/Strings/Validating String" "/Users/shubhangigupta/Documents/GitHub/Data-Structures-and-Algorithms/C++/Strings/Validating String" "/Users/shubhangigupta/Documents/GitHub/Data-Structures-and-Algorithms/C++/Strings/Validating String/cmake-build-debug" "/Users/shubhangigupta/Documents/GitHub/Data-Structures-and-Algorithms/C++/Strings/Validating String/cmake-build-debug" "/Users/shubhangigupta/Documents/GitHub/Data-Structures-and-Algorithms/C++/Strings/Validating String/cmake-build-debug/CMakeFiles/Validating_String.dir/DependInfo.cmake" --color=$(COLOR)
.PHONY : CMakeFiles/Validating_String.dir/depend

