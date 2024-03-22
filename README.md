# LangChain OpenAI Integration

## Description
This repository contains scripts for integrating LangChain with OpenAI's language models.

## Components
1. **Language Models**: Utilizes OpenAI's GPT-3.5 language model for natural language processing tasks.
2. **Human Message Handling**: Uses LangChain's message class to handle human input messages.
3. **Prompt Generation**: Utilizes LangChain's prompt templates for generating prompts dynamically.
4. **Output Parsing**: Employs LangChain's output parsers for parsing and formatting model output.

Usage
1. Initialize OpenAI Model:
Create an instance of OpenAI's model.

from langchain_openai import OpenAI

llm = OpenAI()
2. Initialize Chat Model:
Create an instance of ChatOpenAI model for chat-based interactions.
from langchain_openai import ChatOpenAI
chat_model = ChatOpenAI(model="gpt-3.5-turbo-0125")
3. Provide Input Messages:
Define human input messages using LangChain's HumanMessage class.
from langchain_core.messages import HumanMessage
text = "What would be a good company name for a company that makes colorful socks?"
messages = [HumanMessage(content=text)]
4. Invoke Language Model:
Invoke OpenAI's language model to process the input text.
llm_result = llm.invoke(text)
print("Result from llm:", llm_result)
5. Invoke Chat Model:
Invoke the chat model to respond to human input messages.
chat_model_result = chat_model.invoke(messages)
print("Result from chat_model:", chat_model_result)
6. Generate Prompt:
Generate prompts dynamically using LangChain's PromptTemplate.
from langchain.prompts import PromptTemplate
prompt = PromptTemplate.from_template("What is a good name for a company that makes {product}?")
print(prompt.format(product="colorful socks"))
7. Generate Chat Prompt:
Generate chat prompts with specified templates.
from langchain.prompts.chat import ChatPromptTemplate
template = "You are a helpful assistant that translates {input_language} to {output_language}."
human_template = "{text}"

chat_prompt = ChatPromptTemplate.from_messages([
("system", template),
("human", human_template),
])
formatted_messages = chat_prompt.format_messages(input_language="English", output_language="French", text="I love programming.")
print("Formatted messages:", formatted_messages)
8. Output Parsing:
Parse and format model output using LangChain's output parsers.
from langchain.output_parsers import CommaSeparatedListOutputParser
output_parser = CommaSeparatedListOutputParser()
print(output_parser.parse("hi, bye"))
9. Chain Invocation:
Chain multiple components to process input and produce output.
chain = chat_prompt | chat_model | output_parser
result = chain.invoke({"text": "colors"})
print("Result:", result)
## Author
Yukti
