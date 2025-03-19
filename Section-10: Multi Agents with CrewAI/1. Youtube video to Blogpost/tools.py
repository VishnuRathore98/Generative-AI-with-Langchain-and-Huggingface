from crewai_tools import YoutubeChannelSearchTool
from crewai import LLM

from dotenv import load_dotenv
import os

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

llm = LLM(
    model="groq/llama-3.2-90b-text-preview",
    temperature=0.7,
    api_key=GROQ_API_KEY
)


# Initialize the tool with a specific Youtube channel handle to target your search
yt_tool = YoutubeChannelSearchTool(
    youtube_channel_handle='@krishnaik06',
    config=dict(
        llm=dict(
            provider="ollama",  # or google, openai, anthropic, llama2, ...
            config=dict(
                model="deepseek-r1:1.5b",
                # temperature=0.5,
                # top_p=1,
                # stream=true,
            ),
        ),
    ))
