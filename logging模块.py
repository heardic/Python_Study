import logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d',
)


# --- 使用日志 ---
logging.info("程序启动")
logging.warning("系统资源紧张")  # 会显示 WARNING
logging.error("数据库连接失败")   # 会显示 ERROR