#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import json
from typing import Dict, Any

def fetch_recommend_products(userId: str, shopId: str):
    """
    获取商品分类树

    Returns:
        Any: API响应数据或错误信息
    """
    url = "http://192.168.64.4:9010/openApi/getProductRecommendList"

    headers = {
        'Content-Type': 'application/json'
    }

    
    url += f"?userId={userId}&shopId={shopId}"

    try:
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()
        return response.json()

    except requests.exceptions.RequestException as e:
        return {"error": f"请求失败: {str(e)}"}
    except json.JSONDecodeError as e:
        return {"error": f"JSON解析失败: {str(e)}"}
    except Exception as e:
        return {"error": f"未知错误: {str(e)}"}

def main(userId: str, shopId: str):
    """
    主函数 - 获取推荐商品并返回商品列表

    Returns:
        List: 包含productId和productName的字典列表
    """
    # 获取推荐商品数据
    recommend_products_result = fetch_recommend_products(userId, shopId)
    print("获取的推荐商品数据:", recommend_products_result)
    data = []
    try:
        if isinstance(recommend_products_result, dict) and recommend_products_result.get("code") == 200 and "result" in recommend_products_result:
            records = recommend_products_result.get("result", [])
            data = [
                {
                    "productId": record.get("productId"),
                    "productName": record.get("productName"),
                    "productSn": record.get("productSn"),
                    "picUrl": record.get("picUrl"),
                    "price": record.get("price")
                    
                }
                for record in records
            ]
        else:
            data = []
    except Exception:
        data = []

    return {
        "result": json.dumps(data, ensure_ascii=False)
    }
if __name__ == "__main__":
    # 测试代码
    test_result = main("6d7099092a57c99a83ff56232509a6e3", "f981da024da0d5b84a3bbdbca00e2d66")
    print("测试结果:")
    print(json.dumps(test_result, indent=2, ensure_ascii=False))