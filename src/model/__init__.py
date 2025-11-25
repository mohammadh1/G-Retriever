from src.model.llm import LLM
from src.model.pt_llm import PromptTuningLLM
from src.model.graph_llm import GraphLLM


load_model = {
    "llm": LLM,
    "inference_llm": LLM,
    "pt_llm": PromptTuningLLM,
    "graph_llm": GraphLLM,
}

# Replace the following with the model paths
llama_model_path = {
    "qwen2_3b": "/media/external_16TB_1/mohammad_hoseinkhani/resources/qwen25-3b",
    "llama3_8b_ins": "/media/external_16TB_1/mohammad_hoseinkhani/resources/meta-llama/llama3-8b",
    "llama2_7b_hf": "/media/external_16TB_1/mohammad_hoseinkhani/resources/meta-llama/llama2-7b",
}
