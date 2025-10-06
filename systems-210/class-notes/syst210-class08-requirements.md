# SYST 210: SYSTEM DESIGN
## CLASS 08: SYSTEM REQUIREMENTS

**Instructor:** Dr. Ali K. Raz  
**Institution:** George Mason University, SEOR Department

---

## Comic Strip Introduction

*[Comic showing a dialogue about requirements]*

Panel 1: "I'll need to know your requirements before I start to design the software."

Panel 2: "First of all, what are you trying to accomplish?"

Panel 3: "I'm trying to make you design my software."

Panel 4: "I mean what are you trying to accomplish with the software?"

Panel 5: "I won't know what I can accomplish until you tell me what your software can do."

Panel 6: "Try to get this concept through your thick skull: The software can do whatever I design it to do!"

Panel 7: (Empty)

Panel 8: "Can you design it to tell you my requirements?"

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

---

## Define the Design Problem → What Do We Want?

### Major Inputs:
- System Statement of Need
- Stakeholder Analysis

### Major Outputs

**Operational Concept of the System**
- Vision of the system
- Mission Requirements
- Operational Scenarios and Use-cases

**External Systems and System Boundary**

**Objective hierarchy**

**Originating System Requirements**
- Description of constraints and performance
- How the system will behave

---

## Learning Objectives for Today

☐ List the characteristics of sound requirements (individual and set)

☐ Describe why effective requirements management is essential to successful system design

☐ Given an objectives hierarchy, a set of operational scenarios, and an external systems diagram for a system, develop:
  - ☐ A candidate set of originating requirements for the system
  - ☐ A set of questions to pose to stakeholders to refine the originating requirements

☐ Represent requirements and objectives in SysML using MBSE software

---

## Requirements

### Purpose and Importance

Requirements translate stakeholder needs and objectives into measurable parameters:
- Communication tool between stakeholders and developers
- Basis for design
- Basis for evaluation
- Create contractual obligation

### Requirements Are Key to Successful Systems

**Study by Standish Group (1996):**
- Requirement difficulties responsible for 35% to 44% project failures
- $100B in 96 spent on cancelled IT projects

### Requirement Challenges Today
- **Writing and identifying requirements for AI systems**

---

## Requirement Definitions

### From Various Sources

**MIL-STD 499B [Military Standard, 1993]:**
> Identifies the accomplishment levels needed to achieve specific objectives.

**Chambers and Manos [1992]:**
> The attributes of the final design that must be a part of any acceptable solution to the design problem.

**Davis [1993]:**
> A user need or necessary feature, function, or attribute of a system that can be sensed from a position external to that system.

**Grady [1993]:**
> An essential attribute for a system or an element of a system, coupled by a relation statement with value and units information for the attribute.

**Harwell et al. [1993]:**
> "If it mandates that something must be accomplished, transformed, produced, or provided, it is a requirement period."

---

## Our Requirement Definition

> **A requirement is a necessary feature, function or attribute of a system that can be sensed from a position external to the system**

### Originating Requirement:
- Comes from the stakeholder

### Derived Requirement
- Requirement that is developed to meet originating requirement

---

## Requirements Hierarchy

```
                    Mission Requirements
                           │
                           ▼
              ┌─── Stakeholders' Requirements
              │
              ▼
       System Requirements ────────────┐
              │                        │
              ▼                        │
       Component Requirements          │
              │                        │  Derived
              ▼                        │  Requirements
       CI Requirements ────────────────┘
```

*From: Chapter 6 - Requirements and Defining the Design Problem*

---

## Originating Requirements

### Requirements Must Be Developed for Each Phase of the System's Life Cycle

- Development (design and integration)
- Manufacturing or production
- Deployment
- Training
- Operations
- Maintenance and Support
- Refinement
- Retirement

### Important Considerations

- Relevance of these phases differs for different systems
  - For some systems, some phases may not occur

- Relevance of stakeholders differs for different lifecycle phases
  - Important to consider all stakeholder groups

---

## Characteristics of Sound Requirements: Individual Requirement

**1. Unambiguous** – every requirement has only one interpretation

**2. Understandable** – the interpretation of each requirement is clear

**3. Correct** – a requirement the system is in fact required to do

**4. Concise** – no unnecessary information is included in the requirement

**5. Traced** – each originating requirement is traced to some document or statement of the stakeholders

**6. Traceable** – each derived requirement must be traceable to an originating requirement via some unique name or number

**7. Design independent** – each requirement does not specify a particular solution or a portion of a particular solution

**8. Verifiable** – a finite, cost-effective process can be defined to check that the requirement has been attained

*From Buede, The Engineering Design of Systems, Table 6.3*

---

## Characteristics of Sound Requirements: The Set as a Whole

**9. Unique** – requirement(s) is (are) not overlapping or redundant with other requirements

**10. Complete** –
- (a) everything the system is required to do throughout the system's life cycle is included,
- (b) responses to all possible (realizable) inputs throughout the system's life cycle are defined,
- (c) the document is defined clearly and self-contained, and
- (d) there are no to be defined (TBD) or to be reviewed (TBR) statements; completeness is a desired property but cannot be proven at the time of requirements development, or perhaps ever

**11. Consistent** – (a) internal, no two subsets of requirements conflict and (b) external, no subset of requirements conflicts with external documents from which the requirements are traced

**12. Comparable** – the relative necessity of the requirements is included

**13. Modifiable** – changes to the requirements can be made easily, consistently (free of redundancy) and completely

**14. Attainable** – solutions exist within performance, cost and schedule constraints

---

## Writing Requirements

### Example Requirement Structure

**The SD-Car shall activate auto-mode at speeds greater than 60mph.**

### Key Components

**Define the system under consideration**
- "The SD-Car"

**Include a verb:**
- Ordinary requirement: **shall**
- Goals use: **should** (desirable but not necessary)
- Constraints: **will**

**Defines a positive end results**
- Avoid compound predicates
- Avoid negative predicates (turn to positive)

**Quality Criteria**
- Describe what not how

---

## Writing Requirements: What to Avoid

### Avoid the following:

- Ambiguity and including words such as 'or' 'etc.' and 'so on'…….
- Escape clauses: 'but', 'if' 'when', 'although' 'except' …….
- Informal words or slang: 'cool', 'user-friendly', 'as much possible', 'totally'……
- Compounding or joining sentences with 'and', 'also', 'with'……..
- Vague words: 'usually', 'normally', 'may', 'perhaps' 'could'……
- Incompleteness: TBD, TBR (often difficult to avoid early on)

### Always keep in mind:

- Requirements are for a system and not for external system or user
- Requirements must be unambiguous
- Requirements must be verifiable

---

## How Requirements Effect System Design

### Requirements Always State the Problem to Keep the Solution Space Open

**Example 1:**

| Top-level function: | The system shall hold together 2–20 sheets of 8½ by 11 in., 20 lb paper |
|---------------------|-------------------------------------------------------------------------|
| **Alternatives:**   | Stapler, paper clip, fold the corner, put the pages in a folder        |

**Example 2:**

| The deficiency: | My reports are typically composed of 2–20 sheets of 8½ by 11 in., 20 lb paper. The pages get out of order and become mixed up with pages of other reports, especially when they lie on a car seat with the windows down |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Alternatives:** | Stapler, paper clips, fold the corner, put the pages in folders, number the pages, put them in envelopes, put them in three-ring binders, throw away the reports, convert them to electronic form, have them bound as books, put them on audio tapes, distribute them electronically, put them on DVDs, put them on microfiche, transform the written reports into videotapes |

*Reference: Bahill, A. Terry, and Azad M. Madni. "Discovering system requirements." Tradeoff Decisions in System Design. Cham: Springer International Publishing, 2016. 373-457.*

---

## What Not How

### The Relationship Between Whats and Hows at Different Levels

**One Man's Ceiling is Another Man's Floor**

```
Stakeholder needs ──────────────────► What
                    ╲                  How
                     ╲
System features ◄────────────────────► What
                    ╲                  How
                     ╲
Requirements ◄──────────────────────► What
                    ╲                  How
                     ╲
Design specifications ◄──────────────► What
                    ╲                  How
                     ╲
Test procedures ◄───────────────────► What
                                       How
```

*Figure 4.1: The relationship between whats and hows at different levels*

*Reference: Bahill, A. Terry, and Azad M. Madni. "Discovering system requirements." Tradeoff Decisions in System Design. Cham: Springer International Publishing, 2016. 373-457.*

---

## DILBERT Comic on Requirements

*[DILBERT by Scott Adams comic strip showing the complexity of requirements]*

Panel 1: "YOUR USER REQUIREMENTS INCLUDE FOUR HUNDRED FEATURES."

Panel 2: "DO YOU REALIZE THAT NO HUMAN WOULD BE ABLE TO USE A PRODUCT WITH THAT LEVEL OF COMPLEXITY?"

Panel 3: "GOOD POINT. I'D BETTER ADD 'EASY TO USE' TO THE LIST."

---

## Some Examples: Can You Tell If Something Is Wrong Here!!!

**Example 1:**
> Security personnel shall respond promptly to emergencies identified by the alarm.

**Example 2:**
> The solar powered drone shall be light-weight and flexible.

**Example 3:**
> The self-checkout system increases efficiency of supermarket and it shall quickly process customers.

**Example 4:**
> The solar powered drone shall operate for 15minutes in air.

---

## Common Types of Requirements

```
┌─────────────────┐  ┌─────────────────┐
│   Input Reqs    │  │   Output Reqs   │
└─────────────────┘  └─────────────────┘

┌─────────────────┐  ┌─────────────────┐
│  Technology     │  │   Trade-off     │
│      Reqs       │  │      Reqs       │
└─────────────────┘  └─────────────────┘

      ┌─────────────────┐
      │ Qualification   │
      │      Reqs       │
      └─────────────────┘
```

---

## Requirements Management

### Key Activities

- Identify, derive, analyze, allocate & control requirements
- In a consistent, traceable, correlatable, verifiable manner
- Include all the system functions, attributes, interfaces, and verification methods a system must meet

### Manage Changes to Requirements as Design Evolves

- Document source of change, rationale for change, approvals
- Make sure affected parties are notified of changes
- Trace changes to other affected requirements, make appropriate changes, and analyze overall impact of change
- Keep up to date version of requirements in a common repository and make sure all members of design team are working from the most current version
- Keep a history of versions

### Requirements Management Tools Are Useful

- DOORS
- CORE
- SysML tool – e.g. MagicDraw, Enterprise Architect

---

## Requirements Diagram in MBSE

### SysML Requirements Diagrams

**SysML tools use a requirements diagram to specify and display requirements. Magic SoS is a full SysML implementation and supports requirements diagrams**

**Figure 12.12. Example of requirements containment hierarchy:**

Shows a hierarchical structure with:
- Operating Environment (top-level requirement)
  - All Weather Operation (S1.1)
  - 24/7 Operation (S1.2)
  - Verified by: Water Spray Test

**Figure 12.14. Example of «deriveReqt» relationship, with rationale attached:**

Shows:
- All Weather Operation and 24/7 Operation requirements
- Both derive to: Sensor Decision requirement
- Rationale: "Using a camera is the most cost-effective way of meeting these requirements. See trade study T.1."

---

## Representing Requirements in MBSE Tools

### Requirements Can Be Related to Other Elements of a SysML Model

**(Table 12.2 of Friedenthal, et al)**

| Relationship Name | Keyword Depicted on Relation | Requirement (arrow) End Callout/Compartment | Client (no arrow) End Callout/Compartment |
|------------------|------------------------------|---------------------------------------------|-------------------------------------------|
| **Satisfy** | «satisfy» | Satisfied by «model element» | Satisfies «requirement» |
| **Verify** | «verify» | Verified by «model element» | Verifies «requirement» |
| **Refine** | «refi ne» | Refined by «model element» | Refines «requirement» |
| **Derive Requirement** | «de-riveReqt» | Derived «requirement» | Derived from «requirement» |
| **Copy** | «copy» | (None) | Master «requirement» |
| **Trace** | «trace» | Traced «model element» | Traced from «requirement» |
| **Containment (Requirement decomposition)** | (Crosshair icon) | (No callout) | (No callout) |

---

## Identifying Stakeholder Needs and Obtaining Requirements

### Start with Usage Scenarios (Use Cases)
- What requirements are necessitated by each use case?
- Are we missing any use cases?

### Observe Them Doing Their Job
- Normal and stressful times

### Give Them Something to Respond To
- Draft to modify
- Prototype to evaluate
- Choices between options

### Work with Them in Groups
- They are inspired by each other's ideas
- We are poor filters of their conversations

### Continue Involvement Throughout System Life Cycle
- Requirements evolve over time as the world changes
- Emergent requirements are new, undiscovered, often critical

---

## What You Need to Do Soon!

### Homework 2
- ✓ Done

### Homework 3
- Available on Wednesday (Sept 24, 2025)
- Due Oct 5th, 2025

### Final Project
- What need area you would like to address in your project
- Be creative and innovative
- Discuss ideas within your team
- PD-1 Due Sept 26th, 2025

### Discover Systems
- Feedback and schedule now available
- Make sure you know when you are presenting

---

## To Think About!

### Purpose and Consequences

What is the purpose of each of the following? What happens if it is ignored or done poorly?
- Objectives hierarchy
- Requirements

### Stakeholder Engagement

We hear a great deal about stakeholder input to the design process. But slogging through page after page of "The system shall…" is a colossally boring thing to have to do.
- What happens if stakeholders don't review requirements?
- Do you have suggestions for how to engage stakeholders in ensuring that requirements reflect their needs and values?

### Organization Schemes

Your textbook defines four categories of requirements (input, output, technology & system-wide; trade off; qualification)
- What is the point of having such an organization scheme?
- You might encounter different organization schemes at organizations you join. What should you do if this happens?

### Real-World Scenarios

You may find yourself a member of an organization that has no well-defined process for capturing and managing requirements. What should you do if this happens to you?

---

## /SYST210/TIL/

### Today I Learned

- Why are requirements important?

- What are some characteristics of good requirements?

- How do we obtain requirements?

---

*Copyright © Ali K. Raz GMU SEOR*