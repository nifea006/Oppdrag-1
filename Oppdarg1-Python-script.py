import platform

def get_basic_system_info():
    """Retrieves and prints basic system information."""
    system_info = platform.uname()
    print("--- Basic System Information ---")
    print(f"System: {system_info.system}")
    print(f"Node Name: {system_info.node}")
    print(f"Release: {system_info.release}")
    print(f"Version: {system_info.version}")
    print(f"Machine: {system_info.machine}")
    print(f"Processor: {system_info.processor}")

get_basic_system_info()