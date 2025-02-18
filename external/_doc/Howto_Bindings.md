# Folders structure

## binding_generations/
bindings_generations/ holds generation scripts and utilities:

```
bindings_generation/
├── __init__.py
├── external_library.py                  # Describes a bound external library
├── all_external_libraries.py            # List of all libraries
├── autogenerate_all.py                  # will generate all C++ bindings and python stubs (as well as all_pybind_files.cmake) 
├── cpp/
│         ├── all_pybind_files.cmake     # this file is autogenerated and used by the main cmake
│         ├── module.cpp                 # main pybind11 module
│         └── pybind_imgui_bundle.cpp    # manual c++ files that gather all modules
├── paths.py
├── sandbox.py
├── shell_commands.py
└── update_libs.py
```

## Typical bound library structure:

The basic structure for a bound library is as shown below:

```
external/imgui-knobs/                        # Base library folder
│                                            # this folder name should reflect the real name of the library
│                                            # (the generated python module name will be converted to snake case, 
│                                            #  and "-" will be replaced by "_", so that the python module will be imgui_knobs
|
│
├── external/imgui-knobs/imgui-knobs/        # A git submodule that holds the library code 
│    ├── LICENSE                             
│    ├── README.md
│    ├── imgui-knobs.cpp
│    └── imgui-knobs.h
├── external/imgui-knobs/bindings/            # Python binding utilities
│         ├── generate_imgui_knobs.py         # a script with options to autogenerate the library
│         │
│         ├── imgui_knobs.pyi -> ../../../bindings/imgui_bundle/imgui_knobs.pyi  
│         │                                     # an optional symlink to the autogenerated python stubs 
│         │
│         └── pybind_imgui_knobs.cpp          # autogenerated C++ to python bindings
binding/imgui_bundle/
            └── imgui-knobs.himgui_knobs.pyi  # autogenerated python stubs
```


For a more complex library, it may look like:

```
imgui_md/                              # Base library folder
├── assets/                            
│         ├── ...
├── bindings/                         # Python binding utilities
│         ├── generate_imgui_md.py
│         ├── imgui_md.pyi -> ../../../bindings/imgui_bundle/imgui_md.pyi
│         └── pybind_imgui_md.cpp
├── imgui_md/                         # A git submodule that holds the library code
│         ├── ...
├── imgui_md_wrapper/                 # Manually written wrapper to ease python bindings
│         ├── imgui_md_wrapper.cpp
│         └── imgui_md_wrapper.h
└── md4c/                             # additional submodule required by the lib
    ├── ...
```


# How to add a new bound libray

This is an example, based on the lib imgui-command-palette, which will be added as a python module `imgui_command_palette`

See commit ["Add imgui_command_palette"](https://github.com/pthom/imgui_bundle/commit/1e52b3c992dac890b5b13dc2dacd81446e944050)

### Optional: fork the library and add a branch imgui_bundle

### Register your library inside `all_external_libraries.py` 

Edit [bindings_generation/all_external_libraries.py](../bindings_generation/all_external_libraries.py) 
and add your library, then modify `ALL_LIBS`

Example:

```python
def lib_imgui_command_palette() -> ExternalLibrary:
    return ExternalLibrary(
        name="imgui-command-palette",
        official_git_url="https://github.com/hnOsmium0001/imgui-command-palette.git",
        official_branch="master",
        fork_git_url="https://github.com/pthom/imgui-command-palette.git"
    )
```

### Add the lib as a submodule

```
git submodule add -b imgui_bundle https://github.com/pthom/imgui-command-palette.git external/imgui-command-palette/imgui-command-palette
```

### Create bindings scripts, prepare bindings and stubs file

```bash
# Create bindings/ folder
mkdir external/imgui-command-palette/bindings

# Copy generate script and cpp pydef file from an example
cp external/imgui-knobs/bindings/generate_imgui_knobs.py external/imgui-command-palette/bindings/generate_imgui_command_palette.py 
cp external/imgui-knobs/bindings/pybind_imgui_knobs.cpp external/imgui-command-palette/bindings/pybind_imgui_command_palette.cpp

# Copy stubs from an example
cp bindings/imgui_bundle/imgui_knobs.pyi bindings/imgui_bundle/imgui_command_palette.pyi

# optional: add stub symlink
cd external/imgui-command-palette/bindings
ln -s ../../../bindings/imgui_bundle/imgui_command_palette.pyi
 ```

Edit pybind_imgui_command_palette.cpp: remove code related to imgui-knobs
Edit imgui_command_palette.pyi: remove code related to imgui-knobs

### Add your library inside external/CMakeLists.txt

### Add your library inside "external/bindings_generation/cpp/all_pybind_files.cmake"
(Or you can run external/bindings_generation/autogenerate_all.py which will add it also)

### Edit and adapt `generate_imgui_command_palette.py`, then run it and test the compilation
Refer to litgen documentation (see litgen/options.py).
You will also need to adapt pybind_imgui_command_palette.cpp

### Edit bindings/imgui_bundle/__init__.py and bindings/imgui_bundle/__init__.pyi
Add references to imgui_command_palette

### Edit external/bindings_generation/cpp/pybind_imgui_bundle.cpp
Add references to imgui_command_palette

### Add demos inside bindings/imgui_bundle/demos_cpp and bindings/imgui_bundle/demos_python
