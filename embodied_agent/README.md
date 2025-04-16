# Listen, See, Act: Building Embodied Agents with Multimodal LLMs and 6-DOF Robotic Arms

This repository contains the code for the paper "Listen, See, Act: Building Embodied Agents with Multimodal LLMs and 6-DOF Robotic Arms" submitted to the Special Issue on 'Artificial Intelligence (AI) and Machine Learning in Mechanical and Industrial Engineering' in Applied Sciences.

## Abstract

This paper presents a novel approach to creating embodied intelligent agents by integrating large language models (LLMs) with multimodal perception and robotic action capabilities. We demonstrate how modern foundation models can serve as the cognitive core for physical robotic systems, enabling natural language control, visual understanding, and coordinated manipulation of objects. Our system leverages a 6-DOF robotic arm as the physical platform, with multimodal LLMs providing the intelligence to process speech commands, interpret visual scenes, and generate appropriate action sequences. We provide experimental results demonstrating the system's ability to interpret complex instructions, adaptively respond to environmental changes, and successfully complete multi-step tasks requiring cross-modal reasoning.

## System Architecture

The system consists of three primary modules:

1. **Perception Module**: Handles processing of sensory inputs through:

   - Speech recognition and synthesis
   - Visual scene understanding and object detection
   - Multimodal integration of sensory information

2. **Cognitive Module**: Serves as the agent's "brain" through:

   - Multiple Large Language Models (OpenAI GPT, Anthropic Claude, Google Gemini, Yi-Large, Qwen-VL)
   - Action planning and sequencing
   - Dynamic response generation

3. **Action Module**: Controls physical interactions through:
   - Robotic arm movement and coordination
   - Actuator control (vacuum pump, LED lights)
   - Teaching mode for demonstration learning

## Supported Language Models

This system supports multiple state-of-the-art language models:

- **Text Models**:

  - OpenAI GPT (4o, 4, 3.5-turbo)
  - Anthropic Claude (3 Opus, 3 Sonnet)
  - Google Gemini (1.5 Pro, 1.5 Flash)
  - Yi Large
  - Baidu ERNIE

- **Vision Models**:
  - OpenAI GPT-4o Vision
  - Google Gemini 1.5 Pro
  - Qwen VL

Models can be selected through configuration or at runtime.

## Requirements

- Python 3.12 or higher
- MyCobot 280 Pi robotic arm
- Raspberry Pi 4B with Ubuntu 20.04
- Camera module
- Vacuum pump attachment
- API keys for supported language models

Detailed software dependencies are listed in `requirements.txt`.

## Installation

1. Clone this repository:

```bash
git clone https://github.com/username/multimodal-embodied-agent.git
cd multimodal-embodied-agent
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Configure your API keys:

   - Copy `config.py.example` to `config.py` (if available)
   - Add your API keys to the configuration
   - Alternatively, set environment variables for API keys

## Usage

Run the main program:

```bash
python main.py
```

When prompted:

- Enter a number to record audio for that many seconds
- Type 'k' to input a text command manually
- Type 'c' to use a default command

### Model Selection

To select which language model to use:

```bash
# Set in environment
export DEFAULT_TEXT_MODEL=openai  # Options: openai, claude, gemini, yi, qianfan
export DEFAULT_VISION_MODEL=qwen  # Options: openai, gemini, qwen

# Or modify in config.py
```

## Project Structure

```
embodied_agent/
├── main.py                      # Main program entry point
├── config.py                    # Configuration file
├── requirements.txt             # Dependencies
├── README.md                    # Project documentation
├── assets/                      # Static resources
│   ├── fonts/                   # Font files
│   └── audio/                   # Audio files
├── temp/                        # Temporary files directory
└── src/                         # Source code
    ├── agent/                   # Agent-related code
    │   ├── agent_coordinator.py # Agent coordination
    │   └── prompts.py           # System prompts
    ├── perception/              # Perception system
    │   ├── speech.py            # Speech processing
    │   ├── vision.py            # Visual processing
    │   └── multimodal.py        # Multimodal integration
    ├── action/                  # Action system
    │   ├── robot_control.py     # Robotic arm control
    │   ├── actuators.py         # Actuator control
    │   └── teaching.py          # Teaching mode
    └── models/                  # Model interfaces
        └── llm_interface.py     # LLM API integration
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.
