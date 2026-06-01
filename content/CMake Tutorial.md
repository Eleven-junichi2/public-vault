---
categories:
  - LiteratureNote
title: CMake Tutorial
source:
  - https://cmake.org/cmake/help/latest/guide/tutorial/index.html
author:
shelf:
tags:
ISBN:
publish: true
---

## 目次

- [Step 0: Before You Begin](https://cmake.org/cmake/help/latest/guide/tutorial/Before%20You%20Begin.html) 10m
    - [Getting the Tutorial Exercises](https://cmake.org/cmake/help/latest/guide/tutorial/Before%20You%20Begin.html#getting-the-tutorial-exercises)
    - [Getting CMake](https://cmake.org/cmake/help/latest/guide/tutorial/Before%20You%20Begin.html#getting-cmake)
    - [CMake Generators](https://cmake.org/cmake/help/latest/guide/tutorial/Before%20You%20Begin.html#cmake-generators)
    - [Single and Multi-Configuration Generators](https://cmake.org/cmake/help/latest/guide/tutorial/Before%20You%20Begin.html#single-and-multi-configuration-generators)
    - [Other Usage Basics](https://cmake.org/cmake/help/latest/guide/tutorial/Before%20You%20Begin.html#other-usage-basics)
    - [Try It Out](https://cmake.org/cmake/help/latest/guide/tutorial/Before%20You%20Begin.html#try-it-out)
    - [Getting Help and Additional Resources](https://cmake.org/cmake/help/latest/guide/tutorial/Before%20You%20Begin.html#getting-help-and-additional-resources)
- [Step 1: Getting Started with CMake](https://cmake.org/cmake/help/latest/guide/tutorial/Getting%20Started%20with%20CMake.html)
    - [Background](https://cmake.org/cmake/help/latest/guide/tutorial/Getting%20Started%20with%20CMake.html#background)
    - [Exercise 1 - Building an Executable](https://cmake.org/cmake/help/latest/guide/tutorial/Getting%20Started%20with%20CMake.html#exercise-1-building-an-executable)
    - [Exercise 2 - Building a Library](https://cmake.org/cmake/help/latest/guide/tutorial/Getting%20Started%20with%20CMake.html#exercise-2-building-a-library)
    - [Exercise 3 - Linking Together Libraries and Executables](https://cmake.org/cmake/help/latest/guide/tutorial/Getting%20Started%20with%20CMake.html#exercise-3-linking-together-libraries-and-executables)
    - [Exercise 4 - Subdirectories](https://cmake.org/cmake/help/latest/guide/tutorial/Getting%20Started%20with%20CMake.html#exercise-4-subdirectories)
- [Step 2: CMake Language Fundamentals](https://cmake.org/cmake/help/latest/guide/tutorial/CMake%20Language%20Fundamentals.html)
    - [Background](https://cmake.org/cmake/help/latest/guide/tutorial/CMake%20Language%20Fundamentals.html#background)
    - [Exercise 1 - Macros, Functions, and Lists](https://cmake.org/cmake/help/latest/guide/tutorial/CMake%20Language%20Fundamentals.html#exercise-1-macros-functions-and-lists)
    - [Exercise 2 - Conditionals and Loops](https://cmake.org/cmake/help/latest/guide/tutorial/CMake%20Language%20Fundamentals.html#exercise-2-conditionals-and-loops)
    - [Exercise 3 - Organizing with Include](https://cmake.org/cmake/help/latest/guide/tutorial/CMake%20Language%20Fundamentals.html#exercise-3-organizing-with-include)
- [Step 3: Configuration and Cache Variables](https://cmake.org/cmake/help/latest/guide/tutorial/Configuration%20and%20Cache%20Variables.html)
    - [Background](https://cmake.org/cmake/help/latest/guide/tutorial/Configuration%20and%20Cache%20Variables.html#background)
    - [Exercise 1 - Using Options](https://cmake.org/cmake/help/latest/guide/tutorial/Configuration%20and%20Cache%20Variables.html#exercise-1-using-options)
    - [Exercise 2 - `CMAKE` Variables](https://cmake.org/cmake/help/latest/guide/tutorial/Configuration%20and%20Cache%20Variables.html#exercise-2-cmake-variables)
    - [Exercise 3 - CMakePresets.json](https://cmake.org/cmake/help/latest/guide/tutorial/Configuration%20and%20Cache%20Variables.html#exercise-3-cmakepresets-json)
- [Step 4: In-Depth CMake Target Commands](https://cmake.org/cmake/help/latest/guide/tutorial/In-Depth%20CMake%20Target%20Commands.html)
    - [Background](https://cmake.org/cmake/help/latest/guide/tutorial/In-Depth%20CMake%20Target%20Commands.html#background)
    - [Exercise 1 - Features and Definitions](https://cmake.org/cmake/help/latest/guide/tutorial/In-Depth%20CMake%20Target%20Commands.html#exercise-1-features-and-definitions)
    - [Exercise 2 - Compile and Link Options](https://cmake.org/cmake/help/latest/guide/tutorial/In-Depth%20CMake%20Target%20Commands.html#exercise-2-compile-and-link-options)
    - [Exercise 3 - Include and Link Directories](https://cmake.org/cmake/help/latest/guide/tutorial/In-Depth%20CMake%20Target%20Commands.html#exercise-3-include-and-link-directories)
- [Step 5: In-Depth CMake Library Concepts](https://cmake.org/cmake/help/latest/guide/tutorial/In-Depth%20CMake%20Library%20Concepts.html)
    - [Background](https://cmake.org/cmake/help/latest/guide/tutorial/In-Depth%20CMake%20Library%20Concepts.html#background)
    - [Exercise 1 - Static and Shared](https://cmake.org/cmake/help/latest/guide/tutorial/In-Depth%20CMake%20Library%20Concepts.html#exercise-1-static-and-shared)
    - [Exercise 2 - Interface Libraries](https://cmake.org/cmake/help/latest/guide/tutorial/In-Depth%20CMake%20Library%20Concepts.html#exercise-2-interface-libraries)
    - [Exercise 3 - Object Libraries](https://cmake.org/cmake/help/latest/guide/tutorial/In-Depth%20CMake%20Library%20Concepts.html#exercise-3-object-libraries)
- [Step 6: In-Depth System Introspection](https://cmake.org/cmake/help/latest/guide/tutorial/In-Depth%20System%20Introspection.html)
    - [Background](https://cmake.org/cmake/help/latest/guide/tutorial/In-Depth%20System%20Introspection.html#background)
    - [Exercise 1 - Check Include File](https://cmake.org/cmake/help/latest/guide/tutorial/In-Depth%20System%20Introspection.html#exercise-1-check-include-file)
    - [Exercise 2 - Check Source Compiles](https://cmake.org/cmake/help/latest/guide/tutorial/In-Depth%20System%20Introspection.html#exercise-2-check-source-compiles)
    - [Exercise 3 - Check Interprocedural Optimization](https://cmake.org/cmake/help/latest/guide/tutorial/In-Depth%20System%20Introspection.html#exercise-3-check-interprocedural-optimization)
- [Step 7: Custom Commands and Generated Files](https://cmake.org/cmake/help/latest/guide/tutorial/Custom%20Commands%20and%20Generated%20Files.html)
    - [Background](https://cmake.org/cmake/help/latest/guide/tutorial/Custom%20Commands%20and%20Generated%20Files.html#background)
    - [Exercise 1 - Using a Code Generator](https://cmake.org/cmake/help/latest/guide/tutorial/Custom%20Commands%20and%20Generated%20Files.html#exercise-1-using-a-code-generator)
- [Step 8: Testing and CTest](https://cmake.org/cmake/help/latest/guide/tutorial/Testing%20and%20CTest.html)
    - [Background](https://cmake.org/cmake/help/latest/guide/tutorial/Testing%20and%20CTest.html#background)
    - [Exercise 1 - Adding Tests](https://cmake.org/cmake/help/latest/guide/tutorial/Testing%20and%20CTest.html#exercise-1-adding-tests)
- [Step 9: Installation Commands and Concepts](https://cmake.org/cmake/help/latest/guide/tutorial/Installation%20Commands%20and%20Concepts.html)
    - [Background](https://cmake.org/cmake/help/latest/guide/tutorial/Installation%20Commands%20and%20Concepts.html#background)
    - [Exercise 1 - Installing Artifacts](https://cmake.org/cmake/help/latest/guide/tutorial/Installation%20Commands%20and%20Concepts.html#exercise-1-installing-artifacts)
    - [Exercise 2 - Exporting Targets](https://cmake.org/cmake/help/latest/guide/tutorial/Installation%20Commands%20and%20Concepts.html#exercise-2-exporting-targets)
    - [Exercise 3 - Exporting a Version File](https://cmake.org/cmake/help/latest/guide/tutorial/Installation%20Commands%20and%20Concepts.html#exercise-3-exporting-a-version-file)
- [Step 10: Finding Dependencies](https://cmake.org/cmake/help/latest/guide/tutorial/Finding%20Dependencies.html)
    - [Background](https://cmake.org/cmake/help/latest/guide/tutorial/Finding%20Dependencies.html#background)
    - [Exercise 1 - Using `find_package()`](https://cmake.org/cmake/help/latest/guide/tutorial/Finding%20Dependencies.html#exercise-1-using-find-package)
    - [Exercise 2 - Transitive Dependencies](https://cmake.org/cmake/help/latest/guide/tutorial/Finding%20Dependencies.html#exercise-2-transitive-dependencies)
    - [Exercise 3 - Finding Other Kinds of Files](https://cmake.org/cmake/help/latest/guide/tutorial/Finding%20Dependencies.html#exercise-3-finding-other-kinds-of-files)
- [Step 11: Miscellaneous Features](https://cmake.org/cmake/help/latest/guide/tutorial/Miscellaneous%20Features.html)
    - [Exercise 1: Target Aliases](https://cmake.org/cmake/help/latest/guide/tutorial/Miscellaneous%20Features.html#exercise-1-target-aliases)
    - [Exercise 2: Generator Expressions](https://cmake.org/cmake/help/latest/guide/tutorial/Miscellaneous%20Features.html#exercise-2-generator-expressions)
    