import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.path import Path
import numpy as np

# Font settings - use system default font
# Reset font settings to defaults to avoid font-related errors
plt.rcParams.update(plt.rcParamsDefault)

# Create figure and axes
fig, ax = plt.subplots(figsize=(14, 10))
ax.axis('off')  # Hide axes

# Set colors
colors = {
    'input': '#D4F1F9',       # Light blue
    'perception': '#DAEEC7',   # Light green
    'fusion': '#E6E6FA',       # Light purple
    'llm': '#FFE5CC',          # Light orange
    'planning': '#FFF9C4',     # Light yellow
    'execution': '#E8E8E8',    # Light gray
    'border': '#555555',       # Border color
    'arrow': '#2F4F4F',        # Arrow color
    'feedback': '#AA4444',     # Feedback arrow color
}

# Architecture layer height and width
layer_height = 1.2
layer_width = 12
spacing = 0.3
component_height = 0.8
component_width = 3

# Y-axis positions (top to bottom)
y_positions = {
    'input': 9,
    'perception': 7,
    'fusion': 5,
    'llm': 3,
    'planning': 1,
    'execution': -1,
}

# Draw background and title for each layer
def draw_layer(name, y_pos, color, title):
    rect = patches.Rectangle((-layer_width/2, y_pos-layer_height/2), 
                            layer_width, layer_height, 
                            linewidth=1, edgecolor=colors['border'], 
                            facecolor=color, alpha=0.3,
                            zorder=1)
    ax.add_patch(rect)
    ax.text(-layer_width/2+0.2, y_pos+layer_height/2-0.3, title, fontsize=12, fontweight='bold')

# Draw components
def draw_component(x, y, width, height, title, details=None, color=None):
    if color is None:
        color = '#FFFFFF'
    
    rect = patches.Rectangle((x-width/2, y-height/2), 
                            width, height, 
                            linewidth=1, edgecolor=colors['border'], 
                            facecolor=color, alpha=0.7,
                            zorder=2)
    ax.add_patch(rect)
    
    # Add title
    ax.text(x, y+height/4, title, fontsize=10, ha='center', fontweight='bold')
    
    # Add details
    if details:
        details_y = y - 0.05
        for detail in details:
            ax.text(x, details_y, detail, fontsize=8, ha='center', style='italic')
            details_y -= 0.15

# Draw arrow connections
def draw_arrow(start_x, start_y, end_x, end_y, color=None, feedback=False):
    if color is None:
        color = colors['arrow']
    
    # Using Bezier curves to draw arrows
    if feedback:
        # Feedback arrow (dashed line)
        control_x = end_x + abs(end_x - start_x) * 0.5
        verts = [
            (start_x, start_y),
            (control_x, start_y),
            (control_x, end_y),
            (end_x, end_y)
        ]
        codes = [Path.MOVETO, Path.CURVE4, Path.CURVE4, Path.CURVE4]
        path = Path(verts, codes)
        patch = patches.PathPatch(path, facecolor='none', edgecolor=color, linestyle='--', lw=1, zorder=1)
    else:
        # Regular arrow
        dx = end_x - start_x
        dy = end_y - start_y
        
        # If vertical connection
        if abs(dx) < 0.1:
            verts = [(start_x, start_y), (end_x, end_y)]
            codes = [Path.MOVETO, Path.LINETO]
        else:
            # Horizontal or diagonal connection
            mid_y = start_y + dy/2
            verts = [
                (start_x, start_y),
                (start_x, mid_y),
                (end_x, mid_y),
                (end_x, end_y)
            ]
            codes = [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO]
        
        path = Path(verts, codes)
        patch = patches.PathPatch(path, facecolor='none', edgecolor=color, lw=1, zorder=1)
    
    ax.add_patch(patch)
    
    # Arrow head
    head_length = 0.15
    head_width = 0.1
    
    # Determine arrow direction
    if feedback:
        dx = end_x - verts[-2][0]
        dy = end_y - verts[-2][1]
    else:
        if len(verts) > 2:
            dx = end_x - verts[-2][0]
            dy = end_y - verts[-2][1]
        else:
            dx = end_x - start_x
            dy = end_y - start_y
    
    # Normalize direction vector
    length = np.sqrt(dx**2 + dy**2)
    if length > 0:
        dx = dx / length
        dy = dy / length
    
    # Draw arrow head
    arrow = patches.FancyArrow(end_x-dx*head_length, end_y-dy*head_length, 
                              dx*head_length, dy*head_length,
                              width=head_width, head_width=3*head_width, 
                              length_includes_head=True, 
                              facecolor=color, edgecolor=color, zorder=3)
    ax.add_patch(arrow)

# Draw all layers
for name, y_pos in y_positions.items():
    draw_layer(name, y_pos, colors[name], {
        'input': 'Input Layer',
        'perception': 'Perception Layer',
        'fusion': 'Multimodal Fusion Layer',
        'llm': 'LLM Reasoning Layer',
        'planning': 'Execution Planning Layer',
        'execution': 'Physical Execution Layer',
    }[name])

# Draw input layer components
draw_component(-3, y_positions['input'], component_width, component_height, 
              "Speech Input", ["Local ASR Engine", "Chinese/English Recognition", "WER<5%"], colors['input'])
draw_component(3, y_positions['input'], component_width, component_height, 
              "Visual Input", ["720p HD Camera", "30fps Real-time Acquisition"], colors['input'])

# Draw perception layer components
draw_component(-3, y_positions['perception'], component_width, component_height, 
              "Speech Recognition Module", ["Instruction Parsing", "WER<5%"], colors['perception'])
draw_component(3, y_positions['perception'], component_width, component_height, 
              "Visual Processing Module", ["OpenCV Object Detection", "Position Tracking"], colors['perception'])
draw_component(0, y_positions['perception']-0.7, component_width, 0.6, 
              "Queue Buffer Mechanism", ["Multimodal Input Synchronization"], colors['perception'])

# Draw fusion layer components
draw_component(-3, y_positions['fusion'], component_width, component_height, 
              "Text Embedding", ["Language Feature Extraction", "Instruction Semantic Understanding"], colors['fusion'])
draw_component(3, y_positions['fusion'], component_width, component_height, 
              "Visual Embedding", ["Scene Feature Extraction", "Object Feature Extraction"], colors['fusion'])
draw_component(0, y_positions['fusion']-0.7, component_width, 0.6, 
              "Multimodal Context Integration", ["Vision-Language Alignment", "Unified Vector Representation"], colors['fusion'])

# Draw LLM reasoning layer components
draw_component(0, y_positions['llm'], 4.5, component_height, 
              "Inference Engine (GPT-4o/Claude-3-Opus)", ["750ms Average Inference Time"], colors['llm'])
draw_component(-4, y_positions['llm'], component_width, component_height, 
              "System Prompt", ["Context Optimization", "Physical Constraint Understanding"], colors['llm'])
draw_component(4, y_positions['llm'], component_width, component_height, 
              "JSON Action Plan Generation", ["Structured Action Planning", "Execution Parameterization"], colors['llm'])

# Draw planning layer components
draw_component(-4, y_positions['planning'], component_width, component_height, 
              "Inverse Kinematics", ["Spatial Coordinates to Joint Angles"], colors['planning'])
draw_component(0, y_positions['planning'], component_width, component_height, 
              "Collision Detection", ["Safe Path Validation", "Obstacle Avoidance"], colors['planning'])
draw_component(4, y_positions['planning'], component_width, component_height, 
              "Path Planning", ["Smooth Trajectory Generation", "Speed/Force Configuration"], colors['planning'])

# Draw execution layer components
draw_component(-4, y_positions['execution'], component_width, component_height, 
              "Robotic Arm Control", ["6-DOF Precise Control", "Pymycobot API", "±0.5mm Joint Precision"], colors['execution'])
draw_component(0, y_positions['execution'], component_width, component_height, 
              "Vacuum Pump Control", ["0.1MPa Suction", "Object Grasping & Release"], colors['execution'])
draw_component(4, y_positions['execution'], component_width, component_height, 
              "LED Feedback System", ["Visual Status Indication", "GPIO Control"], colors['execution'])

# Draw connection arrows
# Input layer -> Perception layer
draw_arrow(-3, y_positions['input']-component_height/2, -3, y_positions['perception']+component_height/2)
draw_arrow(3, y_positions['input']-component_height/2, 3, y_positions['perception']+component_height/2)

# Perception layer -> Queue Buffer
draw_arrow(-3, y_positions['perception']-component_height/2, -1.5, y_positions['perception']-0.7)
draw_arrow(3, y_positions['perception']-component_height/2, 1.5, y_positions['perception']-0.7)

# Queue Buffer -> Fusion layer
draw_arrow(0, y_positions['perception']-0.7-0.3, -3, y_positions['fusion']+component_height/2)
draw_arrow(0, y_positions['perception']-0.7-0.3, 3, y_positions['fusion']+component_height/2)

# Fusion layer -> Multimodal Context Integration
draw_arrow(-3, y_positions['fusion']-component_height/2, -1.5, y_positions['fusion']-0.7)
draw_arrow(3, y_positions['fusion']-component_height/2, 1.5, y_positions['fusion']-0.7)

# Multimodal Context Integration -> LLM Reasoning layer
draw_arrow(0, y_positions['fusion']-0.7-0.3, 0, y_positions['llm']+component_height/2)
# System Prompt -> LLM Inference Engine
draw_arrow(-4, y_positions['llm'], -2.25, y_positions['llm'])
# LLM Inference Engine -> JSON Output
draw_arrow(2.25, y_positions['llm'], 4, y_positions['llm'])

# LLM Reasoning layer -> Execution Planning layer
draw_arrow(4, y_positions['llm']-component_height/2, 4, y_positions['planning']+component_height/2)
draw_arrow(4, y_positions['llm']-component_height/2, 0, y_positions['planning']+component_height/2)
draw_arrow(4, y_positions['llm']-component_height/2, -4, y_positions['planning']+component_height/2)

# Internal connections within Execution Planning layer
draw_arrow(-4, y_positions['planning']-component_height/2, -4, y_positions['planning']-0.7)
draw_arrow(0, y_positions['planning']-component_height/2, 0, y_positions['planning']-0.7)
draw_arrow(-4, y_positions['planning']-0.7, 4, y_positions['planning']-0.7)
draw_arrow(0, y_positions['planning']-0.7, 4, y_positions['planning']-0.7)
draw_arrow(4, y_positions['planning']-component_height/2, 4, y_positions['planning']-0.7)

# Execution Planning layer -> Physical Execution layer
draw_arrow(4, y_positions['planning']-0.7-0.3, 4, y_positions['execution']+component_height/2)
draw_arrow(4, y_positions['planning']-0.7-0.3, 0, y_positions['execution']+component_height/2)
draw_arrow(4, y_positions['planning']-0.7-0.3, -4, y_positions['execution']+component_height/2)

# Feedback loop
draw_arrow(-4, y_positions['execution']-component_height/2, -5.5, y_positions['execution']-component_height/2-0.3, colors['feedback'], True)
draw_arrow(-5.5, y_positions['execution']-component_height/2-0.3, -5.5, y_positions['perception']+component_height/2+0.3, colors['feedback'], True)
draw_arrow(-5.5, y_positions['perception']+component_height/2+0.3, 3, y_positions['perception']+component_height/2, colors['feedback'], True)

# Add chart title
ax.text(0, 10.5, "Multimodal LLM-Driven Robot Control System Architecture", fontsize=16, ha='center', fontweight='bold')

# Add legend
legend_elements = [
    patches.Patch(facecolor=colors['input'], edgecolor='k', alpha=0.3, label='Input Layer'),
    patches.Patch(facecolor=colors['perception'], edgecolor='k', alpha=0.3, label='Perception Layer'),
    patches.Patch(facecolor=colors['fusion'], edgecolor='k', alpha=0.3, label='Multimodal Fusion Layer'),
    patches.Patch(facecolor=colors['llm'], edgecolor='k', alpha=0.3, label='LLM Reasoning Layer'),
    patches.Patch(facecolor=colors['planning'], edgecolor='k', alpha=0.3, label='Execution Planning Layer'),
    patches.Patch(facecolor=colors['execution'], edgecolor='k', alpha=0.3, label='Physical Execution Layer'),
    patches.Patch(facecolor='none', edgecolor=colors['arrow'], label='Data Flow'),
    patches.Patch(facecolor='none', edgecolor=colors['feedback'], linestyle='--', label='Feedback Loop')
]
ax.legend(handles=legend_elements, loc='upper center', bbox_to_anchor=(0.5, -0.05), 
          ncol=4, fancybox=True, shadow=True)

# Add caption
ax.text(-5.8, -1.8, "Fig 2: Multimodal LLM-Driven Robot Control System Architecture, showing perception, reasoning, and execution modules and their interrelations", 
        fontsize=9, style='italic')

# 设置坐标轴范围
ax.set_xlim(-layer_width/2-1, layer_width/2+1)
ax.set_ylim(-2.5, 11)

plt.tight_layout()
plt.savefig('system_architecture.png', dpi=300, bbox_inches='tight')
plt.show()
