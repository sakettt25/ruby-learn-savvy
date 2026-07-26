# VISUAL DIAGRAMS FOR PRESENTATION

## 1. COMPLETE SYSTEM ARCHITECTURE

```
┌─────────────────────────────────────────────────────────────────────────┐
│                         SAVVY-SURFACE PLATFORM                          │
└─────────────────────────────────────────────────────────────────────────┘

                               CLIENT LAYER
                                    │
        ┌───────────────────────────┼───────────────────────────┐
        │                           │                           │
        ▼                           ▼                           ▼
┌──────────────────┐      ┌──────────────────┐      ┌──────────────────┐
│  Partner Portal  │      │  Investor App    │      │  Admin Dashboard │
│  (Distributor/   │      │  (Mobile/Web)    │      │  (Reporting/     │
│   RIA manage     │      │  Onboarding      │      │   Analytics)     │
│   investors)     │      │  & Portfolio     │      │                  │
└────────┬─────────┘      └────────┬─────────┘      └────────┬─────────┘
         │                         │                         │
         └─────────────────────────┼─────────────────────────┘
                                   │ HTTP/REST API
                                   ▼
        ┌─────────────────────────────────────────────────────┐
        │         RAILS API & ENGINE LAYER                    │
        │  ┌────────────────────────────────────────────────┐ │
        │  │ Routes: /deposits, /sips, /mandates, /accounts│ │
        │  │ Engines: api_admin, api_investor, crm, ...    │ │
        │  └────────────────────────────────────────────────┘ │
        └────────────────┬─────────────────────────────────────┘
                         │
        ┌────────────────┼────────────────┬─────────────────┐
        ▼                ▼                ▼                 ▼
    ┌────────┐      ┌────────┐      ┌────────┐        ┌────────┐
    │Business│      │ Access │      │Validation      │ Auth   │
    │ Logic  │      │Control │      │Callbacks       │        │
    │(Models)│      │        │      │                │        │
    └────────┘      └────────┘      └────────┘        └────────┘
        │
        ├─────────────────────┬──────────────────┬──────────────────┐
        │                     │                  │                  │
        ▼                     ▼                  ▼                  ▼
    ┌──────────┐         ┌──────────┐      ┌──────────┐     ┌──────────┐
    │ Partner  │         │Onboarding│     │Deposit   │     │Mandate   │
    │          │         │          │     │          │     │          │
    │ - AMC    │         │ - KYC    │     │- Payment │     │- Auth    │
    │ - Type   │         │ - Bank   │     │- Status  │     │- Status  │
    │ - Keys   │         │ - Verify │     │- Gateway │     │- Method  │
    └──────────┘         └──────────┘     └──────────┘     └──────────┘
        │                     │                  │                  │
        ├─────────────────────┴──────────────────┴──────────────────┤
        │                                                            │
        ▼                  DATA PERSISTENCE LAYER                   ▼
    ┌────────────────────────────────────────────────────────────────────┐
    │                                                                    │
    │  ┌──────────────┐  ┌──────────────┐  ┌──────────────────────┐   │
    │  │ PostgreSQL   │  │   Redis      │  │    Sidekiq Jobs      │   │
    │  │              │  │              │  │                      │   │
    │  │ - Persistent │  │ - Cache      │  │ - Async Processing   │   │
    │  │   Data       │  │ - Sessions   │  │ - Scheduled Jobs     │   │
    │  │ - ACID Txns  │  │ - KYC Data   │  │ - Retries/DLQ        │   │
    │  │ - Audit Log  │  │ - Performance│  │ - Background Tasks   │   │
    │  │              │  │   Data       │  │                      │   │
    │  └──────────────┘  └──────────────┘  └──────────────────────┘   │
    │                                                                    │
    └────────────────────────────────────────────────────────────────────┘
        │                     │                  │
        ▼                     ▼                  ▼
    ┌─────────────┐     ┌──────────────┐  ┌──────────────┐
    │Backup &     │     │Real-time     │  │Job Execution │
    │Replication  │     │Caching       │  │& Scheduling  │
    └─────────────┘     └──────────────┘  └──────────────┘
        │
        │              EXTERNAL INTEGRATIONS
        ▼
    ┌───────────────────────────────────────────────────────────┐
    │                                                           │
    ├─────────────┬────────────────┬────────────┬────────────┤
    │             │                │            │            │
    ▼             ▼                ▼            ▼            ▼
┌─────────┐ ┌─────────────┐ ┌──────────┐ ┌─────────┐ ┌─────────┐
│Payment  │ │KYC Gateway  │ │ RTA      │ │ Banking │ │Messaging│
│Gateway  │ │             │ │          │ │ Services│ │Services │
│         │ │- Signzy     │ │- CAMS    │ │         │ │         │
│-Razorpay│ │- CAMS       │ │- KARVY   │ │- SFTP   │ │- Twilio │
│-Billdesk│ │- Boharr     │ │- DSP     │ │- FTP    │ │-Sendgrid│
│-SBI     │ │             │ │          │ │         │ │- Gupshup│
│-Cashfree│ │(PAN Valid?) │ │(Register)│ │(File    │ │(Email/  │
│-Camspay │ │             │ │          │ │Transfer)│ │SMS/WA)  │
│-DSP     │ └─────────────┘ └──────────┘ └─────────┘ └─────────┘
└─────────┘
```

## 2. INVESTOR JOURNEY MAP

```
DAY 1: ONBOARDING
┌──────────────────────────────────────────────────────────────┐
│ Investor visits platform                                     │
│ ↓                                                            │
│ Fill personal details (name, PAN, DOB, address)            │
│ ↓                                                            │
│ System checks: PAN valid? (KYC API)                        │
│ ↓ (Real-time)                                               │
│ Verify email (one-time link)                               │
│ ↓                                                            │
│ Verify phone (OTP via SMS)                                 │
│ ↓                                                            │
│ Add bank account (number, IFSC, type)                      │
│ ↓                                                            │
│ ✅ ONBOARDING COMPLETE (15 min)                            │
└──────────────────────────────────────────────────────────────┘

DAY 2-3: INVESTMENT
┌──────────────────────────────────────────────────────────────┐
│ Browse funds → Select one (e.g., SBI Balanced Fund)        │
│ ↓                                                            │
│ Enter amount (system validates min/max)                    │
│ ↓                                                            │
│ Confirm details                                             │
│ ↓                                                            │
│ Redirected to Payment Gateway                              │
│ ↓                                                            │
│ Select payment method (UPI/Card/NetBanking)                │
│ ↓                                                            │
│ Complete payment (OTP, if needed)                          │
│ ↓                                                            │
│ Return to app: ✅ Payment Successful                       │
│ ↓ (Background: RTA registration)                           │
│ Next day: ✅ Units visible in portfolio                    │
└──────────────────────────────────────────────────────────────┘

DAY 4+: RECURRING INVESTMENT (SIP)
┌──────────────────────────────────────────────────────────────┐
│ Investor creates SIP (₹5000/month for 5 years)             │
│ ↓                                                            │
│ System creates MANDATE (authorization)                     │
│ ↓                                                            │
│ Investor approves via NetBanking/UPI                       │
│ ↓                                                            │
│ ✅ Mandate Active                                          │
│ ↓                                                            │
│ ✅ SIP Activated (starts next month)                       │
│ ↓                                                            │
│ EVERY MONTH (auto):                                        │
│   - Deposit created automatically                          │
│   - ₹5000 collected via mandate                            │
│   - RTA processes                                          │
│   - Units added                                            │
│   NO USER ACTION NEEDED                                    │
│ ↓                                                            │
│ After 60 months (5 years): ✅ SIP Complete                 │
│ Investor can: Continue, Pause, or Cancel                   │
└──────────────────────────────────────────────────────────────┘

ONGOING: PORTFOLIO MANAGEMENT
┌──────────────────────────────────────────────────────────────┐
│ Dashboard shows:                                             │
│  - All holdings (multiple funds)                            │
│  - Current value                                            │
│  - Gains/Losses (day, month, year)                          │
│  - NAV updates (real-time)                                  │
│                                                              │
│ Can:                                                         │
│  - Switch funds                                             │
│  - Add to existing SIP                                      │
│  - Download statements                                      │
│  - View transaction history                                │
│  - Redeem (sell) units                                      │
└──────────────────────────────────────────────────────────────┘
```

## 3. DEPOSIT CREATION FLOW (Technical)

```
REQUEST PHASE (Investor's browser)
┌────────────────────────────────────────────────┐
│ POST /deposits {                               │
│   fund_id: 123,                                │
│   amount: 10000,                               │
│   account_id: 456                              │
│ }                                              │
└──────────────────┬───────────────────────────────┘
                   │
                   ▼
           Rails Controller
           ├─ Validate amount
           ├─ Check fund active
           ├─ Create Deposit record
           └─ Call create_payment

PAYMENT PHASE (3rd party gateway)
           ↓
        ┌──────────────────────────────────────┐
        │ Redirect to Payment Gateway          │
        │ POST {                               │
        │   amount: 10000,                     │
        │   deposit_id: 789,                   │
        │   return_url: callback_url           │
        │ }                                    │
        └──────────────────┬───────────────────┘
                           │
                    Investor pays
                    (UPI/Card/NetBanking)
                           │
                           ▼
                    Payment processed ✅
                           │
                           ▼
        Callback sent to:
        POST /deposits/razorpay_redirect {
          razorpay_payment_id: "pay_xxx",
          notes: {
            deposit_id: 789
          }
        }
                           │
                           ▼
                   Rails Webhook Handler
                   ├─ Verify payment
                   ├─ Update status: payment_made
                   ├─ Store settlement_id
                   └─ Queue RTA job

ASYNC PHASE (Background job)
                           ↓
                   RTA Submission
                   ├─ Get deposit record
                   ├─ Call RTA API
                   ├─ Send to RTA
                   └─ Update status: submitted_to_rta

DAILY RECONCILIATION (Cron job at 10:30 AM)
                           ↓
                   RTA Mailback Processing
                   ├─ Download confirmation file from RTA
                   ├─ Parse units allocated
                   ├─ Update deposit with units
                   ├─ Mark status: completed
                   └─ Send webhook to partner

WEBHOOK NOTIFICATION
                           ↓
                   POST partner.webhook_url {
                     event: "deposit.completed",
                     deposit: {
                       id: 789,
                       amount: 10000,
                       units: 100,
                       status: "completed"
                     }
                   }
```

## 4. SIP AUTOMATION TIMELINE

```
CREATION (Day 1)
┌────────────┐
│ SIP Created│ Amount: ₹5000, Start: Feb 1, End: Feb 1, 2029
├────────────┤ Frequency: Monthly, Mandate: Pending
│ Status:    │
│ CREATED    │
└────────────┘

MANDATE (Day 1)
      ↓
┌────────────────┐
│ Mandate        │ Amount: ₹5000, Period: Feb 1 - Feb 1, 2030
├────────────────┤ Status: PENDING (awaiting investor approval)
│ Status:        │
│ PENDING        │
└────────────────┘
      ↓ (Investor approves via NetBanking/UPI)

SIP ACTIVATED (Day 3)
      ↓
┌────────────┐
│ SIP Active │ Now automated, waits for trigger day
├────────────┤
│ Status:    │
│ ACTIVE     │
└────────────┘

MONTH 1: FEB 1 (Sidekiq-Cron triggers at 6 AM)
      ↓
    Deposit 1 created automatically
    ├─ Amount: ₹5000
    ├─ Payment: Via Mandate (no user action)
    ├─ Sent to RTA
    └─ Units added next day
      
MONTH 2: MAR 1 → Deposit 2 (automatic)
      ↓
MONTH 3: APR 1 → Deposit 3 (automatic)
      ↓
...
MONTH 60: JAN 1, 2029 → Deposit 60 (final)
      ↓
┌────────────────┐
│ SIP            │ 60 deposits completed, ₹300,000 invested
├────────────────┤ 
│ Status:        │
│ COMPLETED      │
└────────────────┘

Investor can:
├─ View all 60 transactions
├─ See total units acquired
├─ See overall returns
└─ Choose: Extend, Pause, or Exit
```

## 5. MANDATE LIFECYCLE

```
CREATION
    │
    ▼
   PENDING ←─ Awaiting investor approval
    │
    ├─ Investor chooses auth method
    │  (NetBanking / Debit Card / UPI)
    │
    └─ Investor completes auth
       │
       ▼
    COMPLETED ←─ Now active, can debit
       │
       ├─ SIPs can use this mandate
       ├─ Auto-debits every month
       └─ Stored for future use
       │
       ├─ PAUSE ─→ PAUSED (temporary stop)
       │           │ (Can resume)
       │           └─ COMPLETED
       │
       ├─ CANCEL ─→ CANCELLED (permanent)
       │           (Cannot be reused)
       │
       └─ EXPIRE ─→ EXPIRED (time limit reached)
                   (Validity date passed)

Also possible:
PENDING ─→ ERROR (Auth failed, declined by bank)
PENDING ─→ EXPIRED (Mandate valid for 30 days, not activated)
```

## 6. PARTNER TYPES & THEIR ROLES

```
AMC (Asset Management Company)
├─ Creates funds
├─ Manages investments
├─ Registers with SEBI
├─ Can have their own distributor network
└─ Example: SBI MF, ICICI Prudential, HDFC

        │
        ├─────────────────────┐
        ▼                     ▼
    Distributor            RIA (Relationship Inv. Advisor)
    ├─ Sells funds          ├─ Sells funds to retail
    ├─ Partners with AMCs   ├─ Independent agent
    ├─ Has team of agents   ├─ One-person operation usually
    ├─ Bulk commission      ├─ Higher individual commission
    └─ Example: ABC         └─ Example: Mutual Fund advisor
      Financial Services      with SMS/WhatsApp marketing

Both use Savvy-Surface to:
├─ Onboard investors
├─ Process investments
├─ Manage SIPs
├─ Generate reports
└─ Track performance

Integration:
├─ Each gets API key (access_key)
├─ Each gets dashboard
├─ Webhooks notify them of events
└─ Real-time transaction tracking
```

## 7. TECHNOLOGY STACK PYRAMID

```
┌─────────────────────────────────┐
│                                 │
│   PRESENTATION LAYER            │
│   Web UI, Mobile App, Admin     │
│                                 │
└──────────────┬──────────────────┘
               │
┌──────────────┴──────────────────┐
│                                 │
│   API LAYER (Rails/REST)        │
│   Controllers, Routes, Engines  │
│                                 │
└──────────────┬──────────────────┘
               │
┌──────────────┴──────────────────┐
│                                 │
│   BUSINESS LOGIC LAYER          │
│   Models, Services, Jobs        │
│                                 │
└──────────────┬──────────────────┘
               │
      ┌────────┴────────┐
      │                 │
      ▼                 ▼
  ┌────────┐         ┌──────────┐
  │DATABASE│         │CACHE &   │
  │        │         │QUEUE     │
  │PostgreSQL         │Redis     │
  │        │         │Sidekiq   │
  └────────┘         └──────────┘
      │                 │
      └────────┬────────┘
               │
┌──────────────┴──────────────────┐
│                                 │
│   EXTERNAL INTEGRATION LAYER    │
│   Gateways, RTAs, KYC, Banks   │
│                                 │
└─────────────────────────────────┘

DEPLOYMENT:
Docker Container (runs Rails app + Sidekiq worker)
├─ Scales horizontally (multiple containers)
├─ Load balancer (Nginx/ELB)
└─ Database & Redis separately (managed services)
```

