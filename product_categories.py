#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import json
from typing import Dict, Any

def fetch_product_categories():
    """
    获取商品分类树

    Returns:
        Any: API响应数据或错误信息
    """
    url = "http://shopadmin.frp.hngfjh.com/openApi/product/getProductCategoryTree"

    headers = {
        'token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1dWlkIjoiZjhjMmNhODIyNzIyNGUzNzllYjZjZjNlMDAwNTU3ZmYiLCJhcHBJZCI6IjllYzdiZTQ2MjkxNDQ1YmZmOGE1Nzk2MzdjZDdlNDdiIiwidGltZSI6MTc2NDIxMjU2Mn0.LHCUCzfbnYFbw3UzZ8YHoA2KD_A09mniuQfbFjgyO7E',
        'Content-Type': 'application/json'
    }

    payload = {
        "page": 1,
        "size": 100
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

def main():
    """
    主函数 - 获取商品分类并返回分类列表

    Returns:
        List: 包含categoryId和categoryName的字典列表
    """
    # 获取商品分类数据
    categories_result = fetch_product_categories()
    data = []
    try:
        if isinstance(categories_result, dict) and categories_result.get("code") == 200 and "data" in categories_result:
            records = categories_result["data"].get("records", [])
            data = [
                {
                    "categoryId": record.get("categoryId"),
                    "categoryName": record.get("categoryName")
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
    test_result = main()
    print("测试结果:")
    print(json.dumps(test_result, indent=2, ensure_ascii=False))