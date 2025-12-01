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

## 项目学习路线（Roadmap）

| 周次  | 主题                 | 主要内容/里程碑                                                                                                                                                |
| ----- | -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 第1周 | Python基础           | 1_\* 基础语法、流程控制、函数、数据结构                                                                                                                        |
| 第2周 | 对话系统             | 2_\* 单轮对话 → 多轮对话 → 角色扮演 → TTS（语音合成）                                                                                                          |
| 第3周 | 记忆系统             | 3_\* 函数引入 → 记忆机制基础 → 克隆机器人 → 接入 Streamlit 前端                                                                                                |
| 第4周 | 工程重构与实用增强 🆕 | 4.1_\* 项目结构标准化、API解耦拆分、异常处理优化、虚拟环境、依赖管理<br>4.2_\* 角色模块细分、终止规则模块化、对话逻辑增强（见 roles.py / logic.py / chat.py ） |
