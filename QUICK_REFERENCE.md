# QUICK REFERENCE CARD - 5 MINUTE READ

## THE ELEVATOR PITCH (30 seconds)

**Savvy-Surface** is a Ruby on Rails platform that automates mutual fund distribution in India. It connects investors, distributors, and fund companies, handling everything from investor onboarding to automated recurring investments and RTA registration.

**In one sentence**: "It's the Shopify for mutual fund distribution in India."

---

## THE 3-MINUTE VERSION

### What Does It Do?

1. **Investor Onboarding** → KYC verification, bank account setup, phone verification (15 min)
2. **Lump-Sum Investments** → Payment via multiple gateways, RTA registration (5 min + 1 day)
3. **Recurring Investments (SIPs)** → Mandate creation, then automatic monthly investments (fully automated)

### Who Uses It?

- **Investors**: Easy investment app
- **Distributors/RIAs**: Sell funds with less operational overhead
- **AMCs**: Reach new distribution partners
- **Platform**: Powers 1000+ partners, 500K+ investors, ₹50,000+ crores AUM

### How Does It Work?

```
Investor → Platform → Payment Gateway → RTA → Portfolio
                    ↓
                Background Jobs
                (Async processing)
```

### Key Technologies

- **Backend**: Ruby on Rails 7.0
- **Database**: PostgreSQL (data persistence)
- **Cache**: Redis (instant lookups, job queue)
- **Jobs**: Sidekiq (1000s daily background tasks)
- **Container**: Docker (deployment & scaling)

---

## RUBY CONCEPTS IN 2 MINUTES

### 1. Models (Database Tables in Ruby)
```ruby
class Deposit < ApplicationRecord
  belongs_to :fund
  belongs_to :account
  validates_presence_of :amount
end

# Usage: Deposit.create(amount: 10000, fund_id: 1)
```

### 2. Relationships
```ruby
# One partner has many deposits
Partner.has_many :deposits
deposit.partner  # Access related partner
```

### 3. Status Management (Enums)
```ruby
enum status: { pending: 'pending', completed: 'completed' }
deposit.completed?  # Query method
Deposit.completed   # Find all completed
```

### 4. Automated Behavior (Callbacks)
```ruby
after_commit :trigger_webhook, on: :create
# Automatically runs after deposit is created
```

### 5. Filtering (Scopes)
```ruby
scope :successful, ->{ where.not(status: 'error') }
Deposit.successful  # Get all successful deposits
```

### 6. Complex Logic (Instance Methods)
```ruby
def can_create_sip?
  mandates.completed.present? && account.present?
end
```

---

## THE DATA FLOW IN 3 STEPS

### Step 1: Investor Onboarding
```
Fill form → KYC check (API) → Verify email/phone → Add bank → ✅ Done
```

### Step 2: One-Time Investment
```
Select fund → Pay → Webhook callback → RTA registration (async) → Units allocated
```

### Step 3: Recurring Investment (SIP)
```
Create SIP → Create mandate → Investor approves → Activate
    ↓
    Every month (automatic):
    Create deposit → Collect payment → RTA registration → Add units
```

---

## KEY MODELS (What Gets Stored)

| Model | Purpose | Key Fields |
|-------|---------|-----------|
| **Partner** | Distribution partner | name, code, partner_type (AMC/Distributor/RIA) |
| **Onboarding** | Investor profile | pan_number, email, phone, kyc_verified |
| **Account** | Folio with one AMC | folio_number, amc_id, holding_mode |
| **Fund** | Mutual fund scheme | code, name, nav, minimum_amount |
| **Deposit** | One-time investment | amount, units, status, payment_gateway |
| **SIP** | Recurring investment | amount, frequency, start_date, end_date |
| **Mandate** | Payment authorization | amount, status, authentication_method |

---

## BACKGROUND JOBS (The Magic)

**Why needed**: Long operations shouldn't block user's request

```
User clicks "Submit"
    ↓
Job queued in Redis → Return response immediately ✅
    ↓
Meanwhile, background worker processes:
├─ Call RTA API (might take 5 seconds)
├─ Update database
├─ Send notifications
└─ All without user waiting
```

**Examples**:
- `TriggerSipWorker`: Monthly SIP execution
- `RtaSubmissionWorker`: Send deposit to RTA
- `ReconciliationWorker`: Daily RTA file processing
- `WebhookWorker`: Notify partners

---

## PAYMENT FLOW

```
Step 1: Investor selects fund & amount
    ↓
Step 2: Redirect to payment gateway (chosen based on AMC)
    ↓
Step 3: Investor pays (UPI/Card/NetBanking)
    ↓
Step 4: Gateway sends callback (webhook)
    ↓
Step 5: Deposit status updated to "payment_made"
    ↓
Step 6: Background job sends to RTA
    ↓
Step 7: Daily reconciliation adds units
    ↓
Step 8: Partner notified via webhook
```

---

## INTEGRATIONS (External Systems)

| Category | Examples | Purpose |
|----------|----------|---------|
| **Payment** | Razorpay, Billdesk, SBI, Cashfree | Collect payments |
| **KYC** | Signzy, CAMS, Boharr | Verify investor identity |
| **RTA** | CAMS, KARVY, DSP | Register funds officially |
| **Messaging** | Twilio, Sendgrid, Gupshup | SMS/Email/WhatsApp |

---

## SCALING SOLUTION

### Problem
What if 100,000 SIPs all trigger on 1st of month simultaneously?

### Solution
1. **Async queuing** → Jobs queued in Redis (not processed immediately)
2. **Multiple workers** → 10 Sidekiq workers process in parallel
3. **Batch processing** → 1000 SIPs per batch operation
4. **Database optimization** → Indexes for fast queries
5. **Caching** → Redis prevents repeated DB hits

Result: Can handle 1M+ jobs daily ✅

---

## COMMON QUESTIONS

**Q: How is this different from other fintech apps?**
A: Purpose-built for mutual fund distribution with deep RTA integration. Not general banking app.

**Q: What if payment gateway is down?**
A: Multiple gateways available, automatic fallback. Jobs retry automatically.

**Q: How do you ensure data safety?**
A: PostgreSQL transactions (ACID), audit trails for every change, encrypted backups.

**Q: Can investor have multiple accounts?**
A: Yes! One account per AMC. Can hold SBI + ICICI + HDFC funds simultaneously.

**Q: What happens to investor data?**
A: Permanently stored, encrypted, available via API, compliant with regulations.

---

## TECHNICAL STACK SUMMARY

```
┌─────────────────────────────────┐
│ CLIENT (Web/Mobile App)         │
└────────────────────┬────────────┘
                     │ REST API
         ┌───────────┴────────────┐
         │ Rails 7.0 API Server   │
         ├─ Controllers           │
         ├─ Models                │
         ├─ Services              │
         └─ Engines               │
         │                         │
    ┌────┴────┐      ┌──────────┐ │
    │PostgreSQL│      │  Redis   │ │
    │(Data)   │      │(Cache)   │ │
    └─────────┘      │(Jobs)    │ │
                     └──────────┘ │
                                 │
    ┌────────────────────────────┐
    │ Sidekiq Workers            │
    │ (Background Processing)    │
    └────────────────────────────┘
         │
    ┌────┴────┬────────┬────────┐
    │ Payment  │ KYC    │ RTA    │
    │ Gateways │ Service│ System │
    └─────────┴────────┴────────┘
```

---

## PRESENTATION TALKING POINTS

1. **Automation**: What takes 5-7 days manually → 15 min + 1 day automatic
2. **Scale**: 1000s of distribution partners, 500K+ investors on one platform
3. **Integration**: Connects multiple complex fintech systems seamlessly
4. **Reliability**: 99.9% uptime, comprehensive audit trails for compliance
5. **Engineering**: Async-first architecture, modular design, horizontal scaling

---

## FINAL TAKEAWAY

**Savvy-Surface** is not just an app. It's a **distribution platform** that powered an entire ecosystem of mutual fund investing in India.

Key achievements:
- ✅ Automated what was manual
- ✅ Scaled from 10s to 100Ks of daily transactions
- ✅ Reduced operational costs by 60-70%
- ✅ Enabled new distribution partnerships
- ✅ Improved investor experience (fast, simple, 24/7)

**It's the infrastructure that makes modern digital investing possible.**

---

## BEFORE YOUR PRESENTATION

✅ Read RUBY_PROJECT_GUIDE.md (comprehensive reference)
✅ Review VISUAL_DIAGRAMS.md (for slides)
✅ Know the 3 main flows (Onboarding → Deposit → SIP)
✅ Understand the tech stack choices
✅ Practice explaining Ruby concepts simply
✅ Have examples ready (real numbers from the project)

🎯 **GOAL**: Help audience understand not just WHAT it does, but WHY it was built this way.

**GOOD LUCK! 🚀**
