import json

def main(language: str):
    data = {"command":"transfer_to_agent","payload":{"message":"正在为您转接人工客服，请稍候..."}}
    if(language == "en"):
        data = {"command":"transfer_to_agent","payload":{"message":"Transferring you to a human agent, please wait..."}}
    return {
        "result": json.dumps(data, ensure_ascii=False)
    }
