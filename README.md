# Autonomous System with MAPE-K Loop

## Overview
This project implements an autonomous software system based on the MAPE-K loop (Monitor, Analyze, Plan, Execute, Knowledge). The system is designed to manage resources by monitoring environmental parameters and automatically adapting to changing conditions.

## Features
- **Monitoring**: Detecting environmental parameters using sensors.
- **Analysis**: Analyzing collected data to identify anomalies or intervention needs.
- **Planning**: Defining corrective actions to optimize system conditions.
- **Execution**: Applying decisions through actuators.
- **Knowledge**: Storing data to improve future decisions.

## System Goals
The system can be configured to manage various environmental aspects, including:
- Energy consumption
- Temperature
- Lighting
- Humidity

## Architecture
The architecture follows the autonomous management model discussed in the course materials, adopting:
- **A single autonomic manager** for the entire system
- **Multiple localized managers** for distributed decision-making (if applicable)

## Sensors & Effectors
- **Sensors**: Detect the specified environmental parameters.
- **Effectors**: Apply changes, such as adjusting heating, smart lights, and smart windows.

## Decision Function
The autonomic manager can use different strategies to make decisions, including:
- Rule-based decision-making
- Search-based optimization algorithms
- Artificial intelligence (if implemented)
