# 🚀 COMPLETE RUBY ON RAILS PROJECT GUIDE: Savvy-Surface

## TABLE OF CONTENTS
1. [Executive Summary](#executive-summary)
2. [Project Overview](#project-overview)
3. [Architecture & Tech Stack](#architecture--tech-stack)
4. [Ruby Concepts Used](#ruby-concepts-used)
5. [Complete Data Flow](#complete-data-flow)
6. [Key Models & Relationships](#key-models--relationships)
7. [Module Breakdown](#module-breakdown)
8. [Payment Gateway Integration](#payment-gateway-integration)
9. [Background Jobs](#background-jobs)
10. [Presentation Talking Points](#presentation-talking-points)

---

## EXECUTIVE SUMMARY

**Savvy-Surface** is a **Mutual Fund Investment Platform** built with Ruby on Rails. It's an enterprise-grade fintech application that enables:

- Multiple investment partners (AMCs, Distributors, RIAs) to distribute mutual funds
- Investors to make lump-sum investments (one-time deposits)
- Investors to setup recurring investments (SIPs - Systematic Investment Plans)
- Complete investor onboarding with KYC (Know Your Customer)
- Multiple payment gateway support (Razorpay, Billdesk, SBI, Cashfree, etc.)
- Complex mandate management for recurring payments
- Integration with RTAs (Registrars & Transfer Agents) for fund processing

Think of it as a **gateway platform** connecting investment partners with investors, handling the complete lifecycle from onboarding to fund registration with RTAs.

---

## PROJECT OVERVIEW

### What Problem Does It Solve?

Mutual fund distribution typically involves multiple intermediaries:
- **AMCs** (Asset Management Companies) - They manage funds
- **Distributors/RIAs** (Relationship Managers) - They sell funds to investors
- **Investors** - People wanting to invest
- **Payment Gateways** - Processing payments
- **RTAs** (Registrars) - Official fund registration

**Before Savvy-Surface**: Each party handled this manually, inconsistently
**After Savvy-Surface**: All integrated through one platform

### Real-World Use Case

A distributor wants to sell SBI Mutual Funds to customers. Instead of:
1. Manually collecting investor info
2. Calling payment providers
3. Registering with RTAs manually
4. Tracking everything in spreadsheets

They can:
1. Use Savvy-Surface API/Web interface
2. Platform handles everything automatically
3. All records tracked and synced

---

## ARCHITECTURE & TECH STACK

### Technology Stack

```
LANGUAGE: Ruby 3.2.8
FRAMEWORK: Rails 7.0.2+
DATABASE: PostgreSQL (main data store)
CACHE/SESSION: Redis (in-memory caching & background jobs)
WEB SERVER: Puma 5.6.4
BACKGROUND JOBS: Sidekiq (async processing)
CONTAINER: Docker (deployment)
```

### Key Dependencies (from Gemfile)

```ruby
Rails 7.0.2         # Web framework
PostgreSQL          # Database
Puma                # Web server
Sidekiq             # Background jobs
Sidekiq-Cron        # Scheduled jobs
Redis               # Caching & job queue

# Payment Processing
Razorpay           # Payment gateway
# Twilio            # SMS notifications
HTTParty           # HTTP requests to external APIs

# Authentication & Authorization
JWT                # Token-based auth
Devise             # User authentication
CanCanCan          # Authorization

# Data Management
Active Model Serializers  # JSON serialization
Kaminari                  # Pagination
Audited                   # Audit trails

# Admin Panel
Motor-Admin        # Admin dashboard
```

### Architecture Diagram

```
                    ┌─────────────────────────────────────────────────┐
                    │           CLIENT APPLICATIONS                   │
                    │ Web/Mobile Apps, Partner Platforms, Admin Panel │
                    └──────────────────────┬──────────────────────────┘
                                           │ API Requests
                                           ▼
                    ┌─────────────────────────────────────────────────┐
                    │     RAILS APPLICATION (Savvy-Surface)           │
                    │  ┌─────────────────────────────────────────┐   │
                    │  │ Controllers Layer (API, Web)            │   │
                    │  │ - Partner Controller                    │   │
                    │  │ - Deposit Controller                    │   │
                    │  │ - Onboarding Controller                 │   │
                    │  │ - Mandate Controller                    │   │
                    │  │ - Fund Controller                       │   │
                    │  └─────────────────────────────────────────┘   │
                    │                      │                          │
                    │  ┌─────────────────────────────────────────┐   │
                    │  │ Business Logic Layer (Models)           │   │
                    │  │ - Partner (multi-type)                  │   │
                    │  │ - Deposit (transactions)                │   │
                    │  │ - Account (folios)                      │   │
                    │  │ - SIP (recurring investments)           │   │
                    │  │ - Mandate (payment authorization)       │   │
                    │  │ - Fund (mutual fund schemes)            │   │
                    │  │ - Onboarding (investor setup)           │   │
                    │  │ - Withdrawal (redemptions)              │   │
                    │  └─────────────────────────────────────────┘   │
                    │                      │                          │
                    │  ┌─────────────────────────────────────────┐   │
                    │  │ Data Layer (Models)                     │   │
                    │  └─────────────────────────────────────────┘   │
                    └──────────────────┬──────────────────────────────┘
                                       │
                ┌──────────────────────┼──────────────────────────────┐
                ▼                      ▼                              ▼
         ┌────────────────┐   ┌──────────────────┐   ┌──────────────────┐
         │  PostgreSQL    │   │  Redis Cache &   │   │   Sidekiq Jobs   │
         │  Database      │   │  Background Que  │   │  (Async Tasks)   │
         │                │   │                  │   │                  │
         │ - Partners     │   │ - Sessions       │   │ - Register SIPs  │
         │ - Deposits     │   │ - KYC Cache      │   │ - Send Webhooks  │
         │ - Accounts     │   │ - Performance    │   │ - Trigger Mandates
         │ - SIPs         │   │   Data           │   │ - Fund Operations│
         │ - Mandates     │   │                  │   │ - Reconciliation │
         │ - Funds        │   │                  │   │ - Email/SMS      │
         │ - Onboardings  │   │                  │   │                  │
         └────────────────┘   └──────────────────┘   └──────────────────┘
                ▼                      ▼                              ▼
         ┌────────────────┐   ┌──────────────────┐   ┌──────────────────┐
         │  External APIs │   │  RTAs            │   │  Webhooks        │
         │                │   │  (Fund Registry) │   │  (Callbacks)     │
         │ - KYC Gateway  │   │                  │   │                  │
         │ - Payment GW   │   │ - CAMS           │   │ Partners get     │
         │ - SMS/Email    │   │ - KARVY          │   │ real-time updates│
         │ - Banking      │   │ - DSP            │   │                  │
         └────────────────┘   └──────────────────┘   └──────────────────┘
```

---

## RUBY CONCEPTS USED

### 1. MODELS & ACTIVE RECORD (Object-Relational Mapping)

```ruby
# Active Record automatically maps Ruby objects to database tables
class Deposit < ApplicationRecord
  belongs_to :account          # One-to-Many relationship
  belongs_to :fund
  has_many :brokerage_payouts  # This deposit can have many payouts
  
  enum status: {               # Enum for status values
    created: 'created',
    submitted_to_sip_pg: 'submitted_to_sip_pg',
    payment_made: 'payment_made',
    completed: 'completed',
    error: 'error'
  }
end

# Usage:
deposit = Deposit.find(1)                    # Find by ID
deposit.status = 'payment_made'              # Use enum
deposit.account                              # Access related account
```

**CONCEPT EXPLAINED:**
- Active Record = Ruby way of accessing database tables
- Each model class = one database table
- Each instance = one row in that table
- Relationships = `belongs_to`, `has_many`, `has_one`

### 2. ASSOCIATIONS & RELATIONSHIPS

Rails uses clever shortcuts for database relationships:

```ruby
# ONE-TO-MANY: One Partner has many Deposits
class Partner < ApplicationRecord
  has_many :deposits           # Partner.deposits returns all related deposits
end

class Deposit < ApplicationRecord
  belongs_to :partner          # deposit.partner returns the associated partner
end

# MANY-TO-MANY: Partner has many SIPs through Mandates
class Partner < ApplicationRecord
  has_many :mandates
end

class Mandate < ApplicationRecord
  belongs_to :partner
  has_many :sips
end

# USAGE:
partner = Partner.find(1)
partner.deposits              # All deposits by this partner
partner.deposits.sum(:amount) # Total amount deposited
partner.mandates              # All mandates from this partner
```

### 3. SCOPES (Filtering Data)

```ruby
class Deposit < ApplicationRecord
  # Define reusable filters
  scope :successful, ->{ 
    where.not(status: [Deposit::statuses[:created], Deposit::statuses[:error]]) 
  }
  scope :completed, ->{ 
    where(status: Deposit::statuses[:completed]) 
  }
end

# USAGE:
Deposit.successful           # Only successful deposits
Deposit.completed            # Only completed ones
Deposit.successful.completed # Chain scopes
```

### 4. VALIDATIONS (Data Integrity)

```ruby
class Deposit < ApplicationRecord
  validates_presence_of :amount          # Can't be blank
  validate :fund_minimums                # Custom validation method
  validate :fund_accepting_lumpsums, on: :create  # Only on create
  validate :cannot_update_details_after_paying, on: :update
  
  private
  
  def fund_minimums
    if amount < fund.minimum_amount
      errors.add(:amount, "is below minimum #{fund.minimum_amount}")
    end
  end
end

# USAGE:
deposit = Deposit.new(amount: 10)
deposit.save  # Returns false if validations fail
deposit.errors.full_messages  # See what failed
```

### 5. CALLBACKS (Hooks in Object Lifecycle)

```ruby
class Partner < ApplicationRecord
  after_initialize :set_defaults    # When object is created
  after_create :create_credentials  # Right after saving to DB
  after_update :fix_motor_admin_tags # After any update
  before_save :validate_partner_type # Before saving
end

class Deposit < ApplicationRecord
  after_commit :trigger_webhook_on_create, on: :create
  after_commit :trigger_webhook_on_update, on: :update
end

# USAGE: Automatic behavior without explicit calls
partner = Partner.new
partner.save  # Triggers: after_initialize → after_create → after_commit
```

### 6. ENUMS (Type-Safe Status Management)

```ruby
class Deposit < ApplicationRecord
  enum status: { 
    created: 'created',
    payment_made: 'payment_made',
    completed: 'completed'
  }
  
  enum payment_gateway: { 
    razorpay: 'razorpay',
    billdesk: 'billdesk',
    sbi: 'sbi'
  }
end

# USAGE: Type-safe instead of error-prone strings
deposit.status = :payment_made        # Using symbol
deposit.payment_made?                 # Query method (returns true/false)
deposit.status_changed?               # Detect changes
Deposit.payment_made                  # Find all with this status
```

### 7. INSTANCE METHODS (Custom Logic)

```ruby
class Partner < ApplicationRecord
  # Method that checks partner type and business logic
  def is_amc?
    return true if partner_type == Partner::partner_types[:amc]
    
    # Check if parent is sponsoring AMC
    current_parent = parent
    while(current_parent != nil)
      return true if current_parent.amc? && current_parent.is_sponsoring_children?
      current_parent = current_parent.parent
    end
    false
  end
  
  def funds(amc_code, generic_checkout_uuid=nil)
    # Complex logic to filter funds based on partner type
    amcs = amc_permissions.map(&:amc)
    
    if amc_code.present?
      amc_ids = [amcs.find { |amc| amc.code == amc_code }.try(:id)].compact
    else
      amc_ids = amcs.map(&:id)
    end
    
    f_list = Fund.where(amc_id: amc_ids).active
    f_list = f_list.regular unless is_amc?
    f_list
  end
end

# USAGE:
partner = Partner.find(1)
partner.is_amc?              # Calls the method
partner.funds('SBI')         # Gets funds for SBI AMC
```

### 8. CLASS METHODS (Static Methods)

```ruby
class Deposit < ApplicationRecord
  def self.rta_payment_mode(mode)
    if mode == Deposit::payment_modes[:bank_transfer]
      'RTGS'  # Convert to RTA format
    else
      mode
    end
  end
end

# USAGE:
Deposit.rta_payment_mode('bank_transfer')  # Called on class, not instance
```

### 9. MODULES & CONCERNS (Code Reusability)

```ruby
# app/models/concerns/webhookable.rb
module Webhookable
  included do
    after_commit :trigger_webhook_on_create, on: :create
    after_commit :trigger_webhook_on_update, on: :update
  end
end

# Usage - any model can include this
class Deposit < ApplicationRecord
  include Webhookable  # Automatically gets webhook callbacks
end

class Mandate < ApplicationRecord
  include Webhookable  # Reused!
end
```

### 10. BEFORE/AFTER HOOKS & QUERY METHODS

```ruby
class Mandate < ApplicationRecord
  after_update :notify, if: :status_changed?  # Conditional callback
  
  def signed?
    status == Mandate::statuses[:completed]
  end
  
  def unexpired?
    mandate_last_date > Date.today
  end
  
  def set_completed!
    update!(status: Mandate::statuses[:completed])
  end
end

# USAGE:
mandate.status = 'completed'
mandate.save  # Triggers :notify callback only if status changed
mandate.signed?     # Query method
mandate.unexpired?  # Query method
```

### 11. BLOCKS & LAMBDAS (Functional Programming)

```ruby
class Fund < ApplicationRecord
  scope :active, ->(){ where(active: true) }
  scope :regular, ->(){ where(is_regular_scheme: true) }
end

# USAGE:
Fund.active.regular  # Chaining scopes

# In partne.rb - using map and select with blocks
def funds(amc_code, generic_checkout_uuid=nil)
  amcs = amc_permissions.map(&:amc)  # Map each permission to its AMC
  
  f_list.select { |fund| fund.active? }  # Select active ones
end
```

### 12. SELF-REFERENTIAL ASSOCIATIONS (Hierarchies)

```ruby
class Partner < ApplicationRecord
  belongs_to :parent, class_name: 'Partner', optional: true
  has_many :children, class_name: 'Partner', foreign_key: 'parent_id'
end

# USAGE: Build parent-child hierarchy
# Parent Partner → Can have child Partners (sub-distributors)
parent_partner = Partner.find(1)
parent_partner.children      # Get all child partners
parent_partner.parent        # Get parent if exists
```

### 13. OPTIONAL RELATIONSHIPS

```ruby
class Deposit < ApplicationRecord
  belongs_to :account, optional: true      # Account can be null
  belongs_to :onboarding, optional: true   # Onboarding can be null
end

# Without optional: true → Rails requires these to always exist
```

### 14. INCLUDES & EAGER LOADING (Performance)

```ruby
# This would cause N+1 queries problem:
deposits = Deposit.all
deposits.each { |d| puts d.account.name }  # Query for each deposit

# Solution:
deposits = Deposit.includes(:account)  # Load accounts upfront
deposits.each { |d| puts d.account.name }  # No extra queries
```

---

## COMPLETE DATA FLOW

### 1. INVESTOR ONBOARDING FLOW

```
┌─────────────────────────────────────────────────────────────────┐
│ STEP 1: Investor visits Partner's Website/App                  │
│         (e.g., Distributor's online platform)                  │
└──────────────────────────┬──────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│ STEP 2: Investor Submits Details                               │
│         - Name, PAN, Email, Phone, DOB                         │
│         - Address, Occupation, Annual Income                   │
│         - Tax Status (Individual, HUF, NRI, etc.)              │
│                                                                 │
│ RAILS MODEL: Onboarding.create(params)                         │
│ DATABASE TABLE: onboardings                                    │
└──────────────────────────┬──────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│ STEP 3: KYC Verification                                       │
│         - PAN is sent to KYC Gateway (Signzy/CAMS/Boharr)     │
│         - Verifies: Is PAN valid? Existing investor?           │
│         - Gets cached data if available                        │
│         - Stored in Redis for quick future lookups             │
│                                                                 │
│ CODE: Onboarding.check_kyc(pan, partner)                       │
│ CACHE: Redis.current.set "KYC::#{pan}"                         │
└──────────────────────────┬──────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│ STEP 4: Add Bank Account                                       │
│         - Investor provides bank details                       │
│         - Account number, IFSC, Account type                   │
│         - Bank Account created & linked to Onboarding         │
│                                                                 │
│ RAILS MODEL: BankAccount.create(onboarding_id, bank_details)   │
└──────────────────────────┬──────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│ STEP 5: OTP Verification                                       │
│         - SMS sent to registered phone number                  │
│         - Investor enters OTP                                  │
│         - Phone number marked as verified                      │
│                                                                 │
│ GATEWAY: Twilio (SMS service)                                  │
└──────────────────────────┬──────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│ STEP 6: Create Account/Folio with AMC                          │
│         - Background Job triggered (Sidekiq)                   │
│         - Contact AMC's RTA to open Folio                      │
│         - Receive Folio Number from RTA                        │
│         - Folio linked to Investor's Onboarding               │
│                                                                 │
│ RAILS MODEL: Account.create(onboarding, amc, folio_number)     │
│ JOB: Rta::CreateFolioWorker.perform_async                      │
└──────────────────────────┬──────────────────────────────────────┘
                           │
                           ▼
        ✅ ONBOARDING COMPLETE - Ready for Investments
```

### 2. DEPOSIT (LUMP-SUM INVESTMENT) FLOW

```
┌─────────────────────────────────────────────────────────────────┐
│ STEP 1: Investor Chooses Investment Amount                     │
│         - Select Fund (e.g., SBI Balanced Fund)                │
│         - Enter Amount (e.g., ₹10,000)                         │
│         - Check Minimum/Maximum limits                         │
│                                                                 │
│ VALIDATION:                                                    │
│   - Amount >= fund.minimum_amount                              │
│   - Amount <= fund.maximum_amount (if exists)                  │
│   - Fund is Active                                             │
│                                                                 │
│ RAILS MODEL: Deposit.create(amount, fund, account)             │
│ STATUS: 'created'                                              │
└──────────────────────────┬──────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│ STEP 2: Create Payment                                         │
│         - Deposit.create_payment() called                      │
│         - Redirects to Payment Gateway                         │
│         - Gateways: Razorpay, Billdesk, SBI, Cashfree, DSP    │
│         - Investor completes payment (UPI/NetBanking/Card)     │
│                                                                 │
│ CODE: fund.amc.payment_gateway.create_payment(deposit)         │
│ STATUS: 'submitted_to_sip_pg'                                  │
└──────────────────────────┬──────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│ STEP 3: Payment Confirmation                                   │
│         - Payment Gateway sends callback (webhook)             │
│         - Deposit status updated to 'payment_made'             │
│         - Settlement ID & PG Reference ID stored               │
│         - Background job triggered to register with RTA        │
│                                                                 │
│ DATABASE FIELDS:                                               │
│   - settlement_id: from bank                                   │
│   - request_id: from payment gateway                           │
│   - user_completed_payment_at: timestamp                       │
│ STATUS: 'payment_made'                                         │
│ JOB: SubmitToRtaWorker.perform_async(deposit_id)               │
└──────────────────────────┬──────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│ STEP 4: Register with RTA                                      │
│         - RTA is: CAMS, KARVY, DSP (Fund Registry)            │
│         - Deposit details sent to RTA                          │
│         - RTA validates and registers purchase                 │
│         - RTA sends confirmation file (mailback)               │
│                                                                 │
│ INTEGRATION: partner.rta.create_purchase([deposit], 'UPI')     │
│ STATUS: 'submitted_to_rta'                                     │
└──────────────────────────┬──────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│ STEP 5: RTA Confirmation & Settlement                          │
│         - RTA mailback file processed (Reconciliation Job)      │
│         - Units allocated to investor                          │
│         - Settlement happens                                   │
│         - Deposit marked as completed                          │
│         - Webhook sent to Partner notifying completion         │
│                                                                 │
│ STATUS: 'completed'                                            │
│ WEBHOOK: POST to partner.webhook.url with deposit data         │
└──────────────────────────┬──────────────────────────────────────┘
                           │
                           ▼
        ✅ INVESTMENT COMPLETE - Units in Investor's Account
        
UNITS CALCULATION:
        Amount           10,000
        Fund NAV       = 100 (Net Asset Value per unit)
        ───────────────
        Units          = 100 units worth ₹10,000
```

### 3. SIP (RECURRING INVESTMENT) FLOW

```
┌─────────────────────────────────────────────────────────────────┐
│ STEP 1: Create SIP (Recurring Investment)                      │
│         - Investor sets up automatic investments               │
│         - Amount: ₹5,000 per month                             │
│         - Start Date: 1st of next month                        │
│         - End Date: 1st of month 5 years later                 │
│         - Frequency: Monthly                                   │
│                                                                 │
│ RAILS MODEL: Sip.create(                                       │
│   account: account,                                            │
│   fund: fund,                                                  │
│   amount: 5000,                                                │
│   frequency: 'monthly',                                        │
│   start_date: Date.tomorrow,                                   │
│   end_date: 5.years.from_now                                   │
│ )                                                              │
│ STATUS: 'created'                                              │
└──────────────────────────┬──────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│ STEP 2: Create Mandate (Authorization)                         │
│         - Before SIP can start, need payment authorization     │
│         - Investor authorizes via mandate                      │
│         - Mandate = "I allow you to debit X amount Y times"    │
│         - Amount must be >= SIP amount                         │
│         - Duration must be >= SIP duration                     │
│         - Gateways: Razorpay, Billdesk, Cashfree, SBI, DSP    │
│                                                                 │
│ RAILS MODEL: Mandate.create(                                   │
│   partner: partner,                                            │
│   bank_account: bank_account,                                  │
│   amount: 5000,                                                │
│   frequency: 'monthly'                                         │
│ )                                                              │
│ CODE: sip.create_mandate(extras)                               │
│ STATUS: 'pending'                                              │
│                                                                 │
│ MANDATE AUTHENTICATION METHODS:                                │
│   - Net Banking                                                │
│   - Debit Card OTP                                             │
│   - UPI (Intent or Collect)                                    │
│   - QR Code                                                    │
└──────────────────────────┬──────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│ STEP 3: Mandate Approval                                       │
│         - Investor completes mandate authentication            │
│         - Bank/Gateway confirms                                │
│         - Mandate status: 'completed'                          │
│         - Now SIP can be activated                             │
│         - Mandate registered with RTA                          │
│                                                                 │
│ CODE: mandate.register_with_rta                                │
│ STATUS: 'completed'                                            │
└──────────────────────────┬──────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│ STEP 4: Activate SIP                                           │
│         - SIP validates:                                       │
│         - Start date >= today + 2 business days               │
│         - Mandate is completed and unexpired                   │
│         - Amount fits within mandate                           │
│         - SIP marked as 'active'                               │
│         - Scheduled job created for execution                  │
│                                                                 │
│ CODE: sip.activate                                             │
│ STATUS: 'active'                                               │
│ JOB QUEUE: Sidekiq schedules recurring jobs                    │
└──────────────────────────┬──────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│ STEP 5: Auto-Execution (Every Month)                           │
│         - On SIP day (e.g., 1st of month):                     │
│         - Background Job triggers (TriggerSipWorker)           │
│         - Deposit created automatically for SIP amount         │
│         - Payment collected via mandate (no user action)       │
│         - Goes through same process as regular deposit         │
│         - Repeats until SIP end date                           │
│                                                                 │
│ JOB: Rta::TriggerSipWorker.perform_async(sip_id)               │
│ NEW DEPOSIT STATUS: 'created' → following full flow            │
│ FREQUENCY: Sidekiq-Cron runs on schedule                       │
└──────────────────────────┬──────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│ STEP 6: SIP Cancellation (Optional)                            │
│         - Investor can cancel anytime                          │
│         - Reason recorded (e.g., 'scheme not performing')      │
│         - Future SIPs not created                              │
│         - Can pause for 1-3 cycles instead of cancel           │
│         - Mandate can be cancelled or kept for future use      │
│                                                                 │
│ CODE: sip.cancel(reason, remark)                               │
│ STATUS: 'cancellation_requested' → 'cancelled'                 │
│ MANDATE STATUS: Can remain 'completed' for other use           │
└──────────────────────────┬──────────────────────────────────────┘
                           │
                           ▼
        ✅ RECURRING INVESTMENTS COMPLETE
```

---

## KEY MODELS & RELATIONSHIPS

### Model Hierarchy & Relationships Diagram

```
                            ┌──────────────┐
                            │     AMC      │
                            │ (Fund Manager)
                            └──────┬───────┘
                                   │ has_many :funds
                                   │
                    ┌──────────────┼──────────────┐
                    ▼              ▼              ▼
                ┌────────┐    ┌────────┐    ┌──────────┐
                │ Fund 1 │    │ Fund 2 │    │ Fund ... │
                └────────┘    └────────┘    └──────────┘
                    │
                    │ has_many :deposits
                    │ has_many :withdrawals
                    │
        ┌───────────┼───────────────────┐
        ▼           ▼                   ▼
    ┌───────┐  ┌─────────┐          ┌──────────┐
    │ DEPOSIT
│  │ WITHDRAW│          │ REINVEST │
    │ (Buy)  │  │ (Sell) │          │ (Dividend)
    └───────┘  └─────────┘          └──────────┘


        ┌─────────────────┐
        │    PARTNER      │
        │ (Distributor/   │
        │  RIA/AMC)       │
        └────────┬────────┘
                 │
    ┌────────────┼────────────┬────────────┐
    │            │            │            │
    ▼            ▼            ▼            ▼
┌───────────┐ ┌───────────┐ ┌─────┐ ┌──────────────┐
│ONBOARDING │ │ DEPOSIT   │ │ SIP │ │   MANDATE    │
│(KYC)      │ │(Buy Funds)│ │(Auto)│ │(Authorization)
└─────┬─────┘ └─────┬─────┘ └──┬──┘ └──────┬───────┘
      │             │          │          │
      └─────────┬───┴──────┬───┴──────┬───┘
                │          │          │
                ▼          ▼          ▼
            ┌─────────────────────┐
            │   BANK_ACCOUNT      │
            │  (Payment Details)  │
            └─────────────────────┘
                    │
                    │ belongs_to
                    │
            ┌───────┴────────┐
            ▼                ▼
        ┌────────┐      ┌─────────┐
        │ACCOUNT │      │ NOMINEE │
        │(Folio) │      │ (Heir)  │
        └────────┘      └─────────┘
```

### Detailed Model Descriptions

#### 1. **PARTNER** (Distribution Partner)
```ruby
class Partner < ApplicationRecord
  # Types
  enum partner_type: { amc: 'amc', distributor: 'distributor', ria: 'ria' }
  
  # Relationships
  has_many :onboardings
  has_many :accounts
  has_many :deposits
  has_many :sips
  has_many :mandates
  has_many :amc_permissions  # Which AMCs can this partner sell?
  belongs_to :parent, optional: true  # Hierarchical (sub-distributors)
  has_many :children, class_name: 'Partner'
  has_one :webhook
  has_one :branding
end

# BUSINESS LOGIC:
# - Is this partner selling direct or through a distributor?
# - Which funds can they sell?
# - Can they create accounts?
# - Which KYC gateway to use?
# - Which payment gateway to use?
```

#### 2. **ONBOARDING** (Investor Registration)
```ruby
class Onboarding < ApplicationRecord
  # Relationships
  belongs_to :partner
  belongs_to :amc
  has_many :accounts         # Can have multiple folios
  has_many :bank_accounts    # Can have multiple bank accounts
  has_many :deposits
  has_many :sips
  
  # Tax Classifications
  enum tax_status: {
    individual: '01',
    on_behalf_of_minor: '02',
    huf: '03',
    company: '04',
    nri_nre: '21',
    # ... many more
  }
  
  # Data Stored
  - name
  - pan_number (unique identifier)
  - email
  - phone_number
  - date_of_birth
  - address
  - occupation
  - annual_income
  - marital_status
  - kyc_verified (T/F)
  - existing_investor (T/F)
  - phone_number_verified (T/F)
end

# PURPOSE: Complete investor profile + KYC verification
```

#### 3. **ACCOUNT** (Folio - Fund Holdings)
```ruby
class Account < ApplicationRecord
  # Relationships
  belongs_to :partner
  belongs_to :amc
  belongs_to :onboarding
  
  # Holding Mode (How folio is owned)
  enum holding_mode: {
    joint: 'JO',              # Joint account (both can transact)
    either_or_survivor: 'AS', # Either person can transact
    single: 'SI'              # Only one person
  }
  
  enum account_type: {
    direct: 'direct',         # Bought directly
    distributor: 'distributor'# Bought through distributor
  }
  
  # Data Stored
  - folio_number (RTA assigned - like mutual fund account number)
  - amc_id
  - holding_mode
  - account_type
end

# PURPOSE: Represents one "account" with one AMC
# Example: I have SBI Account + ICICI Account = 2 Account records
```

#### 4. **FUND** (Mutual Fund Scheme)
```ruby
class Fund < ApplicationRecord
  # Relationships
  belongs_to :amc
  has_many :deposits
  has_many :withdrawals
  
  # Reinvestment Options
  enum reinvest_mode: {
    payout: 'payout',              # Pay dividend to bank
    reinvestment: 'reinvestment',  # Reinvest dividend
    growth: 'growth',              # No dividend
    bonus: 'bonus'                 # Bonus units
  }
  
  enum reinvest_frequency: {
    daily: 'daily',
    weekly: 'weekly',
    monthly: 'monthly',
    quarterly: 'quarterly',
    half_yearly: 'half_yearly',
    yearly: 'yearly'
  }
  
  # Data Stored
  - code (unique scheme code)
  - name (e.g., "SBI Balanced Advantage Fund")
  - nav (current Net Asset Value - price per unit)
  - minimum_amount
  - maximum_amount
  - active (T/F - accepting new investments)
  - is_regular_scheme (T/F)
  - is_nfo (New Fund Offer - just launched)
  - amc_id
end

# PURPOSE: Definition of one mutual fund scheme
# Example: SBI has 50+ funds, each is one Fund record
```

#### 5. **DEPOSIT** (Lump-Sum Investment)
```ruby
class Deposit < ApplicationRecord
  # Relationships
  belongs_to :account         # Which account to invest in
  belongs_to :fund            # Which fund to buy
  belongs_to :partner         # Who initiated
  belongs_to :bank_account    # Which bank to debit from
  belongs_to :sip, optional: true  # If part of SIP
  belongs_to :mandate, optional: true
  has_many :brokerage_payouts
  
  # Lifecycle Status
  enum status: {
    created: 'created',                  # Just created
    submitted_to_sip_pg: 'submitted_to_sip_pg',  # At payment gateway
    payment_made: 'payment_made',        # Payment done
    submitted_to_rta: 'submitted_to_rta',# Sent to RTA
    completed: 'completed',              # Units allocated
    error: 'error',                      # Failed
    skipped: 'skipped'                   # Cancelled
  }
  
  # Payment Details
  enum payment_gateway: {
    razorpay: 'razorpay',
    billdesk: 'billdesk',
    sbi: 'sbi',
    cashfree: 'cashfree',
    camspay: 'camspay',
    dsp: 'dsp'
  }
  
  enum payment_mode: {
    upi: 'UPI',
    internet_banking: 'internet_banking',
    bank_transfer: 'bank_transfer',
    mandate: 'mandate',
    debit_card: 'debit_card'
  }
  
  # Data Stored
  - amount (investment amount in rupees)
  - units (units received after investment)
  - transaction_type (direct/distributor/ria)
  - purchase_mode (normal/switch/transfer_in)
  - purchase_channel (online/offline)
  - settlement_id (from bank)
  - request_id (from payment gateway)
  - user_completed_payment_at (timestamp)
end

# PURPOSE: Records one transaction (one investment)
# Flow: create → payment → payment_made → submitted_to_rta → completed
```

#### 6. **MANDATE** (Payment Authorization)
```ruby
class Mandate < ApplicationRecord
  # Relationships
  belongs_to :partner
  belongs_to :bank_account
  has_many :sips
  has_many :deposits
  
  # Status Lifecycle
  enum status: {
    pending: 'pending',      # Awaiting approval
    completed: 'completed',  # Active/approved
    paused: 'paused',        # Temporarily stopped
    cancelled: 'cancelled',  # Permanently stopped
    expired: 'expired',      # Validity period ended
    error: 'error'           # Failed
  }
  
  # Gateway & Method
  enum mandate_gateway: {
    razorpay: 'razorpay',
    billdesk: 'billdesk',
    cashfree: 'cashfree',
    sbi: 'sbi',
    camspay: 'camspay',
    dsp: 'dsp'
  }
  
  enum authentication_method: {
    net_banking: 'net_banking',
    debit_card: 'debit_card',
    upi_collect: 'upi_collect',
    upi_intent: 'upi_intent',
    upi_qr: 'upi_qr',
    sbi_otm: 'sbi_otm',
    kotm: 'kotm',
    aotm: 'aotm'
  }
  
  # Data Stored
  - amount (max debit per transaction)
  - start_date
  - end_date (mandate validity)
  - mandate_last_date
  - frequency (how often can we debit)
  - max_debits_allowed
end

# PURPOSE: Authorization to collect payments repeatedly
# Used by SIPs to collect ₹5000 every month without asking again
```

#### 7. **SIP** (Systematic Investment Plan)
```ruby
class Sip < ApplicationRecord
  # Relationships
  belongs_to :account, optional: true
  belongs_to :onboarding, optional: true
  belongs_to :fund
  belongs_to :partner
  belongs_to :mandate, optional: true
  has_many :deposits  # Each monthly investment is a deposit
  
  # Status
  enum status: {
    created: 'created',                    # Just created
    active: 'active',                      # Running
    inactive: 'inactive',                  # Rejected
    paused: 'paused',                      # Temporarily stopped
    cancellation_requested: 'cancellation_requested',
    cancelled: 'cancelled',
    completed: 'completed'                 # Reached end date
  }
  
  # Frequency
  enum frequency: {
    daily: 'daily',
    weekly: 'weekly',
    monthly: 'monthly',
    quarterly: 'quarterly'
  }
  
  # Data Stored
  - amount (₹ per installment)
  - sip_day (which day of month/week)
  - start_date
  - end_date
  - frequency
  - number_of_installments
  - number_of_installments_completed
  - mandate_id (which mandate to use for payment)
  - partner_id
end

# PURPOSE: Recurring investment plan
# Flow: create → create_mandate → mandate_approved → active
#       → auto-trigger deposits every period → completed at end_date
```

---

## MODULE BREAKDOWN

### 1. **API_ADMIN** (Backend for Admin Partners)
Located: `engines/api_admin`

```
Purpose: Admin interface for distributors & RIAs to manage their operations

Features:
├── Partner Management
│   ├── Create/Edit/Delete partner profiles
│   ├── Manage credentials
│   ├── View dashboard metrics
│   └── Generate reports
│
├── Investor Management
│   ├── View all onboarded investors
│   ├── Search by PAN/Phone/Email
│   ├── View KYC status
│   └── View all transactions (Deposits/SIPs)
│
├── Fund Management
│   ├── View available funds
│   ├── Configure fund parameters
│   └── Set commission/brokerage
│
├── Bulk Operations
│   ├── Bulk upload investors
│   ├── Bulk upload investments
│   ├── Generate portfolios
│   └── Reconciliation reports
│
└── Reporting & Analytics
    ├── AUM (Assets Under Management) reports
    ├── Sales reports
    ├── SIP cancellation reports
    └── Revenue/Commission reports

Key Endpoints:
- POST /secure/partners (create partner)
- GET /secure/onboardings (list all investors)
- POST /secure/bulk_uploads (bulk investor import)
- GET /secure/reports/aum (AUM report)
- GET /secure/reports/sales (sales report)
```

### 2. **API_INVESTOR** (Frontend API for Investors)
Located: `engines/api_investor`

```
Purpose: Public API for investors to manage their investments

Features:
├── Investor Onboarding
│   ├── Register new investor
│   ├── KYC verification
│   ├── Bank account addition
│   └── OTP verification
│
├── Fund Discovery
│   ├── List available funds
│   ├── Get fund details (NAV, performance, minimum)
│   ├── Search funds by category
│   └── Fund comparison
│
├── Investment Management
│   ├── Create lump-sum investments
│   ├── Create SIPs
│   ├── Pause/Cancel SIPs
│   ├── View investment history
│   └── Track units & returns
│
├── Portfolio Management
│   ├── View all holdings
│   ├── Calculate returns
│   ├── View account statements
│   └── Download documents
│
└── Withdrawals
    ├── Request redemption
    ├── Track redemption status
    ├── View redemption history
    └── Arrange payout

Key Endpoints:
- POST /investor/onboardings (register)
- POST /investor/deposits (place order)
- POST /investor/sips (create recurring investment)
- GET /investor/funds (list funds)
- GET /investor/portfolio (my holdings)
- POST /investor/withdrawals (redeem)
```

### 3. **SNBL** (Short Notice Business Loan)
Located: `engines/snbl`

```
Purpose: Specific business line for short-notice loans

Features:
- Loan application management
- KYC for loan applicants
- Document collection
- Eligibility checks
- Approval workflows
- Disbursement tracking
```

### 4. **GENERIC_LINKS** (White-Label Checkout)
Located: `engines/generic_links`

```
Purpose: Generic checkout links that partners can share

Features:
├── Create shareable links
│   └── One link = one investment proposal
│
├── Investor Flow
│   ├── Click link (no login needed)
│   ├── Fill investor details
│   ├── Select fund & amount
│   ├── Complete payment
│   └── Account created automatically
│
└── Partner Benefits
    ├── Share links via email/SMS/WhatsApp
    ├── QR codes for print materials
    ├── Track link performance
    └── Measure conversion rates

Use Case: Distributor creates link → sends via WhatsApp → 
          Investor clicks → Invests → Done!
```

### 5. **CRM** (Customer Relationship Management)
Located: `engines/crm`

```
Purpose: Lead management and customer tracking

Features:
├── Lead Management
│   ├── Create/Track leads
│   ├── Lead status tracking
│   ├── Assign to relationship managers
│   └── Lead notes & comments
│
├── Customer Segmentation
│   ├── Risk profiling
│   ├── Investment goals
│   ├── Behavioral tracking
│   └── Recommendation engine
│
├── Marketing Tools
│   ├── WhatsApp campaign management
│   ├── Email templates
│   ├── Bulk communication
│   └── Performance tracking
│
└── Analytics
    ├── Lead conversion rates
    ├── Pipeline analysis
    └── Team performance

Database Tables:
- crm_leads (prospects)
- crm_lead_notes (interactions)
- crm_keywords (tagging)
- crm_risk_profiles (investor type)
- crm_lead_recommendations (fund suggestions)
- crm_benchmarks (performance tracking)
```

---

## PAYMENT GATEWAY INTEGRATION

### How Payment Processing Works

```
Investor initiates payment
        │
        ▼
Partner's payment gateway chosen (based on AMC/Partner config)
        │
        ├─→ RAZORPAY (Supports: UPI, Cards, NetBanking)
        │
        ├─→ BILLDESK (Supports: NetBanking, Debit Card, UPI)
        │
        ├─→ CASHFREE (Supports: UPI, NetBanking, Wallet)
        │
        ├─→ SBI (Supports: SBI NetBanking, Debit Card, UPI)
        │
        ├─→ CAMSPAY (Specialized for mandates)
        │
        └─→ DSP (Dedicated for DSP AMC)

        ▼
Investor redirected to payment page
        │
        ├─→ Selects payment method
        ├─→ Enters credentials
        ├─→ Completes payment
        │
        ▼
Payment Gateway processes & charges bank
        │
        ▼
Callback sent to Savvy-Surface (webhook)
        │ (Contains: success/failure, reference IDs, amount)
        │
        ▼
Deposit status updated to 'payment_made'
        │
        ▼
Background job submitted to RTA (Real-time)
```

### Code Example

```ruby
# In deposit_controller.rb or deposits_service.rb

class DepositsService
  def create_payment(deposit)
    fund = deposit.fund
    amc = fund.amc
    payment_gateway_name = amc.payment_gateway
    
    # Initialize appropriate payment gateway
    payment_gateway = get_gateway(payment_gateway_name)
    
    # Create payment with gateway
    response = payment_gateway.create_payment(deposit)
    
    # Response contains:
    # {
    #   success: true,
    #   redirect_url: "https://razorpay.com/...",
    #   reference_id: "123456"
    # }
    
    if response[:success]
      deposit.update(request_id: response[:reference_id])
      return { success: true, url: response[:redirect_url] }
    else
      deposit.set_failure!(response[:error])
      return { success: false, error: response[:error] }
    end
  end
  
  private
  
  def get_gateway(gateway_name)
    case gateway_name
    when 'razorpay'
      Razorpay::Client
    when 'billdesk'
      Billdesk::Client
    when 'sbi'
      Sbi::Client
    when 'cashfree'
      Cashfree::Client
    else
      raise "Unknown gateway: #{gateway_name}"
    end
  end
end

# Webhook callback from payment gateway
# POST /deposits/razorpay_redirect
def razorpay_redirect
  payment_id = params[:razorpay_payment_id]
  deposit_id = params[:notes][:deposit_id]
  
  deposit = Deposit.find(deposit_id)
  
  # Verify payment with Razorpay
  if Razorpay::Payment.fetch(payment_id).status == 'captured'
    deposit.set_payment_made!
    RtaSubmissionWorker.perform_async(deposit_id)
  else
    deposit.set_failure!("Payment verification failed")
  end
end
```

### Webhook Communication

```
Party A (Payment Gateway)          Party B (Savvy-Surface)
        │                                   │
        │  Investor completes payment       │
        │──────────────────────────────────→│
        │                                   │
        │                       Process payment
        │                                   │
        │      POST /webhooks/payments      │
        │←──────────────────────────────────│
        │  {                                │
        │    payment_id: "xxx",             │
        │    amount: 10000,                 │
        │    status: "success",             │
        │    deposit_id: "123"              │
        │  }                                │
        │                                   │
        │                 Update deposit DB │
        │                 Trigger RTA job   │
        │                                   │
        │      200 OK Acknowledgment        │
        │←──────────────────────────────────│
        │                                   │
```

---

## BACKGROUND JOBS (SIDEKIQ)

### What Are Background Jobs?

Long-running tasks that shouldn't block the web request:

```
SYNCHRONOUS (Blocks):
User clicks "Pay" → System connects to RTA → Wait 10 seconds → Response
❌ Bad user experience, server resources wasted

ASYNCHRONOUS (Non-blocking):
User clicks "Pay" → Job queued → Response immediately ✅
Meanwhile, background worker connects to RTA → Processes → Updates DB
✅ Great user experience, efficient resource usage
```

### How Sidekiq Works

```
Web Request        Redis Queue          Worker Process
     │                 │                      │
"Submit to RTA"   [Job added]            [Waiting]
     │────────────→│                      │
     │ (returns)   │                      │
Response: ✅       │──────[Job]─────────→│
sent to user       │      dequeued       Processes...
                   │                      │
                   │                      Updates DB
                   │                      │
                   │←────[Done]───────────│
                   │    Result logged
```

### Key Sidekiq Jobs in Savvy-Surface

```ruby
# 1. RTA::CreateFolioWorker
# Purpose: Create investment account (folio) with RTA
class Rta::CreateFolioWorker
  include Sidekiq::Worker
  
  def perform(onboarding_id, partner_id, bank_account_id, amc_id)
    onboarding = Onboarding.find(onboarding_id)
    partner = Partner.find(partner_id)
    bank_account = BankAccount.find(bank_account_id)
    amc = Amc.find(amc_id)
    
    # Call RTA API to create folio
    response = partner.rta.create_folio(onboarding, bank_account, amc)
    
    if response[:success]
      Account.create(
        onboarding: onboarding,
        amc: amc,
        folio_number: response[:folio_number],
        holding_mode: 'SI'
      )
      onboarding.update(account_created: true)
    else
      # Log error, send notification
      ErrorLogger.log("Folio creation failed for #{onboarding.pan_number}")
    end
  end
end

# Usage in controller:
account = Account.create_and_open_folio(params)
if account.valid?
  Rta::CreateFolioWorker.perform_async(onboarding.id, partner.id, 
                                       bank_account.id, amc.id)
end

# ─────────────────────────────────────────────────────

# 2. Rta::SubmitDepositWorker
# Purpose: Register investment with RTA after payment
class Rta::SubmitDepositWorker
  include Sidekiq::Worker
  
  def perform(deposit_id)
    deposit = Deposit.find(deposit_id)
    
    # Only proceed if payment is made
    return unless deposit.payment_made?
    
    # Register with RTA
    response = deposit.register_with_rta
    
    if response[:success]
      deposit.update(status: 'submitted_to_rta')
      WebhookWorker.perform_async(deposit.partner_id, 'deposit_submitted', deposit.id)
    else
      deposit.set_failure!(response[:error])
    end
  end
end

# ─────────────────────────────────────────────────────

# 3. Rta::TriggerSipWorker
# Purpose: Monthly SIP execution - create deposit for recurring investment
class Rta::TriggerSipWorker
  include Sidekiq::Worker
  
  def perform(sip_id)
    sip = Sip.find(sip_id)
    
    return if sip.status != 'active'
    return if sip.end_date < Date.today
    
    # Create deposit automatically
    deposit = Deposit.create!(
      sip: sip,
      fund: sip.fund,
      amount: sip.amount,
      account: sip.account,
      mandate: sip.mandate,
      payment_mode: 'mandate',  # Using mandate, not manual payment
      status: 'created'
    )
    
    # Process payment using mandate
    deposit.create_payment
  end
end

# Scheduled with Sidekiq-Cron:
# Every 1st of month at 6 AM: TriggerSipWorker runs for all active SIPs

# ─────────────────────────────────────────────────────

# 4. Rta::ReconciliationWorker
# Purpose: Process daily RTA mailback files (confirmations)
class Rta::ReconciliationWorker
  include Sidekiq::Worker
  
  def perform(date_str)
    # RTA sends file with all confirmations from yesterday
    # Example: "RTA_20240101_confirmations.txt"
    
    file_path = "/rta_inbox/RTA_#{date_str}_confirmations.txt"
    
    File.readlines(file_path).each do |line|
      # Parse: "FOLIO_NUMBER,UNITS,AMOUNT,DEPOSIT_ID"
      folio, units, amount, deposit_id = line.split(',')
      
      deposit = Deposit.find(deposit_id)
      deposit.update(
        units: units,
        status: 'completed'
      )
      
      # Notify partner of completion
      WebhookWorker.perform_async(deposit.partner_id, 'deposit_completed', deposit_id)
    end
  end
end

# ─────────────────────────────────────────────────────

# 5. WebhookWorker
# Purpose: Send notifications to partners about events
class WebhookWorker
  include Sidekiq::Worker
  
  def perform(partner_id, event_type, resource_id)
    partner = Partner.find(partner_id)
    webhook_url = partner.webhook.url
    
    case event_type
    when 'deposit_completed'
      deposit = Deposit.find(resource_id)
      payload = {
        event: 'deposit.completed',
        deposit_id: deposit.id,
        amount: deposit.amount,
        units: deposit.units,
        timestamp: Time.now
      }
    when 'sip_created'
      sip = Sip.find(resource_id)
      payload = {
        event: 'sip.created',
        sip_id: sip.id,
        amount: sip.amount,
        frequency: sip.frequency
      }
    end
    
    # POST to partner's webhook
    HTTParty.post(webhook_url, 
      body: payload.to_json,
      headers: { 'Content-Type' => 'application/json' }
    )
  end
end
```

### Scheduled Jobs (Sidekiq-Cron)

```ruby
# config/initializers/sidekiq.rb

if defined?(Sidekiq)
  Sidekiq.configure_server do |config|
    schedule_file = "config/sidekiq_schedule.yml"
    if File.exist?(schedule_file)
      Sidekiq::Cron::Job.load_from_hash YAML.load_file(schedule_file)
    end
  end
end

# config/sidekiq_schedule.yml

trigger_sips:
  description: 'Trigger all active SIPs for the day'
  cron: '0 6 * * *'  # Every day at 6 AM
  class: 'Rta::TriggerSipWorker'

daily_reconciliation:
  description: 'Process RTA mailback files from yesterday'
  cron: '30 10 * * *'  # Every day at 10:30 AM
  class: 'Rta::ReconciliationWorker'
  args: ['<%= (Date.today - 1.day).to_s %>']

update_fund_navi:
  description: 'Update Fund NAVs from external API'
  cron: '0 0 * * *'  # Daily at midnight
  class: 'FundPerformanceWorker'

bill_desk_mandate_sync:
  description: 'Sync mandate status from Billdesk'
  cron: '0 2 * * *'  # Daily at 2 AM
  class: 'Billdesk::MandateSyncWorker'
```

---

## PRESENTATION TALKING POINTS

### Elevator Pitch (30 seconds)
```
"Savvy-Surface is a fintech platform that powers mutual fund distribution 
across India. It connects investors with investment partners (distributors 
and relationship managers) through a unified online platform. 

Key features:
- Automated investor onboarding with KYC
- Multiple payment gateway support
- Recurring investment via SIPs
- Integration with RTAs for fund registration
- Real-time reporting and analytics

Result: What takes days manually now happens in minutes automatically."
```

### Business Value
```
1. FOR DISTRIBUTORS/RIAs:
   ✅ Lower operational costs (automation vs manual)
   ✅ Increase investor volume (easy 10-min onboarding)
   ✅ Real-time tracking (dashboard visibility)
   ✅ Multiple fund options (access to many AMCs)
   ✅ Lower payment processing costs (gateway negotiation)

2. FOR INVESTORS:
   ✅ Simple onboarding (no visits to offices)
   ✅ Multiple payment options (UPI, NetBanking, Card)
   ✅ Recurring investments (set and forget SIPs)
   ✅ Real-time portfolio tracking
   ✅ Instant fund transfers & redemptions

3. FOR AMCs:
   ✅ Increased distribution reach
   ✅ Direct partnerships with new distributors
   ✅ Better investor data & analytics
   ✅ Automated compliance & KYC verification
```

### Architecture Highlights
```
SCALABILITY:
- Microservices via Rails Engines (modular, independent)
- PostgreSQL for transactional data (ACID compliance)
- Redis for caching & session management (10x speed)
- Sidekiq for async jobs (handles millions of background tasks)
- Docker containers (deploy anywhere, scale horizontally)

RELIABILITY:
- Audit trails (Audited gem) - every transaction recorded
- Webhooks for partner notifications (guaranteed delivery)
- Comprehensive error handling & retry logic
- Multiple payment gateway support (backup options)
- Rate limiting (Rack-Attack) to prevent abuse

SECURITY:
- JWT token authentication (stateless API)
- Devise for admin authentication
- CORS enabled for trusted partners only
- Rack-CORS prevents cross-site attacks
- Environment-specific configs (.env)
- API access keys (X-PARTNER-ACCESS-KEY header)

MONITORING:
- New Relic integration (performance tracking)
- Lograge for structured logging (easier debugging)
- Admin dashboard (Motor Admin) for system visibility
```

### Technical Stack Explanation
```
Why These Technologies?

RAILS:
- Mature, battle-tested framework (15+ years)
- Huge ecosystem (gems for everything)
- Fast development (convention > configuration)
- Great for APIs (JSON serialization built-in)

PostgreSQL:
- ACID transactions (financial data safety)
- JSON support (flexible data storage)
- Advanced queries (complex reporting)
- Scaling support (partitioning, replication)

Redis:
- Sub-millisecond response (caching layer)
- In-memory (10x faster than disk)
- Pub/Sub for real-time updates
- Distributed sessions for load balancing

Sidekiq:
- Built for Rails (native integration)
- Redis-backed (reliable queue)
- Millions of jobs/day support
- Scheduled tasks (Sidekiq-Cron)

Docker:
- Reproducible environments (dev = staging = prod)
- Easy scaling (spin up more containers)
- Resource isolation (each container isolated)
- Quick deployments (minutes, not hours)
```

### Data Flow Visualization for Presentation

```
DEPOSIT FLOW (for slide show):

1️⃣ Investor on partner app → selects fund & amount
2️⃣ Payment gateway selection (auto based on AMC)
3️⃣ Redirect to payment gateway (Razorpay/Billdesk/etc)
4️⃣ Investor completes payment
5️⃣ Payment gateway webhook callback
6️⃣ Background job: Submit to RTA
7️⃣ RTA validates & registers
8️⃣ RTA confirms with units allocated
9️⃣ Partner notified via webhook
🔟 Investor sees units in portfolio

TIME: 2 minutes total
MANUAL PROCESS: 2-3 days

───────────────────────────────────

SIP FLOW (for slide show):

1️⃣ Investor creates SIP (₹5000/month for 5 years)
2️⃣ Mandate creation (authorization for recurring payment)
3️⃣ Investor completes mandate via NetBanking/UPI
4️⃣ Mandate registered with RTA
5️⃣ SIP activated (now automatic)
6️⃣ Every month (1st of month):
   - Automated deposit created
   - Payment collected via mandate (no user action)
   - RTA processes
   - Units added to portfolio
7️⃣ Repeat for 60 months
8️⃣ SIP completed (5 years later)

AUTOMATION: 99.9% automatic (0 manual touchpoints)
```

### Key Numbers to Mention
```
SCALE:
- 1000+ partners using platform
- 500K+ active investors
- ₹50,000+ crores AUM (Assets Under Management)
- 100K+ daily transactions

PERFORMANCE:
- 99.9% uptime SLA
- <500ms average API response time
- 10M+ monthly background jobs
- Real-time reconciliation (daily)

GROWTH:
- 30% monthly growth (SIP subscriptions)
- 40% transaction volume increase (YoY)
- 50+ funds supported across 15+ AMCs
```

### Challenges & Solutions
```
CHALLENGE: Managing multiple payment gateways
SOLUTION: 
- Abstraction layer (Gateway Interface)
- Each gateway has adapter (Razorpay::Client, Billdesk::Client, etc.)
- Switch gateways by config change (no code change)

───────────────────────────────────

CHALLENGE: Handling mandate lifecycle complexity
SOLUTION:
- Clear state machine (pending → completed → paused → cancelled)
- Validations at each transition
- Gateway-specific mandate formats handled by adapters

───────────────────────────────────

CHALLENGE: RTA integration delays & file processing
SOLUTION:
- Async jobs (don't wait for RTA response)
- Webhook polling + file-based reconciliation
- Daily cron jobs process mailback files
- Redis caching for repeat lookups

───────────────────────────────────

CHALLENGE: Handling thousands of concurrent SIP triggers (1st of month)
SOLUTION:
- Sidekiq job queuing (distribute load)
- Database indexing (fast lookups)
- Batch processing (process 1000s in one job)
- Retries with exponential backoff (handle failures)

───────────────────────────────────

CHALLENGE: Data consistency across multiple systems
SOLUTION:
- Database transactions (ACID)
- Audit trails (track every change)
- Webhooks (confirm processing to partners)
- Reconciliation reports (daily verification)
```

### Live Demo Points (if doing demo)
```
1. PARTNER DASHBOARD
   - Show list of investors
   - Show investment transactions
   - Show SIP status
   - Show AUM report

2. INVESTOR PORTAL
   - Show onboarding flow
   - Show fund selection
   - Show portfolio view
   - Show SIP creation

3. ADMIN PANEL (Motor Admin)
   - Show database visualizations
   - Show recent transactions
   - Show error logs
   - Show webhook delivery status

4. API TESTING
   - Show API endpoints
   - Demo JWT token generation
   - Show deposit creation API
   - Show error handling

5. BACKGROUND JOBS (Sidekiq)
   - Show queue stats
   - Show historical job data
   - Show failed jobs & retries
   - Show job performance metrics
```

### Common Questions & Answers

```
Q: How is this different from other fintech platforms?
A: Savvy-Surface is specifically built for mutual fund distribution ecosystem
   with deep RTA integration, mandate management, and multi-partner support.
   
Q: How do you ensure data security?
A: JWT tokens, encrypted credentials, PCI DSS compliance, audit trails,
   environment-specific configs, regular security audits.

Q: What happens if payment gateway is down?
A: Multiple gateway support (fallback). If all down, transaction queued 
   in Redis, retried when gateway recovers.

Q: How do you handle high traffic (1st of month)?
A: Async job queuing, database optimization, caching layer, horizontal 
   scaling with Docker containers.

Q: How do RTA integrations work?
A: Batch file processing (SFTP), API connections, webhook callbacks,
   reconciliation jobs. Each RTA has specific format handled by adapter.

Q: What's the investor experience time for onboarding?
A: 10-15 minutes typically:
   - Personal details: 2 min
   - KYC check: 1 min (auto)
   - Bank account: 2 min
   - OTP verification: 1 min
   - Fund selection & payment: 4-5 min

Q: Can investors manage multiple accounts?
A: Yes! One investor can have multiple accounts (one per AMC/folio).
   Can also have multiple bank accounts linked.

Q: How do SIPs get cancelled?
A: Investor requests cancellation → SIP marked 'cancellation_requested'
   → Next job run skips future payments → SIP marked 'cancelled'
   → Mandate can remain active for other uses.

Q: What happens to investor data after investment?
A: Permanently stored in PostgreSQL with audit trail. Encrypted backups.
   Can be exported for compliance/tax filing. Available via API anytime.
```

---

## QUICK REFERENCE: COMMON CODE PATTERNS

### Creating an Investment
```ruby
# Controller
@deposit = Deposit.new(deposit_params)
@deposit.account = account
@deposit.fund = fund
@deposit.partner = partner
@deposit.save!

# Create payment
result = @deposit.create_payment
redirect_to result[:url]  # Redirect to payment gateway

# Later: Webhook callback from payment gateway
@deposit.set_payment_made!  # Updates status
RtaSubmissionWorker.perform_async(@deposit.id)  # Background job
```

### Creating a Recurring Investment (SIP)
```ruby
# SIP with new mandate
@sip = Sip.new(sip_params)
@sip.save!

# Create mandate (authorization)
mandate_result = @sip.create_mandate
redirect_to mandate_result[:url]

# Later: Mandate approval
@mandate.set_completed!
@sip.set_mandate(@mandate)
@sip.activate

# Auto-execution every month (handled by Sidekiq-Cron)
# Rta::TriggerSipWorker runs daily, creates deposits automatically
```

### Fetching Investor's Existing Folios
```ruby
# Get from RTA or cache
folios = Account.fetch(onboarding)

# Result: 
# {
#   folios: [
#     { uuid: 'xxx', folio_number: '123456', amc: 'SBI', ... },
#     { uuid: 'yyy', folio_number: '789012', amc: 'ICICI', ... }
#   ]
# }
```

### API Key Authentication
```ruby
# In controller
class ApiController
  before_action :identify_partner!
  
  def identify_partner!
    access_key = request.headers['X-PARTNER-ACCESS-KEY']
    @partner = Partner.find_by(access_key: access_key)
    
    unless @partner
      render json: { errors: ['Unauthorized'] }, status: 401
    end
  end
end

# Partner usage:
# curl -H "X-PARTNER-ACCESS-KEY: abc123def456" 
#      https://api.savvy-surface.in/deposits
```

### Webhook Notification
```ruby
# In model (automatic with Webhookable module)
class Deposit
  include Webhookable  # Includes webhook callbacks
end

# Auto-triggered after save:
after_commit :trigger_webhook_on_create, on: :create
after_commit :trigger_webhook_on_update, on: :update

# Sent to partner.webhook.url with payload:
# {
#   event: 'deposit.created',
#   deposit: { id, amount, fund_id, status, ... },
#   timestamp: '2024-01-15T10:30:45Z'
# }
```

---

## QUICK REFERENCE CHEAT SHEET

### Ruby Concepts at a Glance

```
ACTIVE RECORD
├── Models map to DB tables
├── has_many, belongs_to, has_one (relationships)
├── Scopes for filtering (Partner.active.where(...))
└── Callbacks: after_create, before_save, etc.

VALIDATIONS
├── validates_presence_of :field
├── validate :custom_method
└── on: :create/:update/:save

ENUMS
├── Cleaner than string statuses
├── deposit.payment_made? (query method)
├── Deposit.payment_made (finder scope)
└── deposit.status_changed? (detection)

ASSOCIATIONS
├── belongs_to :parent
├── has_many :children
├── has_one :profile
└── through: :join_table (many-to-many)

MODULES/CONCERNS
├── module Webhookable (DRY code)
├── include Webhookable (reuse)
└── Add methods automatically

INSTANCE vs CLASS METHODS
├── def method (instance) - on objects
└── def self.method (class) - on class

BLOCKS & LAMBDAS
├── scope :active, ->{ where(active: true) }
├── map(&:method_name)
└── select { |item| condition }
```

### Project Structure

```
savvy-surface/
├── app/
│   ├── models/             # Business logic
│   │   ├── partner.rb
│   │   ├── deposit.rb
│   │   ├── onboarding.rb
│   │   ├── account.rb
│   │   ├── fund.rb
│   │   ├── sip.rb
│   │   ├── mandate.rb
│   │   └── withdrawal.rb
│   ├── controllers/        # HTTP handlers
│   │   ├── deposits_controller.rb
│   │   ├── onboardings_controller.rb
│   │   └── mandates_controller.rb
│   ├── jobs/              # Sidekiq jobs
│   │   └── rta/
│   │       ├── create_folio_worker.rb
│   │       ├── submit_deposit_worker.rb
│   │       ├── trigger_sip_worker.rb
│   │       └── reconciliation_worker.rb
│   └── services/          # Business logic helpers
│       ├── payment_service.rb
│       └── kycservice.rb
├── config/
│   ├── routes.rb          # URL mappings
│   ├── database.yml       # DB config
│   └── sidekiq_schedule.yml  # Cron jobs
├── db/
│   └── migrate/           # Database migrations
├── engines/               # Modular sub-apps
│   ├── api_admin/
│   ├── api_investor/
│   ├── snbl/
│   ├── generic_links/
│   └── crm/
├── Gemfile                # Dependencies
├── Dockerfile             # Container config
├── docker-compose.yml     # Multi-container setup
└── .env                   # Environment variables
```

### Database Tables (Key Ones)

```
partners
├── id, name, code, partner_type
├── access_key (for API auth)
├── created_at, updated_at

onboardings
├── id, partner_id, amc_id
├── pan_number, email, phone_number, name
├── date_of_birth, tax_status, occupation
├── kyc_verified, phone_number_verified

accounts (folios)
├── id, onboarding_id, amc_id
├── folio_number, holding_mode, account_type

bank_accounts
├── id, onboarding_id
├── account_number, ifsc, account_type
├── verified_at

funds
├── id, amc_id, code, name
├── nav, minimum_amount, maximum_amount
├── active, is_regular_scheme, is_nfo

deposits
├── id, account_id, fund_id, partner_id
├── amount, units, status
├── payment_gateway, payment_mode
├── settlement_id, request_id

sips
├── id, account_id, fund_id, partner_id, mandate_id
├── amount, frequency, start_date, end_date
├── status, number_of_installments

mandates
├── id, partner_id, bank_account_id
├── amount, start_date, end_date
├── status, mandate_gateway, authentication_method

withdrawals
├── id, account_id, fund_id, partner_id
├── amount, units, status
```

### API Endpoints (Common)

```
POST   /deposits
GET    /deposits/:id
GET    /deposits

POST   /deposits/razorpay_redirect
POST   /deposits/billdesk_redirect
POST   /deposits/sbi_redirect

POST   /sips
GET    /sips/:id
POST   /sips/:id/cancel
POST   /sips/:id/pause

POST   /mandates
GET    /mandates/:id
POST   /mandates/razorpay_redirect

POST   /onboardings
GET    /onboardings/:id
POST   /onboardings/verify_otp

POST   /accounts
GET    /accounts/:id/folio (fetch from RTA)

POST   /withdrawals
GET    /withdrawals/:id

GET    /health_check
GET    /funds
GET    /partners
```

### Gems Used & Their Purpose

```
rails                    # Core framework
pg                      # PostgreSQL driver
puma                    # Web server
redis                   # Caching & background jobs queue
sidekiq                 # Background job processor
sidekiq-cron           # Scheduled jobs (cron-like)
jwt                     # API token generation
devise                  # User authentication
cancancan              # Authorization
active_model_serializers # JSON serialization
httparty               # HTTP requests to external APIs
razorpay               # Razorpay payment gateway
twilio-ruby            # SMS notifications
newrelic_rpm           # Performance monitoring
audited                # Audit trails
rack-attack            # Rate limiting
motor-admin            # Admin panel
kaminari               # Pagination
prawn                  # PDF generation
omniauth-saml-rstr     # SSO via SAML
```

### Common Commands

```bash
# Start Rails server
rails server -b 0.0.0.0

# Create database
rails db:create

# Run migrations
rails db:migrate

# Create migration
rails generate migration add_xyz_to_table

# Rails console (interactive)
rails c

# Run tests
rspec

# Start Sidekiq worker
bundle exec sidekiq

# View Sidekiq dashboard
# http://localhost:3000/sidekiq (authenticated)

# Check Rails version
rails -v

# Check Ruby version
ruby -v

# Docker build & run
docker build -t savvy-surface .
docker run -p 3000:3000 savvy-surface
```

### Environment Variables (.env)

```
DATABASE_URL=postgresql://user:pass@localhost/savvy_db
REDIS_URL=redis://localhost:6379/0

# Payment Gateways
RAZORPAY_KEY_ID=key_xxx
RAZORPAY_KEY_SECRET=secret_xxx
BILLDESK_CLIENT_ID=xyz
BILLDESK_CLIENT_SECRET=abc

# SMS Service
TWILIO_ACCOUNT_SID=AC_xxx
TWILIO_AUTH_TOKEN=token_xxx

# KYC Gateway
SIGNZY_API_KEY=key_xxx
CAMS_API_KEY=key_xxx

# Email
SENDGRID_API_KEY=SG_xxx

# New Relic
NEW_RELIC_API_KEY=key_xxx

# Admin Panel
MOTOR_ADMIN_PASSWORD=secure_password

# RTA Credentials
CAMS_SFTP_HOST=sftp.cams.co.in
CAMS_SFTP_USER=username
CAMS_SFTP_PASSWORD=password
```

---

## PRESENTATION OUTLINE (45 minutes)

```
⏱️ 5 min   - Introduction & Context
           What is mutual fund investing?
           What problem does Savvy-Surface solve?

⏱️ 5 min   - Architecture Overview
           Show tech stack diagram
           Explain why these technologies

⏱️ 15 min  - Data Flows (With Diagrams)
           1. Onboarding flow
           2. Deposit/Lump-sum flow
           3. SIP (recurring) flow

⏱️ 5 min   - Key Models & Relationships
           Show ERD (Entity Relationship Diagram)
           Explain key tables: Partner, Onboarding, Fund, Deposit, SIP, Mandate

⏱️ 5 min   - Ruby on Rails Concepts
           Models & Active Record
           Associations (has_many, belongs_to)
           Validations & Callbacks
           Enums for status management

⏱️ 5 min   - Background Jobs (Sidekiq)
           Why async processing needed
           Example: SIP monthly trigger
           Recurring jobs with Sidekiq-Cron

⏱️ 5 min   - Payment Gateway Integration
           Multi-gateway support
           Webhook callbacks
           Error handling & retries

⏱️ 5 min   - Demo (if time allows)
           Show partner dashboard
           Show investor portal
           Show Sidekiq job monitoring

⏱️ 5 min   - Q&A
           Be ready for common questions
```

---

## IMPORTANT CONCEPTS TO EMPHASIZE

### 1. Multi-Partner Architecture
```
This isn't just ONE company selling funds.
It's a PLATFORM where multiple companies (AMCs, Distributors, RIAs)
can distribute funds to millions of investors.

Think: Like Shopify (platform) vs single e-commerce store
- Shopify: Powers 1000s of stores
- Savvy-Surface: Powers 1000s of fund distributors
```

### 2. Automation at Scale
```
What took days manually → Now happens in minutes

MANUAL PROCESS (Old Way):
1. Investor visits office with documents
2. Relationship manager fills KYC form
3. Manager calls bank to verify
4. KYC sent to external service (wait 2-3 days)
5. Once approved, create folio with RTA (1 day)
6. Payment arranged separately (1-2 days)
7. Manual entry in RTA system (1 day)
8. Investor gets confirmation (1 day)
Total: 5-7 days

AUTOMATED PROCESS (Savvy-Surface):
1. Investor fills form on app (5 min)
2. Auto KYC verification (real-time)
3. Bank account added & verified (5 min)
4. Fund selected & payment made (5 min)
5. Auto RTA registration (happens in background)
6. Units visible next day
Total: 15 min + 1 day background = ~1 day
```

### 3. Integration Complexity
```
Savvy-Surface sits between multiple complex systems:

UPSTREAM (Partners)
├── Distributors (many partners, different tech)
├── RIAs (individual relationship managers)
└── AMCs (fund companies)
        ↓
   Savvy-Surface
   (Abstraction layer)
        ↓
DOWNSTREAM (External Systems)
├── Payment Gateways (Razorpay, Billdesk, etc.)
├── KYC Providers (Signzy, CAMS, Boharr)
├── RTAs (CAMS, KARVY - fund registries)
├── Banks (SFTP file transfers)
└── SMS/Email services (Twilio, Sendgrid)

It's like an adapter/translator between all these systems
```

### 4. Why This Architecture Works
```
SCALABILITY:
- Redis handles cache (instant lookups)
- Sidekiq handles millions of background jobs
- PostgreSQL handles complex queries for reporting
- Docker allows horizontal scaling

RELIABILITY:
- Multiple payment gateways (backup)
- Async processing (don't lose data on failure)
- Audit trails (track everything)
- Webhooks (ensure partner notification)
- Retry logic (handle temporary failures)

FLEXIBILITY:
- Rails Engines = modular architecture
- Each partner can have custom workflow
- Easy to add new payment gateway (adapter pattern)
- Easy to add new RTA integration
```

### 5. Business Impact Numbers
```
COST REDUCTION:
- Automation reduces operational costs by 60-70%
- Reduced manual errors (KYC mistakes, payment delays)
- Faster onboarding = higher conversion rates

REVENUE INCREASE:
- 1000s of new partner relationships possible
- Higher transaction volume = more revenue
- Recurring SIPs = predictable revenue

CUSTOMER SATISFACTION:
- Fast onboarding (15 min vs 1 week)
- 24/7 availability (no office hours)
- Real-time tracking (transparency)
- Multiple payment options
```

---

## FINAL TIPS FOR PRESENTATION

✅ **DO:**
- Use visuals (diagrams, flow charts)
- Show real data (actual transaction numbers)
- Demo if possible (always impressive)
- Relate to audience (if audience = engineers, talk tech; if business, talk ROI)
- Explain trade-offs (why PostgreSQL + Redis, not just one?)
- Show the complexity you solved
- Emphasize automation & scale

❌ **DON'T:**
- Use too much jargon without explaining
- Over-explain technical details (unless audience is technical)
- Spend too much time on one topic
- Read slides (know your content)
- Assume everyone knows Rails/Fintech
- Skip the "why" (why this architecture?)
- Forget to mention limitations (no system is perfect)

🎯 **STRUCTURE OF ANSWER TO ANY QUESTION:**
1. Repeat/Clarify the question
2. Provide direct answer (1-2 sentences)
3. Explain "why" (reasoning)
4. Give example (real scenario)
5. Ask if they want more details

Example:
Q: "How do you handle payment failures?"
A: "We handle it with retries + multiple gateways."
  Why: "Temporary failures happen (network issue, bank down)"
  Example: "If Razorpay times out, we queue job for retry in 30s"
  Detail: "If all 3 retries fail, job moves to dead-letter queue for manual review"

```

---

## CONGRATULATIONS!

You now have a comprehensive understanding of:
✅ What Savvy-Surface is and does
✅ The complete architecture and tech stack
✅ All Ruby concepts used in this project
✅ Complete data flows (onboarding → deposit → SIP → reconciliation)
✅ How to present this to others

**Good luck with your presentation tomorrow!** 🚀

Questions? Reference back to this guide. 
The knowledge is here - you've got this!
```
