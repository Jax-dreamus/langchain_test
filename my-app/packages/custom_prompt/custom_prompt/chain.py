from langchain_community.chat_models import ChatOpenAI
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate, FewShotPromptTemplate

from custom_prompt.examples import examples, PlaylistAttributes

example_prompt = PromptTemplate(
    input_variables=["content"], template="{content}\n{genre}\n{tempo}\n{instruments}\n{mood}\n{etc_keywords}"
)

fewshot_prompt = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    suffix="{content}",
    input_variables=["content", "genre", "tempo", "instruments", "mood", "etc_keywords"],
)

parser = JsonOutputParser(pydantic_object=PlaylistAttributes)

prompt = PromptTemplate(
    template=""""당신은 음악 플레이리스트 관련된 텍스트를 받으면, 해당 플레이리스트의 특징을 추출하는 역할을 합니다. 
                      당신의 목표는 주어진 플레이리스트의 특징을 추출하는 것입니다.
                      각각의 특징 값들은 한글로 표기 되어야 합니다. 
                      주어진 텍스트는 주로 음악 플레이리스트에 대한 설명입니다.\n{format_instructions}\n{few_shot_prompt}\n{content}""",
    input_variables=["content"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)

_inspector_model = ChatOpenAI()

chain = prompt | _inspector_model | parser
