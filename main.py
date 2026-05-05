# -*- coding: utf-8 -*-
"""
AutoEq REST API 启动入口

使用方法:
    python main.py

访问地址:
    - API文档: http://localhost:8000/docs (Swagger UI)
    - ReDoc: http://localhost:8000/redoc
"""

import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        "autoeq.rest_api:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )
