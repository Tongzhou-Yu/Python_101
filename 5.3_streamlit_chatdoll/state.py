"""状态管理模块"""
import streamlit as st
from datetime import datetime


def init_session_state():
    """初始化session state"""
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "is_speaking" not in st.session_state:
        st.session_state.is_speaking = False
    if "speaking_text" not in st.session_state:
        st.session_state.speaking_text = ""
    if "speaking_start_time" not in st.session_state:
        st.session_state.speaking_start_time = None
    if "bin_id" not in st.session_state:
        st.session_state.bin_id = ""
    if "access_key" not in st.session_state:
        st.session_state.access_key = ""


def update_speaking_state(text):
    """更新说话状态"""
    st.session_state.is_speaking = True
    st.session_state.speaking_text = text
    st.session_state.speaking_start_time = datetime.now()


def stop_speaking():
    """停止说话"""
    st.session_state.is_speaking = False
    st.session_state.speaking_text = ""
    st.session_state.speaking_start_time = None


def clear_all():
    """清空所有状态"""
    st.session_state.messages = []
    stop_speaking()


def should_stop_speaking():
    """判断是否应该停止说话（根据文本长度估算时长）"""
    if not st.session_state.is_speaking or not st.session_state.speaking_start_time:
        return False
    
    # 估算说话时长：每10个字符约1秒，最少2秒
    estimated_duration = max(2, len(st.session_state.speaking_text) / 10)
    elapsed = (datetime.now() - st.session_state.speaking_start_time).total_seconds()
    
    return elapsed > estimated_duration


def add_message(role, content):
    """添加消息到历史记录"""
    st.session_state.messages.append({
        "role": role,
        "content": content,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

