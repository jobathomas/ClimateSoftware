# import relevant libraries
from dotenv import load_dotenv
from langchain.tools import tool
from langchain.agents import create_agent
from langchain.agents.middleware import PIIMiddleware
from langchain_ollama import ChatOllama
from main import df 
load_dotenv()


ollama_model = ChatOllama(
    model = "gpt-oss:120b",
    base_url= "https://ollama.com",
    temperature=0.2
)

@tool
def geo_gen():
    """Dataset containing different countries"""
    return df['country']
    


df_agent = create_agent(
    model= ollama_model,
    tools=[geo_gen], 
    system_prompt= "You are a coordinate generator"
                    "Available tools: \n"
                    "- geo_gen: A dataframe containing countries \n"
                    "Use the geo_gen tool to generate help you generate coordinates \n"
                    ,
    middleware= [PIIMiddleware("email",strategy = "block")]
    )


response = df_agent.invoke(
    {"messages":[{"role": "user", "content": "Return a dictionary of latitude and longitude coordinates for each country for all rows in the dataset"}]}
    )

print(response["messages"][-1].content)
