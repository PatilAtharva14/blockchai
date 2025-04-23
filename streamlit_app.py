
import streamlit as st
import time
import hashlib

# Initialize blockchain with Genesis Block
if "blockchain" not in st.session_state:
    st.session_state.blockchain = [
        {
            "index": 0,
            "timestamp": time.time(),
            "data": "Genesis Block",
            "previous_hash": "0",
            "hash": hashlib.sha256("Genesis Block".encode()).hexdigest()
        }
    ]

# Function to add a new block
def add_block(data):
    previous_block = st.session_state.blockchain[-1]
    index = previous_block["index"] + 1
    timestamp = time.time()
    previous_hash = previous_block["hash"]
    block_content = f"{index}{timestamp}{data}{previous_hash}"
    block_hash = hashlib.sha256(block_content.encode()).hexdigest()

    new_block = {
        "index": index,
        "timestamp": timestamp,
        "data": data,
        "previous_hash": previous_hash,
        "hash": block_hash
    }

    st.session_state.blockchain.append(new_block)

# Streamlit interface
st.title("🧱 Simple Blockchain Demo")

data_input = st.text_input("Enter data for the new block:")

if st.button("Add Block"):
    if data_input:
        add_block(data_input)
        st.success("Block added to the chain!")
    else:
        st.warning("Please enter data for the block.")

st.subheader("Current Blockchain:")

for block in st.session_state.blockchain:
    st.json(block)
