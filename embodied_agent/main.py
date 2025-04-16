#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Embodied Agent with Multimodal LLM and 6-DOF Robotic Arm
This module serves as the main entry point for the embodied agent system that integrates
speech recognition, visual perception, and robotic arm control through large language models.
"""

import os
import sys
import time

# Add the src directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

# Import components
from perception.speech import record, speech_recognition, play_wav, tts
from action.robot_control import back_to_zero, check_camera
from action.actuators import pump_off
from models.llm_interface import SYSTEM_PROMPT
from agent.agent_coordinator import coordinate_actions

def main():
    """
    Main function that orchestrates the embodied agent's perception-action cycle.
    """
    print('\nEmbodied Agent: Listen, See, Act - Multimodal Robotic Control')
    print('Copyright (c) 2025 Zihao Mu, Tongji University\n')

    # Initialize components
    pump_off()
    play_wav('assets/audio/welcome.wav')
    
    # Initialize message history for the agent
    message_history = []
    message_history.append({"role": "system", "content": SYSTEM_PROMPT})
    
    try:
        while True:
            # Reset the robot position
            back_to_zero()
            
            # Get user instruction
            instruction_input = input('Start recording? Enter duration in seconds, k for keyboard input, c for default: ')
            
            # Process the instruction
            if str.isnumeric(instruction_input):
                duration = int(instruction_input)
                record(duration=duration)
                instruction = speech_recognition()
                print(f"Recognized instruction: {instruction}")
            elif instruction_input == 'k':
                instruction = input('Please enter your instruction: ')
            elif instruction_input == 'c':
                instruction = 'First return to zero, then shake head, and put the green block on the basketball'
            else:
                print('No valid instruction provided, exiting')
                raise ValueError('No instruction provided')
            
            # Add user instruction to message history and plan actions
            message_history.append({"role": "user", "content": instruction})
            action_plan = coordinate_actions(message_history)
            
            print('Action plan generated:', action_plan)
            
            # Execute the action plan
            try:
                # Synthesize and play the agent's response
                response = action_plan['response']
                print('Synthesizing speech...')
                tts(response)
                play_wav('temp/tts.wav')
                
                # Execute each function in the action plan
                additional_output = ''
                for action in action_plan['function']:
                    print('Executing action:', action)
                    result = eval(action)  # Execute the action
                    if result is not None:
                        additional_output = result
                
                # Update message history with the action results
                action_plan['response'] += '. ' + additional_output
                message_history.append({"role": "assistant", "content": str(action_plan)})
                
            except Exception as e:
                print(f"Error executing action plan: {e}")
    
    except KeyboardInterrupt:
        print("\nProgram terminated by user")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == '__main__':
    main()
