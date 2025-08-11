import subprocess
import sys
import os

print("🌟 subprocess 模块练习大全 🌟\n")
print(f"Python 路径: {sys.executable}")
print("-" * 50)

# ==================== 示例 1：运行 ping 命令 ====================
print("1. 🌐 运行 ping 命令（检测网络）")
try:
    # Windows 用 -n，Mac/Linux 用 -c
    if os.name == 'nt':  # Windows
        cmd = ['ping', '-n', '4', 'www.baidu.com']
    else:  # Mac/Linux
        cmd = ['ping', '-c', '4', 'www.baidu.com']

    result = subprocess.run(cmd, capture_output=True, text=True)

    print(f"命令: {' '.join(cmd)}")
    print(f"返回码: {result.returncode} (0 表示成功)")

    if result.returncode == 0:
        print("✅ ping 成功！前几行输出:")
        # 只显示前 5 行，避免太多
        for line in result.stdout.splitlines()[:5]:
            print(f"  {line}")
    else:
        print("❌ ping 失败！错误信息:")
        print(f"  {result.stderr}")
except FileNotFoundError:
    print("  系统找不到 ping 命令（可能网络受限）")
print()

# ==================== 示例 2：查看当前目录文件 ====================
print("2. 📁 查看当前目录文件")
try:
    if os.name == 'nt':  # Windows
        cmd = ['dir']
    else:  # Mac/Linux
        cmd = ['ls', '-l']

    result = subprocess.run(cmd, capture_output=True, text=True)
    print(f"命令: {' '.join(cmd)}")
    if result.returncode == 0:
        print("输出预览（前 5 行）:")
        for line in result.stdout.splitlines()[:5]:
            print(f"  {line}")
    else:
        print("错误:", result.stderr)
except Exception as e:
    print("执行失败:", e)
print()

# ==================== 示例 3：获取 Python 版本 ====================
print("3. 🐍 获取 Python 版本")
try:
    result = subprocess.run([sys.executable, '--version'],
                            capture_output=True, text=True)
    print(f"Python 版本: {result.stdout.strip()}")
except Exception as e:
    print("获取版本失败:", e)
print()

# ==================== 示例 4：运行另一个 Python 脚本 ====================
print("4. 📜 运行另一个 Python 脚本")
# 先创建一个临时脚本（用于演示）
demo_script = "temp_demo.py"
with open(demo_script, "w", encoding="utf-8") as f:
    f.write('print("👋 Hello from temp_demo.py!")\n')
    f.write('print("当前目录:", __file__)\n')

try:
    result = subprocess.run([sys.executable, demo_script],
                            capture_output=True, text=True)
    if result.returncode == 0:
        print(f"✅ 脚本输出:\n{result.stdout}")
    else:
        print(f"❌ 脚本出错:\n{result.stderr}")
finally:
    # 清理：删除临时文件
    if os.path.exists(demo_script):
        os.remove(demo_script)
print()

# ==================== 示例 5：检查命令是否存在 ====================
print("5. 🔍 检查命令是否存在（比如 git）")
try:
    result = subprocess.run(['git', '--version'],
                            capture_output=True, text=True)
    if result.returncode == 0:
        print(f"✅ 找到 Git: {result.stdout.strip()}")
    else:
        print("❌ 未安装 Git")
except FileNotFoundError:
    print("❌ 未找到 git 命令（可能未安装或不在 PATH 中）")
print()

# ==================== 示例 6：获取系统信息（Windows: systeminfo）====================
if os.name == 'nt':
    print("6. 💻 Windows: 获取系统信息（只显示前几行）")
    try:
        result = subprocess.run(['systeminfo'], capture_output=True, text=True, timeout=10)
        print(f"系统信息预览（前 5 行）:")
        for line in result.stdout.splitlines()[:5]:
            print(f"  {line}")
    except subprocess.TimeoutExpired:
        print("  命令超时（systeminfo 太慢）")
    except Exception as e:
        print("  执行失败:", e)
    print()

# ==================== 示例 7：打开外部程序（不等待）====================
print("7. 🚀 打开记事本（不等待关闭）")
print("👉 正在尝试打开记事本...")
try:
    # 使用 Popen 不等待程序结束
    if os.name == 'nt':
        process = subprocess.Popen(['notepad.exe'])
        print(f"✅ 记事本已启动（PID: {process.pid}）")
    else:
        print("💡 提示：Mac/Linux 可以尝试打开文本编辑器，如 'nano' 或 'gedit'")
except Exception as e:
    print(f"❌ 启动失败: {e}")
print()

# ==================== 示例 8：向命令输入数据（echo + grep）====================
print("8. 📥 向命令输入数据（模拟输入）")
try:
    # 模拟：echo "hello world" | grep "hello"
    p1 = subprocess.Popen(['echo', 'hello world'], stdout=subprocess.PIPE, text=True)
    p2 = subprocess.Popen(['grep', 'hello'], stdin=p1.stdout, stdout=subprocess.PIPE, text=True)
    p1.stdout.close()  # 允许 p1 正常结束
    output, _ = p2.communicate()

    if output:
        print(f"✅ 找到匹配: '{output.strip()}'")
    else:
        print("❌ 未找到匹配")
except Exception as e:
    print(f"执行失败（可能 grep 不存在）: {e}")
print()

# ==================== 示例 9：设置环境变量运行命令 ====================
print("9. 🏷️ 设置环境变量运行命令")
try:
    # 临时设置一个环境变量
    env = os.environ.copy()
    env["MY_VAR"] = "HelloFromSubprocess"

    result = subprocess.run([sys.executable, '-c', 'import os; print(os.getenv("MY_VAR"))'],
                            capture_output=True, text=True, env=env)
    print(f"环境变量 MY_VAR 的值: {result.stdout.strip()}")
except Exception as e:
    print("失败:", e)
print()

# ==================== 示例 10：超时控制 ====================
print("10. ⏱️ 命令执行超时控制")
try:
    # 运行一个可能很慢的命令，设置 2 秒超时
    result = subprocess.run(
        ['ping', '-n', '10', 'www.baidu.com'] if os.name == 'nt' else ['ping', '-c', '10', 'www.baidu.com'],
        capture_output=True, text=True, timeout=2)
    print("✅ 命令在时间内完成")
except subprocess.TimeoutExpired:
    print("⏰ 命令超时！（我们故意设置的）")
except Exception as e:
    print("其他错误:", e)
print()

print("🎉 所有练习完成！")
print("💡 小贴士：")
print("  - subprocess.run() 适合运行并等待结果")
print("  - subprocess.Popen() 适合运行不等待或复杂交互")
print("  - 记得用 capture_output=True 和 text=True 获取输出")
print("  - 列表形式传参更安全，避免 shell 注入")