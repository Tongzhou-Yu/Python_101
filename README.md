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
- **智谱AI**：https://open.bigmodel.cn/usercenter/proj-mgmt/apikeys
- **Fish Audio TTS**：https://fishspeech.net（Unity 项目使用）
- **JSONBin.io**：https://jsonbin.io（Unity 项目使用）

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

**方式一：使用 requirements.txt（推荐）**
```bash
pip install -r requirements.txt
```

**方式二：手动安装**
```bash
pip install requests streamlit websocket-client pygame
```

**依赖库说明**：

| 库名               | 用途          | 必需性 | 使用场景                                                   |
| ------------------ | ------------- | ------ | ---------------------------------------------------------- |
| `requests`         | HTTP API调用  | ✅ 必需 | 所有课程（调用智谱AI API）                                 |
| `streamlit`        | Web界面框架   | ⚠️ 可选 | 第3周 Streamlit 版本（`3.3_memory_clonebot_streamlit.py`） |
| `websocket-client` | WebSocket连接 | ⚠️ 可选 | 第2周 TTS功能（`xunfei_tts.py`）                           |
| `pygame`           | 音频播放      | ⚠️ 可选 | 第2周 TTS音频播放（有系统默认播放器作为备选）              |

**注意事项**：
1. **基础功能**：如果只学习第1-2周的基础对话功能，只需要安装 `requests`
2. **Streamlit版本**：如果要运行第3周的 Streamlit 版本，需要安装 `streamlit`
3. **TTS功能**：如果要使用第2周的语音合成功能，需要安装 `websocket-client` 和 `pygame`
4. **websocket包冲突**：确保安装的是 `websocket-client` 而不是 `websocket`：
   ```bash
   pip uninstall websocket -y  # 如果已安装错误的websocket包
   pip install websocket-client
   ```

## 项目学习路线（Roadmap）

![Python 101 系统架构图（修正版）](python%201010%20system%20archi...corrected.jpg)


| 周次  | 主题                 | 主要内容/里程碑                                                                                                                                                |
| ----- | -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 第1周 | Python基础           | 1_\* 基础语法、流程控制、函数、数据结构                                                                                                                        |
| 第2周 | 对话系统             | 2_\* 单轮对话 → 多轮对话 → 角色扮演 → TTS（语音合成）                                                                                                          |
| 第3周 | 记忆系统             | 3_\* 函数引入 → 记忆机制基础 → 克隆机器人 → 接入 Streamlit 前端                                                                                                |
| 第4周 | 工程重构与实用增强 🆕 | 4.1_\* 项目结构标准化、API解耦拆分、异常处理优化、虚拟环境、依赖管理<br>4.2_\* 角色模块细分、终止规则模块化、对话逻辑增强（见 roles.py / logic.py / chat.py ） |


## 第五周预告

第五周将深入学习"云端AI对话系统架构"，下图为参考架构图：

![AI对话系统架构图_ChatdollKit版](AI对话系统架构图_ChatdollKit版.png)

## Unity 项目依赖（5.2_unity_chatdoll）

**注意**：`5.2_unity_chatdoll` 文件夹包含版权内容（VRM 模型等），**不会提交到 Git**。详细安装说明请参考 [`5.2_unity_chatdoll/README.md`](5.2_unity_chatdoll/README.md)。

### 必需包（按导入顺序）

1. **UniTask.2.5.10.unitypackage**
   - 异步编程库，ChatdollKit 依赖
   - 下载地址：https://github.com/Cysharp/UniTask/releases

2. **VRM-0.130.1_c721.unitypackage** (或更新版本)
   - VRM 1.0 格式支持库（UniVRM）
   - 下载地址：https://github.com/vrm-c/UniVRM/releases

3. **ChatdollKit_0.8.15.unitypackage**
   - 核心框架，提供 ModelController、AnimatedVoiceRequest 等基础功能
   - 下载地址：https://github.com/uezo/ChatdollKit/releases/tag/v0.8.15

4. **uLipSync-v3.1.4-with-Samples.unitypackage**
   - 口型同步库，用于根据音频生成口型动画
   - 下载地址：https://github.com/hecomi/uLipSync/releases

### 导入步骤

1. 在 Unity 中打开项目
2. 依次双击上述 `.unitypackage` 文件导入
3. 导入顺序建议：**UniTask → VRM → ChatdollKit → uLipSync**
4. 导入完成后，在 `Project Settings > Player > Scripting Define Symbols` 添加 `USE_VRM10`
5. 检查 `Assets/Scripts/JsonBinListener.cs` 是否存在

### API 配置

- **Fish Audio TTS**：注册 https://fishspeech.net，获取 API Key 和 Reference ID
- **JSONBin.io**：注册 https://jsonbin.io，获取 Bin ID 和 Access Key

### 可选资源

- **VRM 模型**：从 VRoid Hub、Booth 或其他来源获取 VRM 1.0 格式的 3D 角色模型


