# Security Design

This architecture follows a **zero direct exposure model** for application servers.

## Security Layers

- No public IPs for application EC2 instances
- SSH access only via Bastion Host
- Security Groups restrict inbound traffic
- ALB exposes only HTTP/HTTPS traffic
- NAT Gateway controls outbound access

## Principle Used
Least Privilege Access Model