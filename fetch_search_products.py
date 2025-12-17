#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import json
from typing import Dict, Any

def fetch_search_products(keyword: str):
    """
    获取商品分类树

    Returns:
        Any: API响应数据或错误信息
    """
    url = "http://192.168.64.4:9010/openApi/searchProductsByKeyword"

    headers = {
        'Content-Type': 'application/json'
    }

    payload = {
        "page": 1,
        "size": 100,
        "keyword": keyword
    }

    try:
        response = requests.post(url, headers=headers, json=payload, timeout=30)
        response.raise_for_status()
        return response.json()

    except requests.exceptions.RequestException as e:
        return {"error": f"请求失败: {str(e)}"}
    except json.JSONDecodeError as e:
        return {"error": f"JSON解析失败: {str(e)}"}
    except Exception as e:
        return {"error": f"未知错误: {str(e)}"}

def main(keyword: str):
    """
    主函数 - 搜索商品并返回分类列表

    Returns:
        List: 包含categoryId和categoryName的字典列表
    """
    # 获取商品分类数据
    categories_result = fetch_search_products(keyword)
    print("获取的搜索商品数据:", categories_result)
    data = []
    try:
        if isinstance(categories_result, dict) and categories_result.get("code") == 200 and "result" in categories_result:
            records = categories_result["result"].get("records", [])
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
    test_result = main("电脑")
    print("测试结果:")
    print(json.dumps(test_result, indent=2, ensure_ascii=False))