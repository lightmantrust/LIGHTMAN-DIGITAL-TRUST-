# Disaster Recovery Playbook

| Scenario | RPO | RTO | Run-book | Last drill |
| -------- | --- | --- | -------- | ---------- |
| GitHub org deleted | 0 h | 30 min | [drills/github-org-delete.md](drills/github-org-delete.md) | 2025-10-04 |
| Domain hijacked | 0 h | 60 min | [drills/domain-hijack.md](drills/domain-hijack.md) | 2025-09-20 |
| All maintainers unreachable | 0 h | 24 h | [drills/bus-factor.md](drills/bus-factor.md) | 2025-08-30 |

## Emergency Contacts
- PagerDuty escalation: `lightman-dr` (primary) / `foundation-legal` (legal shard)
- Signal group: `LightMan-DR-2025` (QR invite in `/drills/signal-qr.png`)
- HAM frequency: 14.230 MHz USB (Sunday 12:00 UTC net)

## Cold Wallet Split
3-of-5 Shamir shards with law firms; restore command:
```bash
sops -d secrets/shamir.json.enc | shamir combine > cold-wallet.json
