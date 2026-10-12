import os
import json

import streamlit as st

from openai import OpenAI

#设置页面配置项
st.set_page_config(
    page_title="AI伙伴",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={}
)

#大标题
st.title("AI伙伴")

#logo
st.logo("recources/logo.png")

#系统提示词（人设）
base_prompt = "你是一个ai陪伴助手"

#聊天记录（流水账）和长期记忆（要点档案）的保存文件
CHAT_FILE = "chat_history.json"
MEMORY_FILE = "memory.json"

#初始化聊天信息：优先从文件恢复历史记录
if "messages" not in st.session_state:
    if os.path.exists(CHAT_FILE):
        with open(CHAT_FILE, "r", encoding="utf-8") as f:
            st.session_state.messages = json.load(f)
    else:
        st.session_state.messages = []

#初始化长期记忆：记忆内容 + 已经总结到第几条消息（防止重复总结）
if "memory" not in st.session_state:
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r", encoding="utf-8") as f:
            memory_data = json.load(f)
            st.session_state.memory = memory_data.get("content", "")
            st.session_state.summarized_count = memory_data.get("summarized_count", 0)
    else:
        st.session_state.memory = ""
        st.session_state.summarized_count = 0

# 展示聊天记录
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])


#创建客户端
client = OpenAI(
    api_key=os.environ.get("MIMO_API_KEY"),
    base_url="https://api.xiaomimimo.com/v1"
)


#拼接本次使用的系统提示词：人设 + 长期记忆
def build_system_prompt():
    prompt = base_prompt
    if st.session_state.memory:
        prompt += (
            "\n\n【关于用户的长期记忆，聊天时请自然地运用这些信息】\n"
            + st.session_state.memory
        )
    return prompt


#保存长期记忆到文件
def save_memory():
    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(
            {
                "content": st.session_state.memory,
                "summarized_count": st.session_state.summarized_count
            },
            f, ensure_ascii=False, indent=2
        )


#让ai把"还没总结过的对话"提炼合并进长期记忆
def update_long_memory():
    #取出上一次总结之后的新消息
    new_messages = st.session_state.messages[st.session_state.summarized_count:]
    if not new_messages:
        return
    #把新消息拼成一段文本
    new_text = "\n".join(f'{m["role"]}：{m["content"]}' for m in new_messages)

    #这次不需要流式输出，等它返回完整结果即可
    memory_result = client.chat.completions.create(
        model="mimo-v2.6-flash",
        messages=[
            {
                "role": "system",
                "content": (
                    "你是记忆整理助手。请从新对话中提取关于用户的、以后聊天有用的长期信息"
                    "（姓名、喜好、厌恶、重要经历、情绪状态、约定等），合并进已有记忆。"
                    "要求：1.用简洁的要点形式输出；2.忽略寒暄等无关内容；"
                    "3.直接输出更新后的完整记忆，不要输出任何解释。"
                )
            },
            {
                "role": "user",
                "content": f"【已有的长期记忆】\n{st.session_state.memory or '（暂无）'}\n\n【新对话】\n{new_text}"
            }
        ],
        stream=False,
        extra_body={"thinking": {"type": "disabled"}}
    )

    #更新记忆内容和总结位置，并写入文件
    st.session_state.memory = memory_result.choices[0].message.content
    st.session_state.summarized_count = len(st.session_state.messages)
    save_memory()


#侧边栏：记忆管理
with st.sidebar:
    st.subheader("🧠 长期记忆")
    with st.expander("查看记忆内容"):
        st.markdown(st.session_state.memory or "（暂无记忆，每聊满10条消息会自动总结）")

    if st.button("立即更新记忆"):
        with st.spinner("正在总结记忆..."):
            update_long_memory()
        st.rerun()

    if st.button("清空记忆"):
        st.session_state.memory = ""
        st.session_state.summarized_count = len(st.session_state.messages)
        save_memory()
        st.rerun()

    st.divider()

    #清空聊天流水账，长期记忆不受影响
    if st.button("清空聊天记录"):
        st.session_state.messages = []
        st.session_state.summarized_count = 0
        if os.path.exists(CHAT_FILE):
            os.remove(CHAT_FILE)
        save_memory()
        st.rerun()


#输入框制作
prompt = st.chat_input("给水饺发送消息")
if prompt:
    st.chat_message("user").write(prompt)
    print("调用ai大模型：提示词", prompt)
    # 保存用户输入的提示词
    st.session_state.messages.append({"role": "user", "content": prompt})


    #调用大模型：system提示词(人设+长期记忆) + 全部历史消息，这样ai才能理解上下文
    completion = client.chat.completions.create(
        model="mimo-v2.6-flash",
        messages=[
            {
                "role": "system",
                "content": build_system_prompt()
            },
            *st.session_state.messages
        ],
        max_completion_tokens=1024,
        temperature=1.0,
        top_p=0.95,
        stream=True,
        # 关闭深度思考（官方默认开启），关闭后首字延迟显著降低
        extra_body={"thinking": {"type": "disabled"}},

        stop=None,
        frequency_penalty=0,
        presence_penalty=0
    )

    # 输出返回的结果：write_stream 自动逐块遍历并显示，返回完整文本
    full_reply = st.chat_message("assistant").write_stream(completion)
    print("ai大模型返回结果：", full_reply)
    # 保存大模型返回的回复
    st.session_state.messages.append({"role": "assistant", "content": full_reply})

    #把聊天记录写入文件（把流水账也持久化）
    with open(CHAT_FILE, "w", encoding="utf-8") as f:
        json.dump(st.session_state.messages, f, ensure_ascii=False, indent=2)

    #每积累10条新消息（约5轮对话），自动总结一次长期记忆
    if len(st.session_state.messages) - st.session_state.summarized_count >= 10:
        with st.spinner("正在更新长期记忆..."):
            update_long_memory()







