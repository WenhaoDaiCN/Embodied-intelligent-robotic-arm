#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Configuration file for the Embodied Agent system.

This module contains API keys and configuration parameters for various
components of the system. In a production environment, these should be
stored more securely.

Author: Zihao Mu (Shanghai Tongji University)
Date: 2025-04-16
"""

import os
from typing import Dict, Any

# Function to load API keys from environment variables with fallback to defaults
def get_env_var(var_name: str, default: str) -> str:
    return os.environ.get(var_name, default)

# ==================== LLM API Keys ====================

# OpenAI API (GPT models)
# https://platform.openai.com/
OPENAI_API_KEY = get_env_var("OPENAI_API_KEY", "sk-XXXXXXXXXXXXXXXXXXXXXXXX")
OPENAI_ORG_ID = get_env_var("OPENAI_ORG_ID", "")  # Optional

# Anthropic API (Claude models)
# https://console.anthropic.com/
ANTHROPIC_API_KEY = get_env_var("ANTHROPIC_API_KEY", "sk-ant-XXXXXXXXXXXXX")

# Google AI Studio (Gemini models)
# https://aistudio.google.com/
GOOGLE_API_KEY = get_env_var("GOOGLE_API_KEY", "XXXXXXXXXXXXXXXXXXXXXXXX")

# Qwen VL Series API (Aliyun Bailian)
# https://bailian.console.aliyun.com/#/model-market
QWEN_API_KEY = get_env_var("QWEN_API_KEY", "f8144ffaff7c459791XXXXXXXXX")

# Yi Large Language Model API
# https://platform.lingyiwanwu.com
YI_API_KEY = get_env_var("YI_API_KEY", "f8144ffaff7c459791XXXXXXXXX")

# Baidu Qianfan ModelBuilder API
# https://qianfan.cloud.baidu.com
QIANFAN_ACCESS_KEY = get_env_var("QIANFAN_ACCESS_KEY", "ALTAKRELRxSXXXXXXXXXX")
QIANFAN_SECRET_KEY = get_env_var("QIANFAN_SECRET_KEY", "3737d9da82de4f2XXXXXXXXXX")

# Baidu Qianfan AppBuilder-SDK
APPBUILDER_TOKEN = get_env_var("APPBUILDER_TOKEN", "bce-v3/ALTAK-7jr20xkZl4cDmhbQKA4ml/f560e5dc3XXXXXXX059XXXXXXXXX")

# Default LLM to use (can be changed at runtime)
DEFAULT_TEXT_MODEL = get_env_var("DEFAULT_TEXT_MODEL", "openai")  # Options: openai, claude, gemini, yi, qianfan
DEFAULT_VISION_MODEL = get_env_var("DEFAULT_VISION_MODEL", "qwen")  # Options: openai, gemini, qwen

# ==================== Robot Configuration ====================

ROBOT_CONFIG = {
    "safe_height": 220,         # Safe height for arm movement
    "default_speed": 40,        # Default movement speed
    "coordinate_speed": 20,     # Speed for coordinate-based movement
    "default_gripper_angle": 90 # Default gripper angle
}

# ==================== System Paths ====================

PATHS = {
    "temp_dir": "temp/",
    "assets_dir": "assets/",
    "audio_dir": "assets/audio/",
    "fonts_dir": "assets/fonts/"
}

# ==================== Audio Configuration ====================

AUDIO_CONFIG = {
    "mic_index": 1,            # Default microphone index
    "sample_rate": 16000,      # Audio sample rate
    "quiet_threshold": 700,    # Threshold for silence detection
    "channels": 1,             # Audio channels
    "chunk_size": 1024         # Audio chunk size
}
