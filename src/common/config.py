# -*- coding: utf-8 -*-

import os
import sys
import json
from typing import Any, Dict, List, Optional
from PySide6.QtCore import QObject, Signal, Slot

class Config(QObject):
    _instance: Optional['Config'] = None
    _config: Dict[str, Any] = {}

    configChanged = Signal(str, Any)

    def __new__(cls) -> 'Config':
        if cls._instance is None:
            cls._instance = super(Config, cls).__new__(cls)
            cls._instance._initialize()
        return cls._instance

    def _initialize(self) -> None:
        super().__init__()
        if getattr(sys, 'frozen', False):
            self.app_dir = os.path.dirname(sys.executable)
        else:
            self.app_dir = os.path.dirname(os.path.abspath(sys.argv[0]))

        self.app_config_file = os.path.join(self.app_dir, 'config.json')
        self.local_config_dir = os.path.join(os.getenv('LOCALAPPDATA', ''), 'jbs')
        self.local_config_file = os.path.join(self.local_config_dir, 'config.json')

        self._load_config()

    def _load_config(self) -> None:
        for config_path in [self.local_config_file, self.app_config_file]:
            if os.path.exists(config_path):
                try:
                    with open(config_path, 'r', encoding='utf-8') as f:
                        self._config = json.load(f)
                        self.active_config_file = config_path
                        return
                except (json.JSONDecodeError, IOError) as e:
                    print(f"Error loading {config_path}: {e}")

        self.active_config_file = self.local_config_file
        self._create_default_config()

    def _create_default_config(self) -> None:
        """创建默认配置文件。"""
        self._config = {
            "version": "",
            "settings": {
                "theme": "auto"
            }
        }

        self.save()

    @Slot(str, result=Any)
    def get(self, *keys: str) -> Any:
        """获取配置值。"""
        value = self._config
        for key in keys:
            if not isinstance(value, dict):
                return None
            value = value.get(key)
            if value is None:
                return None
        return value

    @Slot(*['str'] * 5)  # 这里我们假设最多支持5层嵌套
    def set(self, *args: Any) -> None:
        if len(args) < 2:
            raise ValueError("At least one key and a value are required")

        keys = args[:-1]
        value = args[-1]

        self._set_config_value(keys, value)
        self.save()

    def _set_config_value(self, keys: List[str], value: Any) -> None:
        config = self._config
        for key in keys[:-1]:
            config = config.setdefault(key, {})

        if config.get(keys[-1]) != value:
            config[keys[-1]] = value
            self._emit_config_changed(keys, value)

    def _emit_config_changed(self, keys: List[str], value: Any) -> None:
        self.configChanged.emit('.'.join(keys), value)

    @Slot()
    def save(self) -> None:
        os.makedirs(os.path.dirname(self.active_config_file), exist_ok=True)

        try:
            with open(self.active_config_file, 'w', encoding='utf-8') as f:
                json.dump(self._config, f, indent=4)
        except IOError as e:
            raise IOError(f"Failed to save config file: {e}")

    @property
    def all(self) -> Dict[str, Any]:
        return self._config.copy()

    @property
    def config_path(self) -> str:
        return self.active_config_file
