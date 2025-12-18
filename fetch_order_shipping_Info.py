#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import json
from typing import Dict, Any

def fetch_order_shipping_info(orderId: str):
    """
    获取订单物流信息

    Returns:
        Any: API响应数据或错误信息
    """
    url = "http://192.168.64.4:9010/openApi/getShippingInfo"

    headers = {
        'Content-Type': 'application/json'
    }

    url = url + f"?orderId={orderId}"

    try:
        response = requests.get(url, headers=headers, timeout=5)
        response.raise_for_status()
        return response.json()

    except requests.exceptions.RequestException as e:
        return {"error": f"请求失败: {str(e)}"}
    except json.JSONDecodeError as e:
        return {"error": f"JSON解析失败: {str(e)}"}
    except Exception as e:
        return {"error": f"未知错误: {str(e)}"}

def main(orderId: str):
    """
    主函数 - 查询订单物流信息并返回结果

    Returns:
        List: 包含categoryId和categoryName的字典列表
    """
    # 获取订单物流信息
    fetch_order_shipping_info_result = fetch_order_shipping_info(orderId)
    print("获取的订单物流信息:", fetch_order_shipping_info_result)
    data = []
    try:
        if isinstance(fetch_order_shipping_info_result, dict) and fetch_order_shipping_info_result.get("code") == 200 and "result" in fetch_order_shipping_info_result:
            data = fetch_order_shipping_info_result["result"]
        else:
            data = {}
    except Exception:
        data = {}

    return {
        "result": json.dumps(data, ensure_ascii=False)
    }
if __name__ == "__main__":
    # 测试代码
    test_result = main("2d0ecf70a923342ff5d1900571b7263b")
    print("测试结果:")
    print(json.dumps(test_result, indent=2, ensure_ascii=False))