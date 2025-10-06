# SYST 210: System Design - Class 09: Functional Architecture

**Instructor:** Dr. Ali K. Raz  
**Institution:** George Mason University, SEOR Department

## Learning Objectives

- Define a functional architecture
- From a system concept and requirements, develop a functional architecture
  - Functional decomposition
  - Input/Output Functions
  - Tracing requirements (covered next week)

## Structure of the System Design Process

The functional architecture development fits within the broader system design process:

```
System Statement of Need + Stakeholder Analysis
                ↓
    Define System-level Design Problem
                ↓
    ┌─────────────────────────┐
    │ Develop Functional      │ ← Current Focus
    │ Architecture            │
    └─────────────────────────┘
                ↓
    Develop Physical Architecture
                ↓
    Develop Allocated Architecture
                ↓
    Develop Interface Architecture → Develop Qualification System
```

## What is a Function?

### Mathematical Function
- Basic form: `Y = f(x)` or `Y = f(x) = mx + b`

### System Functions
System functions transform inputs into outputs through various mechanisms:

```
┌─────────┐     Transformation,      ┌─────────┐
│ INPUTS  │     Controls,            │ OUTPUTS │
│ • Data  │ ─────────────────────→   │ • Data  │
│ • Signal│     Mechanisms           │ • Signal│
│ • Energy│                          │ • Energy│
│ • Matter│                          │ • Matter│
└─────────┘                          └─────────┘
```

## System Functions Characteristics

- **Definition:** Individual operations and transformations contributing to overall system purpose
- **Expression:** Usually (verb, noun) pairs
  - Example: "Transport passengers"
- **Purpose:** Functions are defined to meet system requirements
  - Derived from operational concept analysis and originating requirements

### Important Distinctions

- **Function ≠ Form**
  - Form = physical elements (parts, components, subassemblies)
  - Functions = what the system does
  - Form implements functions
- Functions combine to create a **function structure**
- Each function doesn't necessarily map 1:1 to subsystems
  - "Functions are not a function of subsystems" (math joke alert!)

## Useful Terminology

| Term | Definition |
|------|------------|
| **Function** | Process that transforms inputs into outputs |
| **Functionality** | Capability to produce a desired output (to meet system purpose) |
| **State** | Static snapshot of all variables needed to describe the system's capabilities to perform functions |
| **Mode** | Distinct manner of operating the system; some or all functions may be performed to some degree |

### Example: Vending Machine
- **Function:** Dispense products, Accept payment, Provide change
- **Functionality:** Ability to vend specific items
- **State:** Current inventory levels, money inserted, selected item
- **Mode:** Ready mode, Transaction mode, Maintenance mode, Out-of-service mode

## Functional Architecture Components

A functional architecture provides three main elements:

### 1. Functional Decomposition
- Hierarchical decomposition of system top-level functions
- Identifies what the functions are

### 2. Data Model
- Specifies inputs and outputs of functions
  - Data, Signal, Energy, and Matter
- How inputs and outputs are connected

### 3. Requirement Tracing
- Functions, inputs, and outputs traced to requirements they satisfy
- Provides opportunity to derive system-level requirements
- Identifies new requirements

## Example: Coffee Maker Functional Architecture

### Top-Level Function: Brew Coffee

### Functional Decomposition:

```
                    Brew Coffee
                         │
        ┌────────────────┼────────────────┐
        │                │                │
   Store Water      Mix Coffee        Heat Coffee
        │           and Water              │
   Heat Water           │            Store Coffee
                        │
                  Store Grounds
                        ↑
                  Grind Beans
```

### Supporting Sub-Functions:
- Store Water
- Heat Water
- Mix Coffee and Water
- Heat Coffee
- Store Coffee
- Store Grounds

### Auxiliary Functions:
- Grind Beans
- Shut-off Heater

## Functional Decomposition Rules

### Rules for Function Hierarchy:
- **No Function is Repeated**
- **Functions should have clear boundaries**
- **Functions should be labeled with "verb and noun"**

### How Far to Decompose?
- Depends on scope and intended audience
- No single right answer
- Stop when sufficient detail for purpose

### How to Choose Sub-functions:
- Clear and easy to understand
- Well-defined interfaces with other sub-functions
- Input/output structures consistently defined
- No single right answer - iterative process

## Approaches to Identify Functions

### How to Identify Functions and Decompose:
1. **Consider operational scenarios**
2. **Examine inputs and outputs** at top level
3. **Decompose** to next level of detail on transformation
4. **Consider fundamental and auxiliary functions**

### Templates Available:

#### 1. Hatley-Pirbhai Template
Generic pattern of six sub-functions for any function:
- Provide User Interface
- Transform Inputs into Outputs
- Format Outputs
- Prepare Inputs
- Control Execution
- Enable Maintenance, Conduct Self-Test, Manage Redundancy Processing

**Note:** Not all sub-functions need to be present; most useful at top levels

#### 2. Living Systems Template (Miller's 19 Subsystems)

**Categories:**
- Systems processing matter-energy and information:
  - Reproducer, Boundary
- Systems processing matter-energy:
  - Ingestor, Distributer, Converter, Producer, Matter/Energy Storage, Extruder, Motor
- Systems processing information:
  - Input transducer, Internal transducer, Channel and net, Decoder, Associator, Memory, Decider, Encoder, Output transducer

**Hypothesis:** These 19 subsystems are important to human-designed systems as well

### Creative Process
- Brainstorming techniques (covered later in semester)

## Decomposition vs. Composition

### Decomposition (Top-Down)
- Start at highest level for system purpose/objective
- Partition system function one level at a time
- Need sound definitions of all inputs/outputs

### Composition (Bottom-Up)
- Define many functionalities (bottom-level functions)
- Synthesize functional hierarchy from bottom-level functions

**Best Practice:** Use combination of both approaches

## Functional Flow Diagrams

Transition from hierarchical decomposition to flow diagrams showing data connections:

```
Function Hierarchy → Functional Decomposition with Data Model

Parent F0                    D1 → [F0] → D2
   │                              ↙    ↘
Child F1, F2          D1 → [F1] → D3 → [F2] → D2
   │                       ↙         ↘
Grandchild         D1 → [F1.1] → D4 → [F1.2] → D5 → [F1.3] → D3
F1.1, F1.2, F1.3

Where D = Data, Signal, Energy, Matter
```

## Requirement Tracing

### Bi-directional Tracing:
- **Requirements → Functions:** Each requirement drives some aspect of a function
- **Functions → Requirements:** Each function associated with requirements
- Helps identify:
  - Missing requirements
  - Missing functions
- MBSE tools automatically handle bi-directionality

### Derived Requirements:
- Many sub-functions and internal flows won't correspond to originating requirements
- Add derived requirements and trace sub-functions to them

## Evaluation of Functional Architecture

### Key Evaluation Questions:

1. **Have I specified all necessary functionality?**
   - Check for absence of functionality for input sets
   - Verify ability to produce desired outputs
   - Ensure sufficient feedback and control consideration

2. **Does the architecture satisfy requirements?**
   - Are requirements traced to functional elements?

3. **Have I specified redundant functionality?**
   - Have all system modes been considered?

4. **Are all inputs and outputs conserved?**
   - Input to lower-level function must be input of higher-level function
   - Output of lower-level function must be input to another function and/or output of higher-level function

### Operational Scenario Tracing Technique:
1. Choose scenario from operational concept
2. Choose input/output pair from external system diagram
3. Trace scenario through functional decomposition
4. Identify inputs/outputs from main function
5. Trace transformation through subfunctions
6. Continue through all hierarchy levels
7. Repeat for other scenarios

## Common Errors in Functional Architecture

### Substantive Errors:
- Including external system functions
- Violating conservation of inputs and outputs
- Functional requirements with no functionality to satisfy them
- Input/output requirements with no inputs to satisfy them
- Operational scenarios that cannot be fulfilled
- Creating outputs "out of thin air" (e.g., placing cell phone call with no signal)

### Errors in Wording:
- Function name not an action verb with noun
- Input and output not noun phrases

## Key Vocabulary Summary

- **Function:** Process transforming inputs to outputs; something the system does
- **Functionality:** Distinct capability to produce single output
- **State:** Static snapshot of variables needed to describe capability to perform functions
- **Mode:** Distinct manner of operating system
- **Functional Architecture:** Formal description of functions and flow of inputs/outputs, traced to/from requirements
- **Functional Decomposition:** Hierarchical decomposition of top-level system function
- **Data Model:** Specifies inputs and outputs of functions
- **Open-loop Control:** Controls output using only current state and system model
- **Closed-loop Control:** Controls output using current state, model, and comparison of actual with desired output

## Course Planning Notes

### Upcoming Classes:
- **Sept 29, 2025:** Functional Architecture in MagicDraw (Dr. Mohammadreza Torkjazi)
- **Oct 1, 2025:** Regular Lecture
- **Oct 6, 2025:** Mid-term Study Time/Review
- **Oct 8, 2025:** Mid-Term In-Class @ 3:00pm
- **Oct 13, 2025:** Fall Break - No Class
- **Oct 15, 2025:** Guest Lecture by Dr. David Flanigan (Johns Hopkins) - Mandatory

### Action Items:
- Project Deliverable 1: Due Friday
- Project Deliverable 2: Start this week
- Homework 3: Due Oct 3, 2025
- Review Discover Systems Presentation Schedule

## Study Questions (/SYST210/TIL)

1. What are the three components of a functional architecture?
2. Why do we need to consider all modes of operation when defining the functional architecture?
3. List some common errors in defining a functional architecture
4. Why do we sometimes find we need to revise the operational concept, system boundary, and requirements when defining the operational concept?
5. What is the Hatley-Pirbhai template and why is it useful for developing a functional architecture?
6. How are the operational scenarios and external systems diagram used in defining the functional architecture?