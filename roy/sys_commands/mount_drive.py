import subprocess


def mount_me(driver: str) -> None:
    subprocess.run(["sudo", "mount", "-t", "ntfs-3g", "/dev/sda7", "/media/data"])
