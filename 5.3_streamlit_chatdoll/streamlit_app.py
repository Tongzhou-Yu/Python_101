"""Streamlit主应用"""
import streamlit as st
from sprite import get_sprite_html
from jsonbin_client import save_to_jsonbin
from state import (
    init_session_state,
    update_speaking_state,
    stop_speaking,
    clear_all,
    should_stop_speaking,
    add_message
)

st.set_page_config(
    page_title="说话精灵 - ChatDoll",
    page_icon="🗣️",
    layout="wide"
)

# 初始化状态
init_session_state()

st.title("🗣️ 说话精灵 - ChatDoll")
st.markdown("---")

# 侧边栏配置
with st.sidebar:
    st.header("⚙️ JSONBin 配置")
    
    bin_id = st.text_input(
        "Bin ID",
        value=st.session_state.bin_id,
        help="在 JSONBin.io 控制台获取你的 Bin ID"
    )
    st.session_state.bin_id = bin_id
    
    access_key = st.text_input(
        "Access Key",
        value=st.session_state.access_key,
        type="password",
        help="在 JSONBin.io 控制台的 API Keys 页面获取"
    )
    st.session_state.access_key = access_key
    
    if bin_id and access_key:
        st.success("✅ JSONBin 已配置")
    else:
        st.warning("⚠️ 请配置 JSONBin 以使用说话功能")
    
    st.markdown("---")
    st.markdown("### 📝 使用说明")
    st.info(
        "1. 在侧边栏填入 JSONBin 的 Bin ID 和 Access Key\n"
        "2. 在下方输入框输入要说的文本\n"
        "3. 点击发送，精灵会开始说话\n"
        "4. 如果配置了 Unity ChatDollKit，精灵会同步说话"
    )
    
    if st.button("🔄 清空消息"):
        clear_all()
        st.rerun()

# 主界面布局
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("🎭 说话精灵")
    
    # 检查是否应该自动停止说话
    if should_stop_speaking():
        stop_speaking()
    
    # 获取当前说话状态和文本
    is_speaking = st.session_state.is_speaking
    current_text = st.session_state.speaking_text if is_speaking else ""
    
    sprite_html = get_sprite_html(is_speaking, current_text)
    st.components.v1.html(sprite_html, height=500)
    
    # 添加停止说话按钮
    if is_speaking:
        if st.button("⏹️ 停止说话", key="stop_speaking"):
            stop_speaking()
            st.rerun()

with col2:
    st.subheader("💬 消息记录")
    
    # 显示消息历史
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])
            if "timestamp" in msg:
                st.caption(f"时间: {msg['timestamp']}")
    
    # 输入框
    user_input = st.chat_input("输入要让精灵说的话...")
    
    if user_input:
        if not st.session_state.bin_id or not st.session_state.access_key:
            st.error("❌ 请先在侧边栏配置 JSONBin 的 Bin ID 和 Access Key")
        else:
            # 添加用户消息
            add_message("user", user_input)
            
            # 发送到JSONBin
            with st.spinner("正在发送..."):
                success, message = save_to_jsonbin(
                    user_input,
                    st.session_state.bin_id,
                    st.session_state.access_key
                )
            
            if success:
                st.success(f"✅ {message}")
                
                # 添加系统消息
                add_message("assistant", "✅ 已发送到 JSONBin，精灵开始说话！")
                
                # 设置说话状态
                update_speaking_state(user_input)
                
                # 触发精灵说话动画（通过重新渲染）
                st.rerun()
            else:
                st.error(f"❌ {message}")

# 底部说明
st.markdown("---")
st.caption("💡 提示：配置 JSONBin 后，Unity ChatDollKit 会自动监听并让3D角色说话。Web端的精灵会同步显示说话动画。")

