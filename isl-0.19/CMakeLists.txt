cmake_minimum_required(VERSION 2.8)

project(Isl)
include_directories(. include imath_wrap)
file(GLOB ISL_SRC 
	isl_imath.c
	isl_val_imath.c
	isl_int_imath.c
	isl_aff.c
	isl_affine_hull.c
	isl_arg.c
	isl_ast.c
	isl_ast_build.c
	isl_ast_build_expr.c
	isl_ast_codegen.c
	isl_ast_graft.c
	basis_reduction_tab.c
	isl_bernstein.c
	isl_blk.c
	isl_bound.c
	isl_coalesce.c
	isl_constraint.c
	isl_convex_hull.c
	isl_ctx.c
	isl_deprecated.c
	isl_dim_map.c
	isl_equalities.c
	isl_factorization.c
	isl_farkas.c
	isl_ffs.c
	isl_flow.c
	isl_fold.c
	isl_hash.c
	isl_id_to_ast_expr.c
	isl_id_to_id.c
	isl_id_to_pw_aff.c
	isl_ilp.c
	isl_input.c
	isl_local.c
	isl_local_space.c
	isl_lp.c
	isl_map.c
	isl_map_list.c
	isl_map_simplify.c
	isl_map_subtract.c
	isl_map_to_basic_set.c
	isl_mat.c
	isl_morph.c
	isl_id.c
	isl_obj.c
	isl_options.c
	isl_output.c
	isl_point.c
	isl_polynomial.c
	isl_printer.c
	print.c
	isl_range.c
	isl_reordering.c
	isl_sample.c
	isl_scan.c
	isl_schedule.c
	isl_schedule_band.c
	isl_schedule_node.c
	isl_schedule_read.c
	isl_schedule_tree.c
	isl_schedule_constraints.c
	isl_scheduler.c
	isl_set_list.c
	isl_sort.c
	isl_space.c
	isl_stream.c
	isl_seq.c
	isl_stride.c
	isl_tab.c
	isl_tab_pip.c
	isl_tarjan.c
	isl_transitive_closure.c
	isl_union_map.c
	isl_val.c
	isl_vec.c
	isl_version.c
	isl_vertices.c
	isl_ffs.c
    imath_wrap/*.c)

add_library(${PROJECT_NAME} ${ISL_SRC})
add_executable(islcodegen codegen.c)
add_executable(isltest isl_test.c)
add_executable(isltestimath isl_test_imath.c)
add_executable(isltestint isl_test_int.c)
add_executable(islbound bound.c)
add_executable(islflow flow.c)
add_executable(islflowcmp flow_cmp.c)
add_executable(islschedule schedule.c)
add_executable(islschedulecmp schedule_cmp.c)
add_executable(islpip pip.c)

if(WIN32)
   target_link_libraries(islcodegen ${PROJECT_NAME})
   target_link_libraries(isltest ${PROJECT_NAME})
   target_link_libraries(isltestimath ${PROJECT_NAME})
   target_link_libraries(isltestint ${PROJECT_NAME})
   target_link_libraries(islbound ${PROJECT_NAME})
   target_link_libraries(islflow ${PROJECT_NAME})
   target_link_libraries(islflowcmp ${PROJECT_NAME})
   target_link_libraries(islschedule ${PROJECT_NAME})
   target_link_libraries(islschedulecmp ${PROJECT_NAME})
   target_link_libraries(islpip ${PROJECT_NAME})
else()
   target_link_libraries(islcodegen ${PROJECT_NAME} -lm)
   target_link_libraries(isltest ${PROJECT_NAME} -lm)
   target_link_libraries(isltestimath ${PROJECT_NAME} -lm)
   target_link_libraries(isltestint ${PROJECT_NAME} -lm)
   target_link_libraries(islbound ${PROJECT_NAME} -lm)
   target_link_libraries(islflow ${PROJECT_NAME} -lm)
   target_link_libraries(islflowcmp ${PROJECT_NAME} -lm)
   target_link_libraries(islschedule ${PROJECT_NAME} -lm)
   target_link_libraries(islschedulecmp ${PROJECT_NAME} -lm)
   target_link_libraries(islpip ${PROJECT_NAME} -lm)
endif()
