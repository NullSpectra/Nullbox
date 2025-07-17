import shutil
import subprocess
from pathlib import Path

def clean_pyinstaller_artifacts():
    for folder in ["dist", "build"]:
        path = Path(folder)
        if path.exists():
            shutil.rmtree(path)
    for spec_file in Path('.').glob('*.spec'):
        spec_file.unlink()

def build_all_src():
    clean_pyinstaller_artifacts()
    for py_file in Path("src").glob("*.py"):
        subprocess.run(["pyinstaller", "--onefile", str(py_file)])

if __name__ == "__main__":
    build_all_src()
