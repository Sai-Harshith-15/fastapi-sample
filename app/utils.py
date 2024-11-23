from langchain_openai import ChatOpenAI
from langchain.prompts.chat import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain.schema import HumanMessage

# Initialize the LangChain chat model with ChatOpenAI
llm = ChatOpenAI(
    base_url="https://openrouter.ai/api/v1",
    model="meta-llama/llama-3.1-8b-instruct", 
    api_key="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",
    temperature=0.1  # Adjust for more creative responses if needed
)

def generate_description(input_text):
    # Set up the prompt template
    prompt_template = ChatPromptTemplate.from_messages([
        SystemMessagePromptTemplate.from_template("As a Product Description Generator, generate a multi-paragraph rich-text product description with emojis from the information provided to you."),
        HumanMessagePromptTemplate.from_template("{input_text}")
    ])

    # Generate the response
    messages = prompt_template.format_messages(input_text=input_text)
    response = llm(messages)

    # Return the model's reply
    return response.content

# Example usage
input_data = "A modern, ergonomic office chair with adjustable height, lumbar support, and breathable mesh fabric."
description = generate_description(input_data)
# print(description)
