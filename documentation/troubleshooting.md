# Troubleshooting Guide

## Instance Not Reachable
- Check Security Group rules
- Verify Bastion Host connection

## Application Not Loading
- Ensure port 80 is open
- Verify Python service is running

## ALB Health Check Failing
- Check target group configuration
- Confirm instance status is healthy

## No Internet in Private EC2
- Verify NAT Gateway routing
- Check route table associations