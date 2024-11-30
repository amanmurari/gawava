from langchain_openai import OpenAI

from langchain_core.output_parsers import StrOutputParser
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
# Now we can override it and set it to "AI Assistant"
from langchain_core.prompts.prompt import PromptTemplate

template = """your name is Aman bot . he following is a friendly conversation between a human and an AI. The AI is talkative and provides lots of specific details from its context. If the AI does not know the answer to a question, it truthfully says it does not know. 
if you don't know answer you say i don't know.
Current conversation:
{history}
Human: {input}
AI Assistant:"""

prompt = PromptTemplate(input_variables=["history", "input"], template=template)


client = OpenAI(base_url="https://api.groq.com/openai/v1/chat/",api_key="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")

conversation = ConversationChain(
    prompt=prompt,
    llm=client,
    verbose=True,
    memory=ConversationBufferMemory(ai_prefix="AI Assistant")
    
)
chain = conversation  |  StrOutputParser()

