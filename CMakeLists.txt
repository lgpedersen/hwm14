cmake_minimum_required(VERSION 3.7)
project(hwm14 Fortran)
enable_testing()

if(${CMAKE_Fortran_COMPILER_ID} STREQUAL GNU)
  add_compile_options(-Wall -march=native -Wline-truncation -Werror=array-bounds)
endif()

add_executable(hwm src/checkhwm14.f90 src/hwm14.f90)
add_test(NAME HMW14 COMMAND hwm)

set(DATA_FILES
  hwm123114.bin
  dwm07b104i.dat
  gd2qd.dat)

foreach(file ${DATA_FILES})
  file(COPY "${CMAKE_SOURCE_DIR}/src/${file}" DESTINATION "${CMAKE_BINARY_DIR}/")
endforeach()

if(UNIX)
  add_test(NAME compareHWM14
      COMMAND bash -c "$<TARGET_FILE:hwm> | diff - ${CMAKE_CURRENT_SOURCE_DIR}/tests/test.log")
endif()
