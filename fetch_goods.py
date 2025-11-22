import json

def main(goodsKeyword):
    """
    根据商品关键词搜索产品列表
    """
    # data 只包含数组
    data = [
        {
            "productId": 226,
            "productName": "iPhone 13 双卡双待 128G 全网通 5G手机",
            "productSn": "SN000226",
            "productTsn": "0",
            "picThumb": "https://*.com/upload/202511/1714976196IC85msMEaqPFZW8K3f.png",
            "productStock": 500,
            "productPrice": "4849.00",
            "marketPrice": "5999.00",
            "productStatus": "1",
            "productType": "1",
            "categoryId": "421",
            "brandId": "116",
            "shopId": "0",
            "keywords": "iPhone 13 双卡 双待 128G 全 网通 5G 手机",
            "checkStatus": "1",
            "clickCount": 111,
            "productWeight": "0.000",
            "isPromote": "0",
            "isPromoteActivity": "0",
            "promotePrice": "0.00",
            "promoteStartDate": "2025-11-17 11:11:11",
            "promoteEndDate": "2025-11-27 11:11:11",
            "productBrief": "iPhone 13",
            "productDesc": "iPhone 13........",
            "commentTag": "",
            "freeShipping": "0",
            "addTime": "2025-11-17 10:11:11",
            "sortOrder": "100",
            "isDelete": "0",
            "isBest": "0",
            "isNew": "0",
            "isHot": "1",
            "limitNumber": "0",
            "isSupportReturn": "0",
            "isSupportCod": "1",
            "skuValue": "颜色:红色|内存:128g",
            "skuData": [
                {
                    "name": "颜色",
                    "value": "红色"
                },
                {
                    "name": "内存",
                    "value": "128g"
                }
            ]
        },
        {
            "productId": 227,
            "productName": "iPhone 13 双卡双待 256G 全网通 5G手机",
            "productSn": "SN000227",
            "productTsn": "0",
            "picThumb": "https://*.com/upload/202511/1714976196IC85msMEaqPFZW8K3f.png",
            "productStock": 300,
            "productPrice": "5849.00",
            "marketPrice": "6999.00",
            "productStatus": "1",
            "productType": "1",
            "categoryId": "421",
            "brandId": "116",
            "shopId": "0",
            "keywords": "iPhone 13 双卡 双待 256G 全 网通 5G 手机",
            "checkStatus": "1",
            "clickCount": 89,
            "productWeight": "0.000",
            "isPromote": "0",
            "isPromoteActivity": "0",
            "promotePrice": "0.00",
            "promoteStartDate": "2025-11-17 11:11:11",
            "promoteEndDate": "2025-11-27 11:11:11",
            "productBrief": "iPhone 13",
            "productDesc": "iPhone 13........",
            "commentTag": "",
            "freeShipping": "0",
            "addTime": "2025-11-17 10:11:11",
            "sortOrder": "100",
            "isDelete": "0",
            "isBest": "0",
            "isNew": "0",
            "isHot": "1",
            "limitNumber": "0",
            "isSupportReturn": "0",
            "isSupportCod": "1",
            "skuValue": "颜色:蓝色|内存:256g",
            "skuData": [
                {
                    "name": "颜色",
                    "value": "蓝色"
                },
                {
                    "name": "内存",
                    "value": "256g"
                }
            ]
        }
    ]
    
    # 返回 result: json.dumps(data, ensure_ascii=False)
    return {
        "result": json.dumps(data, ensure_ascii=False)
    }