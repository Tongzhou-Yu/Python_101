# Python 基础知识总结

## 课程需安装和下载的程序：
- https://cursor.com/cn
- https://www.anaconda.com/download
- https://git-scm.com/install/
- https://unity.cn/
- https://vroid.com/

注意安装Anaconda的时候要勾选“Add Anaconda 3 to my PATH……”

![Anaconda 添加到 PATH 路径截图](Anaconda_PATH.png)

## 文件一：101.py

### 1. 变量赋值
- **知识点**：Python 中的变量赋值不需要声明类型
- **示例**：`x = "1"` 和 `y = "2"`
- **说明**：Python 是动态类型语言，变量类型由赋值的值决定

### 2. 字符串类型
- **知识点**：使用引号（单引号或双引号）创建字符串
- **示例**：`"1"` 和 `"2"` 都是字符串类型
- **说明**：字符串是 Python 中的基本数据类型之一

### 3. 字符串连接
- **知识点**：使用 `+` 运算符可以连接字符串
- **示例**：`x + y` 的结果是 `"12"`（字符串连接，不是数字相加）
- **说明**：当操作数是字符串时，`+` 执行字符串连接操作

### 4. 输出函数
- **知识点**：`print()` 是 Python 的内置函数，用于输出内容
- **示例**：`print(x+y)` 输出 `"12"`
- **说明**：`print()` 可以将表达式的结果打印到控制台

## 文件二：glm.py

### 1. 模块导入
- **知识点**：使用 `import` 关键字导入外部模块
- **示例**：`import requests` 和 `import json`
- **说明**：Python 通过导入模块来使用第三方库或标准库的功能

### 2. 函数定义
- **知识点**：使用 `def` 关键字定义函数
- **示例**：`def call_zhipu_api(messages, model="glm-4-flash"):`
- **说明**：
  - 函数名遵循命名规范（小写字母+下划线）
  - 可以定义参数，支持默认参数值（`model="glm-4-flash"`）

### 3. 字典（Dictionary）
- **知识点**：字典是键值对的数据结构
- **示例**：
  ```python
  headers = {
      "Authorization": "...",
      "Content-Type": "application/json"
  }
  ```
- **说明**：字典用花括号 `{}` 定义，键值对用冒号 `:` 分隔

### 4. HTTP 请求
- **知识点**：使用 `requests` 库发送 HTTP POST 请求
- **示例**：`requests.post(url, headers=headers, json=data)`
- **说明**：
  - `requests` 是第三方库，需要先安装
  - `post()` 方法用于发送 POST 请求
  - 可以传递 URL、请求头和 JSON 数据

### 5. 条件语句
- **知识点**：使用 `if` 进行条件判断
- **示例**：`if response.status_code == 200:`
- **说明**：
  - `if` 语句用于根据条件执行不同的代码块
  - 使用 `==` 进行相等比较
  - 使用缩进表示代码块（Python 的特色）

### 6. 返回值
- **知识点**：使用 `return` 语句返回函数结果
- **示例**：`return response.json()`
- **说明**：函数可以通过 `return` 返回一个值，也可以返回多个值（元组）

### 7. 异常处理
- **知识点**：使用 `raise` 抛出异常
- **示例**：`raise Exception(f"API调用失败: {response.status_code}, {response.text}")`
- **说明**：
  - `raise` 用于主动抛出异常
  - `Exception` 是 Python 的基础异常类
  - f-string 格式化字符串（`f"..."`）用于在字符串中插入变量

### 8. 列表（List）
- **知识点**：列表是有序的元素集合
- **示例**：
  ```python
  messages = [
      {"role": "user", "content": "你好，请介绍一下自己"}
  ]
  ```
- **说明**：
  - 列表用方括号 `[]` 定义
  - 列表中可以包含字典等复杂数据结构
  - 列表是有序的，可以包含重复元素

### 9. 字典访问
- **知识点**：使用方括号 `[]` 访问字典的值
- **示例**：`result['choices'][0]['message']['content']`
- **说明**：
  - 通过键名访问字典的值
  - 可以嵌套访问多层字典
  - `[0]` 表示访问列表的第一个元素（索引从 0 开始）

### 10. 函数调用
- **知识点**：通过函数名和参数调用函数
- **示例**：`call_zhipu_api(messages)`
- **说明**：调用函数时传递参数，函数执行后返回结果

## 总结

这两个文件涵盖了 Python 的基础知识：

**基础概念**：
- 变量赋值、数据类型（字符串、字典、列表）
- 运算符（`+`、`==`）
- 输入输出（`print()`）

**控制结构**：
- 条件语句（`if`）
- 函数定义和调用（`def`、`return`）

**高级特性**：
- 模块导入（`import`）
- 异常处理（`raise`）
- 数据结构操作（字典、列表的创建和访问）
- 第三方库的使用（`requests`）

**Python 特色**：
- 使用缩进表示代码块（不使用大括号）
- 动态类型（无需声明变量类型）
- f-string 字符串格式化
- 简洁的语法和丰富的内置功能

## Git 基础操作与与 Cursor 同步流程

### 一、Git 基础及常用命令

#### 1. Git 简介
Git 是一个分布式版本控制系统，适合多人协作开发，能够跟踪文件的变更历史，回退版本，方便协作与管理。

#### 2. 配置用户名和邮箱

Git 需要配置用户名（user.name）和邮箱（user.email）以标记每次提交者的信息。

```bash
git config --global user.name "你的名字"
git config --global user.email "你的邮箱@example.com"
```
- `--global` 表示全局配置（对当前用户所有仓库生效）。

#### 3. 初始化本地仓库

```bash
git init
```
- 在当前目录初始化一个新的本地 Git 仓库。

#### 4. 添加文件到暂存区

```bash
git add 文件名
# 或添加所有更改
git add .
```

#### 5. 提交更改

```bash
git commit -m "提交说明"
```
- `-m` 后面是本次提交的信息。

#### 6. 查看状态与历史

```bash
git status    # 查看当前工作区和暂存区状态
git log       # 查看提交历史
```

#### 7. 远程仓库操作

##### 添加远程仓库（如 Cursor 云端）

```bash
git remote add origin 仓库地址
```

##### 拉取远程更新（先同步云端最新代码）

```bash
git pull origin main
```

##### 推送本地代码到远程

```bash
git push origin main
```

### 二、使用 Cursor 与 Git 同步代码的典型流程

以云端团队协作为例，建议操作顺序如下：

1. **拉取最新云端代码（避免冲突）**
   ```bash
   git pull origin main
   ```

2. **编辑本地代码、保存修改**

3. **查看状态，添加需要提交的文件**
   ```bash
   git status
   git add 文件名
   ```

4. **提交到本地仓库**
   ```bash
   git commit -m "描述你的更改"
   ```

5. **推送到远程云端（与 Cursor 或代码托管平台同步）**
   ```bash
   git push origin main
   ```

6. **如遇冲突，按照提示解决，并重复 add/commit/push**

---

### 常见问题与建议

- 每次推送前，**先 pull**，再 push。
- 只需配置一次 user.name 和 user.email。
- 推荐使用 `.gitignore` 忽略不需要同步的文件（如虚拟环境、日志等）。
- 可在 Cursor 编辑器内集成终端直接运行上述 Git 命令。

