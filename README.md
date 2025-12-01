# Python 基础知识总结

## 课程需安装和下载的程序：
- https://cursor.com/cn
- https://www.anaconda.com/download
- https://git-scm.com/install/
- https://unity.cn/
- https://vroid.com/

注意安装Anaconda的时候要勾选“Add Anaconda 3 to my PATH……”

![Anaconda 添加到 PATH 路径截图](Anaconda_PATH.png)

## 课程需申请的API Key：
- https://open.bigmodel.cn/usercenter/proj-mgmt/apikeys
- https://console.xfyun.cn/services/uts

## 虚拟环境设置（Cursor）

### 创建虚拟环境
在Cursor中创建Python虚拟环境：

1. **使用终端创建**：
   ```bash
   python -m venv .venv
   ```

2. **激活虚拟环境**：
   - **Windows (PowerShell)**:
     ```powershell
     .venv\Scripts\Activate.ps1
     ```
   - **Windows (CMD)**:
     ```cmd
     .venv\Scripts\activate.bat
     ```
   - **macOS/Linux**:
     ```bash
     source .venv/bin/activate
     ```

3. **在Cursor中选择解释器**：
   - 按 `Ctrl+Shift+P` (Windows) 或 `Cmd+Shift+P` (Mac)
   - 输入 "Python: Select Interpreter"
   - 选择 `.venv` 文件夹中的Python解释器

### 安装依赖库
激活虚拟环境后，安装项目所需的库：

```bash
pip install requests websocket-client pygame
```

**依赖库说明**：
- `requests` - 用于HTTP API调用（智谱AI）
- `websocket-client` - 用于WebSocket连接（科大讯飞TTS）
- `pygame` - 用于音频播放

**注意**：确保安装的是 `websocket-client` 而不是 `websocket`：
```bash
pip uninstall websocket -y  # 如果已安装错误的websocket包
pip install websocket-client
```

周次	主题	文件
第1周	Python基础	1_* 
第2周	对话系统	2_*(单轮→多轮→角色扮演→TTS)
第3周	记忆系统	3_* (函数引入→记忆基础→克隆机器人→Streamlit)