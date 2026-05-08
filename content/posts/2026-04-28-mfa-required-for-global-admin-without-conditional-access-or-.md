---
title: "MFA required for Global Admin without Conditional Access or PIM enforcement"
date: 2026-04-28
tags: ["Azure", "AI", "Security"]
categories: ["curated"]
source_url: "https://techcommunity.microsoft.com/t5/azure/mfa-required-for-global-admin-without-conditional-access-or-pim/m-p/4515571#M22511"
description: "Hi,I'm analyzing a break-glass account scenario in Microsoft Entra ID and would like to validate a behavior I'm observing.The account:Has Global Administrator role (permanent assignment)Is excluded fr"
---

Hi,I'm analyzing a break-glass account scenario in Microsoft Entra ID and would like to validate a behavior I'm observing.The account:Has Global Administrator role (permanent assignment)Is excluded from all Conditional Access policies (fully validated)Is excluded from Authentication Methods policies and MFA Registration Campaign (fully validated)Has no per-user MFA enabled (disabled)PIM is not enforcing MFA (role is permanently active, no activation required)Security Defaults are disabledSSPR is not enforcing MFAAll configurable sources that could require MFA have been reviewed and fully ruled out.However, when signing into Microsoft Admin Portals (Entra/Azure), MFA is still required and cannot be skipped.In Sign-in logs:Conditional Access → Not AppliedAuthentication Details show:"MFA required in Azure AD""App requires multifactor authentication"Additionally, there is a Microsoft-managed policy:"Multifactor authentication for admins accessing Microsoft Admin Portals"but it is in Report



🔗 [Read the full article](https://techcommunity.microsoft.com/t5/azure/mfa-required-for-global-admin-without-conditional-access-or-pim/m-p/4515571#M22511)

---
*Curated by Cyril Bou-Harb — Solution Engineer, Cloud & AI at Microsoft.*
*Views are my own.*
