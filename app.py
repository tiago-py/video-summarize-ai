import streamlit as st 


with st.sidebar:
	st.header("Video Summarize AI")
	st.text("By: Tiago Braga")

	st.markdown("""
		##About
		***
		Video Summarize AI is a web app that allows you to summarize videos.
		***
		***
		Developed with an LLM from langchain.
		***
		##Feats
		- [Streamlit](https://streamlit.io)
      	- [Modelo OpenAI](https://openai.com) LLM Model
      	- [LangChain](https://www.langchain.com) LLM Library
		""")


def main():
	st.title("Video Summarize AI")
	user_input = st.text_input("Insert an youtube link here:", placeholder="https://youtube.com")

	if user_input:
		st.video(user_input)


if __name__ == "__main__":
	main()