import streamlit as st
from snowflake.cortex import Complete
import time

st.title(":material/airwave: Write Streams")

# Connect to Snowflake
try:
    # Works in Streamlit in Snowflake
    from snowflake.snowpark.context import get_active_session
    session = get_active_session()
except:
    # Works locally and on Streamlit Community Cloud
    from snowflake.snowpark import Session
    session = Session.builder.configs(st.secrets["connections"]["snowflake"]).create() 

llm_models = ["claude-3-5-sonnet", "mistral-large", "llama3.1-8b"]
model= st.selectbox("Select a model", llm_models)

example_prompt = "What is Python?"
prompt = st.text_area("Enter prompt", example_prompt)

if st.button("Generate Response"):
    with st.spinner(f"Generating response with `{model}`"):
        stream_generator = Complete(
                    session=session,
                    model=model,
                    prompt=prompt,
                    stream=True,
                )
                
        st.write_stream(stream_generator)
      
# Footer
st.divider()
st.caption("Day 3: Write streams | 30 Days of AI")