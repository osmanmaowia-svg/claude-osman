# SYST 210: SYSTEM DESIGN
## CLASS 10: FUNCTIONAL ARCHITECTURE MODELING TOOLS

**Instructor:** Dr. Ali K. Raz  
**Institution:** George Mason University, SEOR Department  
**Lecture by:** Dr. Mohammadreza Torkjazi  
**Contact:** <mtorkjaz@gmu.edu>

---

## Learning Objectives for Today

☐ Identify SysML diagrams to build a functional architecture of the system

☐ Utilize MBSE tools and Activity Diagrams to build Functional flow of the system

☐ Generate Block Definition Diagram from MBSE tools to provide functional decomposition hierarchy of a system

---

## Recap from Last Time: Functional Architecture

### Functional Architecture is a Structure of Functions That Provides:

**1. Functional Decomposition**
- Hierarchical decomposition of system top level functions
- Identifies what are the functions

**2. Data Model/Functional Flow**
- Specifies input and outputs of functions
  - **Data, Signal, Energy and Matter**
- How are the input and outputs connected

**3. Requirement Tracing**
- Function, input, and outputs are traced to requirements they satisfy
- Provide an opportunity to derive system level requirements and also identify new requirements

---

## Functional Decomposition to Functional Flow Diagrams

### Function Hierarchy → Functional Decomposition with Data Model

**Function Hierarchy (Left Side):**

```
      (parent) F0
                |
        ┌───────┴───────┐
        |               |
   (child) F1          F2
        |               |
    ┌───┼───┐       ┌──┼──┐
    |   |   |       |  |  |
  F1.1 F1.2 F1.3   ...........
        |
    ┌───┼───┬───┐
    |   |   |   |
 F1.2.1 F1.2.2 F1.2.3
```

**Functional Decomposition with Data Model (Right Side):**

```
Level 0:
      D1 ──► F0 ──► D2
              |
              ▼
Level 1:
      D1 ──► F1 ──► D3 ──► F2 ──► D2
              |              |
              ▼              ▼
Level 2:
      D1 ──► F1.1 ──► D4 ──► F1.2 ──► D5 ──► F1.3 ──► D3
```

**D = Data, Signal, Energy, Matter**

---

## Building Functional Architecture in MBSE - SysML

### Key Diagram Types

Functional Architecture in SysML is built via:
- **Activity Diagram** (behavior/flow)
- **Block Definition Diagram** (structure)

### SysML Diagram Taxonomy

```
                        SysML Diagram
                              |
        ┌─────────────────────┼─────────────────────┐
        ▼                     ▼                     ▼
   Structure            Requirement            Behavior
    Diagram              Diagram               Diagram
        |                                          |
   ┌────┼────┬────────┐              ┌───────────┼────────────┐
   ▼    ▼    ▼        ▼              ▼           ▼      ▼     ▼
 IBD   BDD  Package  Parametric   Activity   Sequence  State  Use Case
           Diagram   Diagram      Diagram    Diagram  Machine Diagram
                                                      Diagram
```

**Highlighted for Functional Architecture:**
- **Activity Diagram** (Behavior)
- **Block Definition Diagram (BDD)** (Structure)

---

## Activity Diagrams

### Overview

**Activity Diagrams:**
- Model dynamic behavior of the system
- Good for expressing flow of data, energy, material, and signals in the system

### Select Elements

**Action Blocks and Nodes:**
- **Action Block:** Performs the activity
- **Initial:** Indicates start of an activity
- **Final:** Indicates completion of an activity
- **Final Flow:** Indicates exit from the system
- **Send/Receive:** Indicates sent or received signals

### Connectors:

- **Control Flow:** Starts an activity once the previous is completed
- **Object Flow:** Models the flow of data, energy, signals, and matter between activities

### Example Activity Diagram Structure

```
[Initial Node: ●]
       |
       ▼
┌──────────────────┐
│  «createObject»  │
│ Controller Dialog│
└──────────────────┘
       |
       ├── value ──► ┌────────────────────────────┐
       |             │ «addStructuralFeature»     │  ──► result
       |             │      application           │
       ▼             └────────────────────────────┘
┌──────────────┐           |
│ «readSelf»   │           |
│    self      │ ── result ┤
└──────────────┘           |
       |                   ▼
       |            ┌────────────────────────────┐
       └── object ─►│ «addStructuralFeature»     │  ──► value
                    │    controlDialog           │
                    └────────────────────────────┘
                           |
                           ▼
                    [Final Node: ◉]
```

---

## Block Definition Diagrams (BDDs)

### Overview

**BDDs are the most common type of SysML diagrams**

- BDDs allow to represent hierarchies in system structure
- Composed of simple blocks but each block can contain multiple compartments:
  - Parts
  - References
  - Values
  - Flow ports
  - Etc.

- It is the compartments and relationships to other system artifacts that provide richness of expressions

### BDD for Functional Decomposition

**BDD are utilized to represent Functional Decomposition Hierarchy of a system**
- Functional decomposition hierarchy can be automatically generated from Activity Diagram

### Example: Vehicle Structure BDD

```
bdd [Package] Structure [ Vehicle Structure ]

                    ┌──────────┐
                    │ «block»  │
                    │ Vehicle  │
                    └─────┬────┘
                          │
          ┌───────────────┼───────────────┐
          │               │               │
       wheel           engine       transmission
          │               │               │
    ┌─────▼─────┐   ┌─────▼─────┐  ┌─────▼─────┐
    │  «block»  │   │  «block»  │  │  «block»  │
    │   Wheel   │   │  Engine   │  │Transmission│
    └─────┬─────┘   └─────┬─────┘  └───────────┘
          │               │
       brake             tire
          │               │
    ┌─────▼─────┐   ┌─────▼─────┐
    │  «block»  │   │  «block»  │
    │   Brake   │   │   Tire    │
    └─────┬─────┘   └───────────┘
          │
    ┌─────┴─────┬────────┬────────┐
    │           │        │        │
  rotor      caliper    pad
    │           │        │
┌───▼───┐  ┌───▼───┐ ┌──▼──┐
│«block»│  │«block»│ │«block»│
│ Rotor │  │Caliper│ │ Pad │
└───────┘  └───────┘ └─────┘
```

---

## Demonstration

### Let's See Activity Diagram and BDD in Action in MagicDraw

*(Practical demonstration section - hands-on tutorial in MagicDraw)*

This section covers:
1. Creating an Activity Diagram in MagicDraw
2. Adding actions, flows, and objects
3. Auto-generating Block Definition Diagrams from Activity Diagrams
4. Understanding the relationship between functional flow and functional hierarchy

---

## Course Planning and What You Need to Do Soon!

### Class Planning:

**Monday Sept 29th, 2025**
- Functional Architecture in Magic Draw
- Dr. Mohammadreza Torkjazi

**Wednesday Oct 1st, 2025**
- Regular Lecture

**Monday Oct 6th, 2025**
- Mid-term Study Time / Review

**Wednesday Oct 8th, 2025**
- Mid-Term In-Class @ 3:00pm

**Monday Oct 13th, 2025**
- Fall Break - No Class

**Wednesday Oct 15th, 2025**
- Guest Lecture by Dr. David Flanigan, John Hopkins University
- Hosted by Dr. Raz
- **Mandatory attendance**

### What You Need to Do Soon:

**Project Deliverable 1**
- Due Friday

**Project Deliverable 2**
- Start working on it this week

**Homework 3**
- Due Oct 3rd, 2025

**Discover Systems Presentations**
- Review your Discover Systems Presentation Schedule

**Project Planning**
- Think about project deliverable 2

---

## /SYST210/TIL/

### Today I Learned

- What is an Activity Diagram?

- What is a Block Definition Diagram?

- What are the differences between an Activity Diagram and a BDD?

- What is SysML?

---

## Key Takeaways

### Activity Diagrams vs. Block Definition Diagrams

| Aspect | Activity Diagram | Block Definition Diagram |
|--------|-----------------|--------------------------|
| **Type** | Behavior Diagram | Structure Diagram |
| **Purpose** | Shows functional flow and behavior | Shows hierarchical decomposition |
| **Elements** | Actions, flows, objects | Blocks, parts, relationships |
| **Focus** | How the system behaves (dynamic) | What the system is composed of (static) |
| **Flow** | Control flow and object flow | Composition and generalization |

### Relationship Between Diagrams

1. **Activity Diagrams** capture the dynamic functional behavior
2. **BDDs** can be auto-generated from Activity Diagrams to show structure
3. Together they provide a complete functional architecture
4. Both tie back to requirements through traceability

### Best Practices

- Start with high-level activities before decomposing
- Use meaningful names for actions and flows
- Ensure all inputs and outputs are specified
- Leverage auto-generation features in MBSE tools
- Maintain traceability to requirements
- Use consistent naming conventions across diagrams

---

*Copyright © Ali K. Raz GMU SEOR*