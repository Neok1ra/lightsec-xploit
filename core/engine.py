def run_module(module_name, target):
    try:
        mod = __import__(f'modules.{module_name}', fromlist=[''])
        mod.run(target)
    except Exception as e:
        print(f"[!] Failed to run module {module_name}: {e}")
