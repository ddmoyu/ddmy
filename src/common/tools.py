import os
import json
import logging
from pathlib import Path

file_dir = Path(os.getenv("APPDATA", "")) / "ddmy"
log_file = file_dir / "app.log"


def setup_logging():
    file_dir.mkdir(parents=True, exist_ok=True)
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler(log_file, encoding="utf-8"),
            logging.StreamHandler(),
        ],
    )


def save_json(data, json_file_name):
    try:
        file_path = file_dir / json_file_name
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, default=str, ensure_ascii=False, indent=4)
            logging.info(f"数据成功写入到 {file_path}")
    except PermissionError:
        logging.error("权限错误：没有权限写入文件。")
    except IOError:
        logging.error("I/O 错误：文件写入失败。")
    except TypeError:
        logging.error("类型错误：提供的数据无法被序列化为 JSON。")
    except Exception as e:
        logging.error(f"发生未知错误：{e}")


def load_json(json_file_name):
    try:
        with open(file_dir / json_file_name, "r", encoding="utf-8") as f:
            if f.read() == "":
                return []
            f.seek(0)
            return json.load(f)
    except FileNotFoundError:
        logging.warning("文件未找到错误：指定的文件路径不存在。")
        return []
    except json.JSONDecodeError:
        logging.error("JSON 解析错误：文件格式不正确。")
        return []
    except Exception as e:
        logging.error(f"发生未知错误：{e}")
        return []
