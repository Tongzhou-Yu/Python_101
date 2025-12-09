# 5.2 Unity Chatdoll

数字媒体艺术本科课程示范项目 - Unity 虚拟角色 + TTS 语音合成

## 功能

- 监听 JSONBin.io 获取文本消息
- 使用 Fish Audio TTS 生成语音
- VRM 模型口型同步 (uLipSync)
- 自动眨眼

## 依赖包安装

克隆此仓库后，需要按以下顺序安装依赖包：

### 1. UniTask
- 下载: `UniTask.2.5.10.unitypackage`
- GitHub: https://github.com/Cysharp/UniTask

### 2. VRM 1.0
- 下载: `VRM-0.130.1_c721.unitypackage`
- GitHub: https://github.com/vrm-c/UniVRM

### 3. ChatdollKit
- 下载: `ChatdollKit_0.8.15.unitypackage`
- GitHub: https://github.com/uezo/ChatdollKit

### 4. uLipSync
- 下载: `uLipSync-v3.1.4-with-Samples.unitypackage`
- GitHub: https://github.com/hecomi/uLipSync

### 5. AnimeGirlIdleAnimations_free (可选)
- 从 Unity Asset Store 下载

## 安装后配置

1. 打开 `Edit → Project Settings → Player`
2. 在 `Other Settings → Scripting Define Symbols` 中添加：
   ```
   USE_VRM10
   ```
3. 点击 Apply

## 场景配置

打开 `Assets/Scenes/Chatdoll.unity`

### ChatDoll 物体组件：
- Model Controller
- Json Bin Listener (配置 Bin ID 和 Access Key)
- Fish Audio Speech Synthesizer (配置 API Key 和 Reference ID)
- U Lip Sync (配置 Profile)
- VRM10 Blink

### Joker 物体组件：
- U Lip Sync Expression VRM (配置 A/I/U/E/O 口型映射)

## API 配置

### JSONBin.io
1. 注册 https://jsonbin.io
2. 创建一个 Bin
3. 获取 Bin ID 和 Access Key

### Fish Audio
1. 注册 https://fishspeech.net
2. 获取 API Key
3. 选择一个声音模型，获取 Reference ID

## VRM 模型

需要自行准备 VRM 1.0 格式的模型，放入 `Assets/Models/` 文件夹。

推荐来源：
- [VRoid Hub](https://hub.vroid.com/) - 免费/付费模型
- [Booth](https://booth.pm/) - 日本创作者平台
- [VRoid Studio](https://vroid.com/studio) - 自己制作

## 文件说明

```
Assets/
├── Scripts/           # 原创脚本
│   ├── JsonBinListener.cs
│   ├── FishAudioSpeechSynthesizer.cs
│   └── VRM10Blink.cs
├── Scenes/            # 场景文件
│   └── Chatdoll.unity
├── Models/            # VRM 模型（需自行准备）
└── Animator/          # 动画控制器
```

