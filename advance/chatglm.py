import transformers
import torch
from transformers import AutoTokenizer, AutoModel

def get_transformer_version():
    print(transformers.__version__)

def torch_version():
    print(torch.__version__)    

def chat():
    tokenizer = AutoTokenizer.from_pretrained("D:\\software\\aigc\\chatglm-6b-int4", trust_remote_code=True)
    model = AutoModel.from_pretrained("D:\\software\\aigc\\chatglm-6b-int4", trust_remote_code=True).half().cuda()
    model = model.eval()
    response, history = model.chat(tokenizer, "你知道特朗普吗", history=[])
    print(response)

def cudaAvailable():
    print(torch.cuda.is_available())

def cudaVersion():
    print(torch.version.cuda)

chat()
