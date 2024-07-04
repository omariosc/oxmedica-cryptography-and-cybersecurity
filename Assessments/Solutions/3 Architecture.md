# 3 Architecture of Computers Assessment Brief

## Overview

Welcome to your third assessment! This exercise is designed to deepen your understanding of computer components and basic logic gates. You will be asked to pick a computer component and explain its role, inputs, outputs, and interfaces. Additionally, you will solve a logic gate question and provide a complete truth table. This assessment should take about 30 minutes to complete.

This is an open-book assessment, so feel free to refer to any resources you find helpful. It is worth 10% of your final grade.

## Part 1: Computer Component

### Part 1 Instructions

1. **Choose a Component:**
I pick the MotherBoard

2. **Describe the Component:**
Explain the role of the chosen component in the computer system.
ANSWER:
The motherboard is one of the most essential components in a computer system, serving as the main circuit board that houses and connects all the crucial components together. Its role can be broken down into several key functions:

Component Integration: The motherboard integrates various components of the computer system, including the CPU (Central Processing Unit), RAM (Random Access Memory), GPU (Graphics Processing Unit), storage drives (HDDs or SSDs), and expansion cards (such as sound cards, network cards, etc.). It provides the physical and electrical connections necessary for these components to communicate with each other.

Data Transfer: The motherboard acts as a hub for data transfer between all connected components. It contains buses (like PCI Express, SATA, USB) that allow data to flow between the CPU, RAM, storage devices, and peripherals.

Power Distribution: The motherboard distributes power from the power supply unit (PSU) to all components connected to it. It ensures that each component receives the correct voltage and current needed for proper operation.

BIOS/UEFI Interface: The motherboard typically contains a BIOS (Basic Input/Output System) or UEFI (Unified Extensible Firmware Interface), which initializes the hardware and provides the basic instructions for booting up the computer. It also manages system settings and configurations.

Expansion Slots: Motherboards feature slots for expansion cards, allowing users to add additional functionality to their systems, such as dedicated graphics cards, sound cards, network adapters, and more.

Form Factor and Compatibility: Motherboards come in different form factors (ATX, microATX, mini-ITX, etc.), determining their size and layout. Compatibility with other components such as the case and power supply unit is crucial for building a functional computer system.

   - Describe its inputs and outputs.
   ANSWER:

   Inputs:

   Power Input:

24-pin ATX Power Connector: This connector receives power from the power supply unit (PSU) to supply the motherboard and its components with the necessary voltage levels.
4-pin or 8-pin CPU Power Connector: Provides additional power specifically to the CPU.

Processor (CPU):

Socket for the CPU: This is where the processor is physically installed on the motherboard. It connects the CPU to the motherboard, providing both electrical connections and mechanical support.

Memory (RAM):

DIMM Slots: These slots receive the RAM modules (memory sticks). They provide electrical connections for the RAM to communicate with the motherboard and the CPU.

Outputs:

Expansion Cards:

Output data to other components or receive data from them, depending on the function of the expansion card.

Input/Output Ports:

Transfer data to and from peripherals connected via USB ports, Ethernet ports, audio jacks, etc.

BIOS/UEFI Configuration:

Output initial system startup information and configurations to ensure proper system initialization.

   - Identify what other components or systems it interfaces with.

### Example Component

**Component:** Central Processing Unit (CPU)

- **Role:** The CPU is the brain of the computer, responsible for executing instructions from programs.
- **Inputs:** Instructions from memory (RAM), data from storage devices.
- **Outputs:** Processed data sent back to memory, signals sent to other components for further actions.
- **Interfaces:** Interfaces with RAM, motherboard, storage devices (HDD/SSD), and peripheral devices through various buses (data, address, control).

## Part 2: Logic Gates and Truth Table

### Part 2 Instructions

1. **Logic Gate Question:**
   - Given the following logic gate circuit, describe what it does:
     - A circuit with two inputs (A and B) and an output (Q).
     - The circuit consists of an AND gate followed by a NOT gate.

2. **Truth Table:**
   - Create a truth table for the described logic gate circuit.
   - Include all possible input combinations and the corresponding output.
   ANSWER:
| A | B | A OR B | NOT(A OR B) | Q |
|---|---|---------|--------------|---|
| 0 | 0 |    0    |      1       | 1 |
| 0 | 1 |    1    |      0       | 0 |
| 1 | 0 |    1    |      0       | 0 |
| 1 | 1 |    1    |      0       | 0 |


<!-- ### Example Logic Gate Circuit

**Logic Gate Circuit:** NOT(AND(A, B))

- **Description:** The circuit takes two inputs, A and B. The AND gate outputs true only if both A and B are true. The NOT gate then inverts this output.
  
**Truth Table:**

| A | B | AND(A, B) | NOT(AND(A, B)) |
|---|---|-----------|----------------|
| 0 | 0 |     0     |        1       |
| 0 | 1 |     0     |        1       |
| 1 | 0 |     0     |        1       |
| 1 | 1 |     1     |        0       | -->

## Submission

- Write your answers in a digital document.
- Include your name at the top of the document.
- Save the file with the name `"3 Architecture Assessment.md"` in the `"Solutions"` folder.

Have fun, and take this opportunity to explore the fascinating world of computer components and logic gates!
