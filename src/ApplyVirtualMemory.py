import ctypes
import psutil
import winreg as reg
from colorama import Fore, Back, Style, init

def get_system_ram():
    total_ram = psutil.virtual_memory().total
    return total_ram // (1024 * 1024)

def calculate_optimal_vram(ram_mb):
    min_vram = ram_mb * 1.5
    max_vram = ram_mb * 3
    return int(min_vram), int(max_vram)

def set_virtual_memory(min_vram_mb, max_vram_mb):
    """Setzen Sie die virtuellen Speichereinstellungen in der Windows-Registrierung."""
    reg_path = r"SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management"
    
    with reg.OpenKey(reg.HKEY_LOCAL_MACHINE, reg_path, 0, reg.KEY_SET_VALUE) as key:
        reg.SetValueEx(key, "PagingFiles", 0, reg.REG_MULTI_SZ, [f"C:\\pagefile.sys {min_vram_mb} {max_vram_mb}"])

    ctypes.windll.kernel32.SetSystemFileCacheSize(min_vram_mb, max_vram_mb, 1)
    ctypes.windll.kernel32.SetSystemFileCacheSize(0, 0, 0)

def Performance():
    init()
    ram_mb= get_system_ram()
    min_vram, max_vram = calculate_optimal_vram(ram_mb)
    set_virtual_memory(min_vram, max_vram)
    print(f"{Fore.LIGHTGREEN_EX}[COMPLETED 3/3]{Style.RESET_ALL} Allocated Virtual Memory For Performance : {Fore.YELLOW}{min_vram}MB {Style.RESET_ALL}- {Fore.YELLOW}{max_vram}MB{Style.RESET_ALL}")
