# SYST 210: SYSTEM DESIGN
## CLASS 06: INTRO TO MODEL-BASED SYSTEM ENGINEERING

**Instructor:** Dr. Ali K. Raz  
**Institution:** George Mason University, SEOR Department

---

## Review from Class 05

### System Boundary, External Systems, and Context

**Context:**
- Impact the system but are not impacted by the system
- Generate originating requirements

**External Systems:**
- Interact with the system via external interfaces
- Impact and are impacted by the system
- Play a major role in establishing requirements
- Can be existing (or legacy) systems

**System Boundary:**
- Delineates what is inside and outside the system
- Essential input to detailed design

### External Systems and Operational Concept

Example: Environments of a passenger airliner (ILS instrument landing system)

**Flight Environment:**
- Rain, Winds, Turbulence
- Flight Commands
- Beacon Interrogation

**Landing Environment:**
- Shock and Vibration
- ILS Beacon

**Support Environment:**
- Power
- Fuel

**People and Payload Interface:**
- Passengers
- Luggage

**Maintenance Environment**

*Reference: Buede, The Engineering Design of Systems, Figure 6.2*

### Operational Concept: Model-Based Representation

Example: Elevator System

**Sequence Diagram (left):**
Shows interaction between Passenger (including mobility, visually, and hearing challenged) and Elevator:
1. Up Service Request
2. Feedback that request was received
3. Feedback that car is on the way
4. Feedback that door is opening
5. Entry Opportunity
6. Floor Request
7. Feedback that request was received
8. Feedback that door is closing
9. Feedback about floor where stopped
10. Feedback that door is opening
11. Exit Opportunity

**Use Case Diagram (right):**
- Vehicle Occupant actors: Passenger and Driver
- Use cases:
  - Enter Vehicle
  - Exit Vehicle
  - Control Vehicle Accessory
  - Drive Vehicle

*References: Buede & Miller, The Engineering Design of Systems; A Practical Guide to SysML*

---

## Learning Objectives for Today

- ☐ Describe what is a model and why they are important for engineering
- ☐ Describe the difference between document-centric and model-centric systems engineering
- ☐ Describe System Modeling Language (SysML)
  - ☐ Create Sequence Diagram
  - ☐ Create Use Case Diagram
- ☐ Use SysML use case and sequence diagrams to represent operational scenarios and systems boundary
- ☐ Given a statement of need and an operational concept, create an external systems diagram showing system boundary, external systems, and context

---

## Structure of the System Design Process

```
System Statement of Need ──┐
                           ▼
                    Define System-level ◄── Stakeholder Analysis
                    Design Problem
                           │
              ┌────────────┴────────────┐
              ▼                         ▼
       Develop Functional        Develop Physical
        Architecture              Architecture
              │                         │
              └────────────┬────────────┘
                           ▼
                    Develop Allocated
                      Architecture
                           │
              ┌────────────┴────────────┐
              ▼                         ▼
       Develop Interface         Develop Qualification
        Architecture                  System
```

**Key Question:** Where do these artifacts exist?

---

## From Documents to Models

### The Transition to MBSE

**Past: Document Centric**
- Multiple separate documents (specifications, interface requirements, system design, analysis & tradeoff, test plans)
- Linear, sequential waterfall process

**Future: Model Centric**
- Integrated system model
- Single source of truth
- Iterative, agile processes

**Transition Principle:**
> "Models replace documents as the primary products or artifacts of SE processes"

*Source: https://www.ltts.com/sites/default/files/resources/pdf/whitepapers/2017-12/WP_MBSEi.pdf*

---

## What Are Models?

### Definitions

**DoD 1998:**
> "A physical, mathematical, or otherwise logical **representation** of a system, entity, phenomenon, or process."

**Bellinger 2004:**
> "A simplified **representation** of a system at some particular point in time or space intended to promote understanding of the real system."

**INCOSE Handbook:**
> "A **representation** of some entity in the physical world. The representations are intended to describe selected aspects of the entity, such as its geometry, functions, or performance."

### Examples of Models

1. **CAD Model of Mars Rover** (Full-scale & Digital)
2. **Bernoulli's Equation** (Analytic mathematical model)
3. **Functional Flow Diagram** (Process representation)
4. **Prototype of a Ventilator** (Full-scale & Prototype)
5. **COVID-19 Simulator** (Simulation of COVID-19 situation due to policies)

---

## Models vs. Reality

### The Box Principle

> **"All models are wrong, but some are useful"**  
> — George E. P. Box

Models are simplified representations that:
- Cannot capture every detail of reality
- Are useful when they capture the essential aspects needed for decision-making
- Must be validated against real-world data

---

## Models and Systems Engineering

### Key Questions

**What do Systems Engineers Model?**
- System requirements
- System architecture (functional, physical, allocated)
- System behavior
- System interfaces
- System performance

**Where do models come from?**
- Stakeholder needs analysis
- Operational concept development
- Requirements elicitation
- Design synthesis
- Analysis and simulation

**When building models, care must be taken for:**
- Model accuracy and fidelity
- Model validation
- Model scope and boundaries
- Model assumptions and limitations
- Traceability to requirements

**What is the process of using models in systems engineering called?**
- Model-Based Systems Engineering (MBSE)

---

## Brief Introduction to Systems Engineering and Model-Based Systems Engineering

### Systems Engineering (INCOSE / IEEE 15288)

> "Systems Engineering is a transdisciplinary and integrative approach to enable successful realization, use, and retirement of engineered system, using systems principles and concepts, and scientific technological, and management methods"

### Model-Based Systems Engineering (MBSE) (INCOSE)

> "Model-based systems engineering (MBSE) is the formalized application of modeling to support system requirements, design, analysis, verification and validation, beginning in the conceptual design phase and continuing throughout development and later life cycle stages."

### MBSE Framework Diagram

Shows integration across:
- System development (requirements, design, analysis)
- Upper level system element development (integration, verification, validation planning)
- Lower level system element or more detailed development
- V and V planning at all levels
- Continuous feedback loops between all elements

*Figure: INCOSE Systems Engineering Handbook, 5th Edition 2024*

---

## Model-Based Systems Engineering

### Definition (Defense Science Board)

> "MBSE is a continuum building upon systems engineering principles that transitions from unstructured document-centric engineering to formalized data- and model-driven characterization of systems at multiple levels of abstraction"

### Current State vs. Future State

**Current State: Document-Based Systems Engineering**
- Multiple disconnected documents
- Requirements, design, operations, testing, manufacturing, engineering as separate documents
- Sequential waterfall process
- Difficult collaboration

**Future State: Model-Based Systems Engineering (MBSE)**
- Integrated digital model
- Requirements, design, operations, testing, manufacturing, engineering all connected
- Agile & iterative process
- Benefits:
  - Model-based
  - Faster
  - Savings
  - **Authoritative Source of Truth**
  - Agile & Adaptable
  - Reuse
  - Collaborative
  - Digital Twins

---

## Model-Based Systems Engineering Foundations

### Three Foundational Pillars

**1. Systems Engineering Principles and Concepts (Methodology)**
- Functional Architecture
- Allocated Baseline
- System Life Cycle Reviews
- Interface, Test, and Validation

**2. Expressing and Describing Concepts (Language)**
- Systems Modeling Language (SysML)
- Composition/Relationships
- Diagrams
- IDEF (old)

**3. Computer Implementation (Tools)**
- Cameo/Magic Draw
- System Composer (Matlab)
- Innoslate
- Genesys (ViTech)

---

## MBSE Methodology

### What is Methodology?

> "Methodology means a system (or set) of methods used in a particular area of study or activity"  
> — Oxford Dictionary

### Methodology for MBSE

**Systems Engineering Principles and Concepts**

Returns to the system design process:
```
System Statement of Need → Define System-level Design Problem ← Stakeholder Analysis
                                      ↓                    ↓
                           Develop Functional    Develop Physical
                            Architecture          Architecture
                                      ↓                    ↓
                                 Develop Allocated Architecture
                                      ↓                    ↓
                           Develop Interface    Develop Qualification
                            Architecture              System
```

---

## MBSE Languages

### Definition
Provides constructs for formally representing some phenomenon

### Common MBSE Languages

#### 1. System Modeling Language (SysML)
- Provides constructs for defining a set of interrelated diagrams that define a system model
- Builds from commonly used Unified Modeling Language for software

#### 2. Integrated Definition (IDEF)
- Provides constructs for defining a set of interrelated diagrams that define a system model
- IDEF0 for Functional Models
- Other IDEFs also exist (e.g., IDEF1 for Data model, etc.)

---

## SysML

### SysML Diagram Taxonomy

```
                        SysML Diagram
                              |
        ┌─────────────────────┼─────────────────────┐
        ▼                     ▼                     ▼
   Structure            Requirement            Behavior
    Diagram              Diagram               Diagram
        |                                          |
   ┌────┼────┐                        ┌───────────┼────────────┐
   ▼    ▼    ▼                        ▼           ▼      ▼     ▼
 IBD   BDD  Package                Activity   Sequence  State  Use Case
           Diagram                 Diagram    Diagram  Machine Diagram
   |                                                   Diagram
   ▼
Parametric
 Diagram
```

**Legend:**
- **Structure Diagrams:**
  - Internal Block Diagram (IBD)
  - Block Definition Diagram (BDD)
  - Package Diagram
  - Parametric Diagram

- **Requirement Diagram**

- **Behavior Diagrams:**
  - Activity Diagram
  - Sequence Diagram
  - State Machine Diagram
  - Use Case Diagram

### SysML Diagram Examples

Visual representation showing multiple diagram types integrated:
- Block Definition Diagram (BDD)
- Requirements
- Parametric diagram
- Internal Block Diagram (IBD)
- Use case
- Sequence diagram
- Activity diagram
- State chart

---

## MBSE Tools

### Definition
Tools provide means to implement the methodology via a language

### Common/Popular MBSE Tool

**MagicDraw**
- "Architecture Made Simple"
- Available to download via Canvas
- Available on VSE 1505 Lab

---

## Implementing Operational Scenarios in MBSE

### Example: Elevator Sequence Diagram

**Text-based representation:**
```
Passenger (including          Elevator
mobility, visually &
hearing challenged)
        |
        |─── Up Service Request ─────────────────►
        |
        |◄── Feedback that request was received ──
        |
        |◄── Feedback that car is on the way ─────
        |
        |◄── Feedback that door is opening ───────
        |
        |◄── Entry Opportunity ───────────────────
        |
        |─── Floor Request ──────────────────────►
        |
        |◄── Feedback that request was received ──
        |
        |◄── Feedback that door is closing ───────
        |
        |◄── Feedback about floor where stopped ──
        |
        |◄── Feedback that door is opening ───────
        |
        |◄── Exit Opportunity ────────────────────
```

**SysML Visual Representation:**
- Shows External Actor (Passenger) and Main System (Elevator)
- Message flows (solid lines for requests, dashed lines for feedback)
- Reply messages (dashed lines)
- Activation Bar showing System lifeline
- Diagram produced with MagicDraw

---

## Demonstration

### Let's See How to Build Sequence Diagram in MagicDraw

*(Practical demonstration section)*

---

## What You Need to Do Soon!

### Continue Reading from Last Week:
- Buede & Miller: 2.1, 2.2, 2.3, 6.3, 6.10 and 6.11
- A Practical Guide to SysML: Chapter 2.1 and 3.1, 3.2, 4.1, 4.2, 4.3.1-4.3.7

### Homework 1
- ✓ Submitted

### Homework 2
- Due this week

### "Discover Systems"
- Presentation schedule coming out soon

---

## Vocabulary

- **Operational Concept:** Describes how system will be used

- **Need Statement:** Describes facts and evidence to justify why proposed system is needed

- **System Boundary / External Systems Diagram:** Shows system as "black box" and how it interacts with context and environment (also called context diagram)

- **Objectives Hierarchy:** Hierarchical decomposition of cost, schedule & performance measures of effectiveness

- **Context (of a system):** Set of entities that can impact the system but are not impacted by the system

- **External system:** System that interacts with system via external interfaces

- **System boundary:** Separates the system from external systems with which it interacts; inputs and outputs must flow across the boundary

- **External systems diagram:** Displays interactions of system with other (external) systems, thus providing a definition of the system boundaries

- **Use case diagram:** SysML diagram depicting operational scenarios and system boundary; provides graphical overview of system functionality

- **Model-based systems engineering:** Formalized application of modeling to support system requirements, design, analysis, verification and validation throughout the system lifecycle

---

## /SYST210/TIL (Today I Learned)

### Key Questions to Reflect On:

- What is a model?

- What is model-based systems engineering and how does it differ from document-centric systems engineering?

- Why do engineers build models of systems?

- How is a system model used to:
  - Manage system requirements?
  - Analyze alternative system designs?
  - Choose the best system design from among a set of alternatives?
  - Develop a test and evaluation plan?
  - Document design decisions and communicate them to stakeholders?

---

*Copyright © Ali K. Raz GMU SEOR*