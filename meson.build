project('hwm14', 'fortran', default_options : ['default_library=static'])

fc = meson.get_compiler('fortran')
if fc.get_id() == 'gcc'
  add_project_arguments('-Wall', '-march=native', '-Wline-truncation', '-Werror=array-bounds', language: 'fortran')
endif

hwm_exe = executable('hwm', 'src/hwm14.f90', 'src/checkhwm14.f90')
test('HMW93', hwm_exe)

#if 'UNIX'
# test('NAME', 'compareHWM14', 'COMMAND', 'bash', '-c', '$<TARGET_FILE:hwm> | diff - ${CMAKE_CURRENT_SOURCE_DIR}/tests/test.log')
#endif
