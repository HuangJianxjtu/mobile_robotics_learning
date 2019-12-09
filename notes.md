# Notes for Mobile Robotics

## 1. ICC

ICC -- Instantaneous Center of Curvature(瞬心)

## 2. Holonomic and non-holonomic constraint

holonomic constraint -- 完整约束

Holonomic 完整性约束机器人是指 机器人总自由度等于可控自由度。而Non-holonomic 非完整性约束是指 可控自由度小于机器人总自由度。通常地面机器人的自由度为3，包括x,y与朝向。对于角轮（castor wheels）或者是全向轮（Omni-wheels）的机器人，是holonomic的，因为它能够朝各个方向移动，并且机器人总自由度与可控自由度是相等的。但是类似于车辆这种结构，其可控的自由度为2，包括：油门/刹车和方向盘转角。使得它难以满足任何方向的行驶（除非车辆发生打滑或侧滑），所以是非完整性约束。
