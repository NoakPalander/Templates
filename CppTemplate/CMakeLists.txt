cmake_minimum_required(VERSION 3.8)

# Overall properties used by cmake or doxygen
set(PROJECT_NAME <ENTER A PROJECT NAME>)
set(PROJECT_VERSION <ENTER A VERSION>)
set(PROJECT_BRIEF <BRIEF DESCRIPTION>)

project(${PROJECT_NAME})

# Includes the cmake-doxygen configuration
include(${CMAKE_SOURCE_DIR}/docs/CMakeLists.txt)

# Includes the external dependencies
include(${CMAKE_SOURCE_DIR}/ext/CMakeLists.txt)

add_executable(${PROJECT_NAME}
    src/Main.cpp)

# C++20
target_compile_features(${PROJECT_NAME} PRIVATE cxx_std_20)

# Debug mode, harder warnings, sanitizers and debug logs
if (CMAKE_BUILD_TYPE MATCHES "Debug")
    message("Configuring debug mode")

    target_compile_definitions(${PROJECT_NAME} PRIVATE DEBUG)
    target_compile_options(${PROJECT_NAME} PRIVATE -Wall -Wextra -pedantic-errors -O0 -g -fsanitize=undefined,leak,address)
    target_link_options(${PROJECT_NAME} PRIVATE -fsanitize=undefined,leak,address)

# Release mode, optimizations
elseif(CMAKE_BUILD_TYPE MATCHES "Release")
    message("Configuring release mode")

    target_compile_definitions(${PROJECT_NAME} PRIVATE RELEASE)
    target_compile_options(${PROJECT_NAME} PRIVATE -O3 -Wpedantic)
endif()

target_link_libraries(${PROJECT_NAME} PRIVATE
    pthread
    fmt::fmt)

