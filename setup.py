import cx_Freeze

executables = [cx_Freeze.Executable(
    script="jogo.py", icon="assets/icone.ico")]
cx_Freeze.setup(
    name="Coleta Seletiva Divertida",
    options={
        "build_exe": {
            "packages": ["pygame"],
            "include_files": ["assets"]
        }},
    executables=executables
)