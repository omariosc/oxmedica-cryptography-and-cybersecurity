### Part 1 Instructions

1. **Choose a Component:**
   - Pick a component inside a computer (e.g., GPU, RAM, Hard Drive, Motherboard, Power Supply, etc.), excluding the CPU (as we will use it as an example).

2. **Describe the Component:**
   - Explain the role of the chosen component in the computer system.
   - Describe its inputs and outputs.
   - Identify what other components or systems it interfaces with.


---

### **Chosen Part**: RAM
### **Description**:
- The RAM is for short term memory. It acts as a faster alternative to Hard Drives and SSDs. Random Access Memory is temporary, and is used for quick direct accessing by the CPU.
- When accessed by the CPU, RAM inputs data and instructions from the CPU, and outputs the data (processed) back to the CPU when required
- Other than the CPU, RAM interfaces with the memory controller, storage devices, peripherals (sometimes), and the operating system

---

1. **Logic Gate Question:**
   - Given the following logic gate circuit, describe what it does:
     - A circuit with two inputs (A or B) and an output (Q).
     - The circuit consists of an OR gate followed by a NOT gate.

2. **Truth Table:**
   - Create a truth table for the described logic gate circuit.
   - Include all possible input combinations and the corresponding output.

### Answer:

This circuit has two inputs (A and B) and one output (Q). It is an OR gate followed by a NOT gate.

OR takes two inputs (A and B) and outputs a 1 (true) if at least one of the inputs is 1.
A | B | Output
--|---|-------
0 | 0 | 0
0 | 1 | 1
1 | 0 | 1
1 | 1 | 1

NOT Gate takes 1 input and outputs the opposite of this input.
Input | Output
------|-------
0     | 1
1     | 0

Now, combining these:
- The OR gate outputs 1 if A OR B is 1 (i.e., A = 1 or B = 1).
- The NOT gate then inverts this output.

The resulting circuit implements the NOT OR (NOR) function:
- Q = NOT (A OR B)

Therefore, the output Q will be:
- 1 when both A and B are 0 (because NOT(0 OR 0) = NOT(0) = 1)
- 0 otherwise (when at least one of A or B is 1).

### NOT(OR(A,B))

---