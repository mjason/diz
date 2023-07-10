import pkg_resources

# 加载入口点
entry_points = pkg_resources.get_entry_map('diz', 'console_scripts')

# 调用命令
command_name = 'diz'
if command_name in entry_points:
    command = entry_points[command_name].load()
    command()
else:
    print(f"Command '{command_name}' not found.")
