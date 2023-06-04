from pathlib import Path

path=Path("begining1")
new_dir= Path("email")
print(path.exists())
#print(new_dir.mkdir())
print(new_dir.exists())
print(new_dir.rmdir())