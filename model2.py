from langchain_openai import ChatOpenAI
from langchain_openai import OpenAI

llm = OpenAI()
chat_model = ChatOpenAI(model="gpt-3.5-turbo-0125")
from langchain_core.messages import HumanMessage

text = "What would be a good company name for a company that makes colorful socks?"
messages = [HumanMessage(content=text)]

# Invoke llm and print the result
llm_result = llm.invoke(text)
print("Result from llm:", llm_result)

# Invoke chat_model and print the result
chat_model_result = chat_model.invoke(messages)
print("Result from chat_model:", chat_model_result)
from langchain.prompts import PromptTemplate

prompt = PromptTemplate.from_template("What is a good name for a company that makes {product}?")
print(prompt.format(product="colorful socks"))
from langchain.prompts.chat import ChatPromptTemplate

template = "You are a helpful assistant that translates {input_language} to {output_language}."
human_template = "{text}"

chat_prompt = ChatPromptTemplate.from_messages([
    ("system", template),
    ("human", human_template),
])

formatted_messages = chat_prompt.format_messages(input_language="English", output_language="French", text="I love programming.")

print("Formatted messages:", formatted_messages)
from langchain.output_parsers import CommaSeparatedListOutputParser

output_parser = CommaSeparatedListOutputParser()
print(output_parser.parse("hi, bye"))
from langchain.prompts.chat import ChatPromptTemplate

template = "Generate a list of 5 {text}.\n\n{format_instructions}"

chat_prompt = ChatPromptTemplate.from_template(template)
chat_prompt = chat_prompt.partial(format_instructions=output_parser.get_format_instructions())
chain = chat_prompt | chat_model | output_parser
result = chain.invoke({"text": "colors"})

print("Result:", result)



