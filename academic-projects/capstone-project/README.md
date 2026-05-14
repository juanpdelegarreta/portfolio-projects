# NETC-290 - Computer Network Engineering Technology Captone Project
## Course Description
Students work in teams to design and build network solutions while demonstrating knowledge and skills gained in the Computer Network Engineering Technology program.

## Project Overview
This capstone project simulates designing, implementing, and validating an enterprise network infrastructure for a smart manufacturing facility. Over 15 weeks, your 5-person team will build the network in a PT/VM-first workflow, translate designs to physical gear only when required, and produce an evidence bundle that demonstrates security controls, segmentation, and operational readiness. Compliance focus: OT/IT Segregation (NIST CSF-lite).

## Key Learning Objectives
- Translate OT/IT Segregation (NIST CSF-lite) requirements into implementable controls and measurable evidence
- Design segmented Layer-2/Layer-3 architecture with a clean IP plan and verification tests
- Deploy Windows Server services (AD/DNS/DHCP) and security-focused GPO baselines
- Implement firewall/NAT/ACL policy using least privilege and documented test cases
- Create a small Python automation deliverable with logged, repeatable output
- Produce runbooks, diagrams, and a final report suitable for an audit-style review

## Important Notes
Pieces of this project lived in three different places: Google Cloud Platform for the cloud and VM services (DC, DHCP, AD, etc.), Packet Tracer (overall topology, limited configuration), and on the physical Cisco networking equipment in the college labs (for testing, advanced configs, verification, rebuilds). As a result, the final presentation reflects more of a proof of concept/demo lab environment than a full-blown network solution for a large-scale client.

The final documentation provided in this repo reflect the culmination of 14 weeks of redesign, reconfiguration, and troubleshooting. It also includes the slide deck from our final presentation.

## Weekly Schedule
Week 1: Project charter, scope, repo, rebuild discipline
Week 2: Logical design & Packet Tracer prototype
Week 3: Switch base config, VLANs
Week 4: L2 Trunking, verification
Week 5: Inter-VLAN routing 
Week 6: Routing Validation
Week 7: AD, DNS, DCHP Foundations
Week 8: Windows Server Advanced Services
Week 9: ASA Firewall Configuration
Week 10: ASA NAT and ACL Validation
Week 11: Compliance Controls
Week 12: Python Automation to Cloud
Week 13: Disaster Recovery and Timed Rebuild Testing
Week 14: End to End Validation and Demo
Week 15: Presentation