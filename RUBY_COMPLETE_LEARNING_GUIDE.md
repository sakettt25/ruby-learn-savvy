# COMPLETE RUBY PROGRAMMING GUIDE: ZERO TO ADVANCED

**Duration**: 4-6 weeks (studying 2-3 hours daily)
**Level**: Beginner → Intermediate → Advanced
**Prerequisites**: Basic programming concepts helpful but not required

---

## TABLE OF CONTENTS

1. [Getting Started](#getting-started)
2. [Phase 1: Ruby Fundamentals (Days 1-5)](#phase-1-ruby-fundamentals)
3. [Phase 2: Object-Oriented Programming (Days 6-12)](#phase-2-object-oriented-programming)
4. [Phase 3: Advanced Ruby Features (Days 13-20)](#phase-3-advanced-ruby-features)
5. [Phase 4: Functional Programming & Metaprogramming (Days 21-28)](#phase-4-functional-programming)
6. [Phase 5: Ruby on Rails Basics (Days 29-42)](#phase-5-ruby-on-rails)
7. [Practice Projects](#practice-projects)
8. [Advanced Topics](#advanced-topics)

---

## GETTING STARTED

### Installation

**macOS (you're on this):**
```bash
# Install Ruby using Homebrew
brew install ruby

# Check version
ruby -v

# Install gems
gem install bundler
```

**Verify Installation:**
```bash
ruby -v          # Should show Ruby version
irb              # Interactive Ruby console
# Type: puts "Hello, Ruby!"
# Exit: exit or Ctrl+D
```

### Your First Ruby Program

```bash
# Create a file
touch hello.rb

# Edit it with your editor
```

```ruby
# hello.rb
puts "Hello, Ruby!"
puts "Welcome to programming!"

name = "Saket"
puts "My name is #{name}"
```

**Run it:**
```bash
ruby hello.rb
```

**Output:**
```
Hello, Ruby!
Welcome to programming!
My name is Saket
```

### Interactive Ruby (IRB)

```bash
irb
```

In IRB, you can test code immediately:
```ruby
irb(main):001:0> puts "Hello"
Hello
=> nil

irb(main):002:0> 5 + 3
=> 8

irb(main):003:0> name = "Ruby"
=> "Ruby"

irb(main):004:0> name.upcase
=> "RUBY"

irb(main):005:0> exit
```

---

## PHASE 1: RUBY FUNDAMENTALS (Days 1-5)

### Day 1: Variables, Data Types, and Basic Operations

#### Variables
```ruby
# Variables hold data
name = "Alice"
age = 25
height = 5.8
is_student = true

puts name      # Alice
puts age       # 25
puts height    # 5.8
puts is_student # true
```

#### Data Types

**Strings** (text):
```ruby
# Single quotes (literal)
greeting1 = 'Hello'

# Double quotes (interpolation)
greeting2 = "Hello #{name}"  # Interpolation!

# Multi-line strings
poem = "Roses are red
Violets are blue
Ruby is fun"

# String methods
str = "hello"
puts str.upcase           # HELLO
puts str.capitalize       # Hello
puts str.reverse          # olleh
puts str.length           # 5
puts str.include?("ell")  # true
```

**Numbers**:
```ruby
# Integers
a = 10
b = -5
c = 0

# Floats (decimals)
x = 3.14
y = 2.5

# Basic arithmetic
puts 10 + 5        # 15
puts 10 - 5        # 5
puts 10 * 5        # 50
puts 10 / 5        # 2
puts 10 % 3        # 1 (remainder/modulo)
puts 2 ** 3        # 8 (exponent)

# Division - be careful!
puts 10 / 3        # 3 (integer division)
puts 10.0 / 3      # 3.333... (float division)

# Number methods
num = 10
puts num.even?     # true
puts num.odd?      # false
puts num.abs       # 10
puts (-5).abs      # 5
```

**Booleans** (true/false):
```ruby
is_active = true
is_deleted = false

# Boolean methods
puts true.class    # TrueClass
puts false.class   # FalseClass

# Truthy vs Falsy
# In Ruby: only 'false' and 'nil' are falsy
# Everything else is truthy!
puts 0 ? "truthy" : "falsy"        # truthy (even 0!)
puts "" ? "truthy" : "falsy"       # truthy (even empty string!)
puts nil ? "truthy" : "falsy"      # falsy
puts false ? "truthy" : "falsy"    # falsy
```

**Nil** (nothing):
```ruby
value = nil
puts value          # (nothing printed)
puts value.class    # NilClass
puts value.nil?     # true

# Nil coalescing
name = nil
display_name = name || "Anonymous"
puts display_name   # Anonymous
```

#### Type Conversion
```ruby
# String to number
str = "25"
num = str.to_i       # 25 (integer)
num_f = str.to_f     # 25.0 (float)

# Number to string
num = 42
str = num.to_s       # "42"

# To boolean (no .to_b in Ruby!)
value = 1
is_true = value != 0 # Use comparison

# Converting between types
puts "10".to_i + 5       # 15
puts "3.14".to_f * 2     # 6.28
puts (100).to_s + "x"    # "100x"
```

#### Practice Exercise 1
```ruby
# Create a program that:
# 1. Stores your name, age, and height
# 2. Calculates your birth year (use current year - age)
# 3. Prints formatted output

name = "Your Name"
age = 25
height = 5.8
current_year = 2024

birth_year = current_year - age

puts "Name: #{name}"
puts "Age: #{age} years old"
puts "Height: #{height} feet"
puts "Birth year (approximately): #{birth_year}"
```

---

### Day 2: Control Flow (If/Else/Case)

#### If Statements

**Basic If:**
```ruby
age = 18

if age >= 18
  puts "You are an adult"
end
```

**If/Else:**
```ruby
temperature = 20

if temperature > 25
  puts "It's hot"
else
  puts "It's cool"
end
```

**If/Elsif/Else:**
```ruby
score = 75

if score >= 90
  puts "Grade A"
elsif score >= 80
  puts "Grade B"
elsif score >= 70
  puts "Grade C"
else
  puts "Grade F"
end
```

**Ternary Operator** (one-line if/else):
```ruby
age = 20
status = age >= 18 ? "adult" : "minor"
puts status  # adult

# More readable multi-line
can_vote = age >= 18 ? "Yes" : "No"
puts can_vote
```

#### Comparison Operators
```ruby
a = 10
b = 20

puts a == b   # false (equals)
puts a != b   # true (not equals)
puts a > b    # false (greater than)
puts a < b    # true (less than)
puts a >= b   # false (greater or equal)
puts a <= b   # true (less or equal)

# String comparison
puts "apple" == "apple"   # true
puts "apple" < "banana"   # true (alphabetical)
```

#### Logical Operators
```ruby
age = 25
income = 50000

# AND (&&)
if age > 18 && income > 30000
  puts "Eligible for loan"  # Will print
end

# OR (||)
has_license = true
has_passport = false

if has_license || has_passport
  puts "Can travel"  # Will print
end

# NOT (!)
is_raining = false

if !is_raining
  puts "Let's go out"  # Will print
end

# Alternative: not (less common)
if not is_raining
  puts "Let's go out"
end
```

#### Unless (opposite of if)
```ruby
is_raining = false

unless is_raining
  puts "Let's go outside"  # Will print
end

# Unless/else
status = "admin"

unless status == "admin"
  puts "Access denied"
else
  puts "Welcome admin"  # Will print
end
```

#### Case/When
```ruby
grade = "B"

case grade
when "A"
  puts "Excellent!"
when "B"
  puts "Good!"
when "C"
  puts "Average"
when "D"
  puts "Poor"
else
  puts "Invalid grade"
end

# Output: Good!

# Case with ranges
score = 85

case score
when 90..100
  puts "A"
when 80..89
  puts "B"
when 70..79
  puts "C"
else
  puts "F"
end

# Output: B

# Case with multiple values
day = "Saturday"

case day
when "Saturday", "Sunday"
  puts "Weekend!"
when "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"
  puts "Weekday"
else
  puts "Invalid day"
end

# Output: Weekend!
```

#### Inline If/Unless
```ruby
# These are called modifiers
puts "Hello" if true          # Prints "Hello"
puts "Hello" unless false     # Prints "Hello"

age = 16
puts "Can vote" if age >= 18  # Doesn't print

# More practical example
user_name = nil
display = user_name || "Guest"
puts "Welcome #{display}" if display  # Welcome Guest
```

#### Practice Exercise 2
```ruby
# Create a program that grades a test score (0-100)
# A: 90-100, B: 80-89, C: 70-79, D: 60-69, F: below 60

score = 85

if score >= 90
  grade = "A"
elsif score >= 80
  grade = "B"
elsif score >= 70
  grade = "C"
elsif score >= 60
  grade = "D"
else
  grade = "F"
end

puts "Score: #{score}, Grade: #{grade}"

# Bonus: Add feedback
feedback = case grade
           when "A" then "Excellent work!"
           when "B" then "Good job!"
           when "C" then "Satisfactory"
           when "D" then "Could be better"
           when "F" then "Need improvement"
           end

puts feedback
```

---

### Day 3: Loops and Iteration

#### While Loop
```ruby
counter = 1

while counter <= 5
  puts "Count: #{counter}"
  counter = counter + 1  # Or: counter += 1
end

# Output:
# Count: 1
# Count: 2
# Count: 3
# Count: 4
# Count: 5

# Until (opposite of while)
counter = 1

until counter > 5
  puts "Count: #{counter}"
  counter += 1
end

# Same output as above
```

#### For Loop
```ruby
# Iterate over a range
for i in 1..5
  puts "Number: #{i}"
end

# Iterate over an array
fruits = ["apple", "banana", "orange"]
for fruit in fruits
  puts fruit
end
```

#### Each (most Ruby way)
```ruby
# Arrays
numbers = [1, 2, 3, 4, 5]

numbers.each do |num|
  puts num
end

# With index
numbers.each_with_index do |num, index|
  puts "Index #{index}: #{num}"
end

# Hashes
person = {name: "Alice", age: 25, city: "NYC"}

person.each do |key, value|
  puts "#{key}: #{value}"
end
```

#### Times
```ruby
# Repeat 5 times
5.times do |i|
  puts "Iteration #{i}"
end

# Output:
# Iteration 0
# Iteration 1
# Iteration 2
# Iteration 3
# Iteration 4

# Without needing index
3.times do
  puts "Hello!"
end

# Output:
# Hello!
# Hello!
# Hello!
```

#### Break and Next
```ruby
# Break - exit loop
(1..10).each do |i|
  if i == 5
    break  # Exit the loop
  end
  puts i
end

# Output: 1, 2, 3, 4

# Next - skip to next iteration
(1..5).each do |i|
  if i == 3
    next  # Skip this iteration
  end
  puts i
end

# Output: 1, 2, 4, 5

# Return - exit method
def find_number
  (1..10).each do |i|
    if i == 5
      return i
    end
  end
end

puts find_number  # 5
```

#### Useful Iterator Methods

**Map** (transform each element):
```ruby
numbers = [1, 2, 3, 4, 5]

# Traditional way
new_numbers = []
numbers.each do |num|
  new_numbers << num * 2
end
puts new_numbers.inspect  # [2, 4, 6, 8, 10]

# Using map (cleaner)
doubled = numbers.map { |num| num * 2 }
puts doubled.inspect  # [2, 4, 6, 8, 10]
```

**Select** (filter elements):
```ruby
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Get only even numbers
even_numbers = numbers.select { |num| num.even? }
puts even_numbers.inspect  # [2, 4, 6, 8, 10]

# Get numbers > 5
greater_than_5 = numbers.select { |num| num > 5 }
puts greater_than_5.inspect  # [6, 7, 8, 9, 10]
```

**Reject** (opposite of select):
```ruby
numbers = [1, 2, 3, 4, 5, 6]

# Remove even numbers
odd_numbers = numbers.reject { |num| num.even? }
puts odd_numbers.inspect  # [1, 3, 5]
```

**Reduce/Inject** (combine elements):
```ruby
numbers = [1, 2, 3, 4, 5]

# Sum all numbers
sum = numbers.reduce(0) { |accumulator, num| accumulator + num }
puts sum  # 15

# Or shorter: use :+
sum = numbers.inject(:+)
puts sum  # 15

# Multiply all
product = numbers.reduce(1) { |acc, num| acc * num }
puts product  # 120
```

#### Practice Exercise 3
```ruby
# Create a program that:
# 1. Loops through numbers 1-10
# 2. Prints only odd numbers
# 3. Stops when it reaches 7

(1..10).each do |i|
  if i == 7
    break
  end
  
  if i.odd?
    puts i
  end
end

# Alternative using iterators
numbers = (1..10).to_a
odd_numbers = numbers.select { |n| n.odd? }
puts odd_numbers.inspect  # [1, 3, 5, 7, 9]
```

---

### Day 4: Arrays and Hashes

#### Arrays (ordered collections)

**Creating Arrays:**
```ruby
# Empty array
empty = []

# Array with elements
fruits = ["apple", "banana", "orange"]

# Array with different types
mixed = [1, "hello", 3.14, true, nil]

# Array with range
numbers = (1..10).to_a
puts numbers.inspect  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Array constructor
letters = Array.new(5, "a")
puts letters.inspect  # ["a", "a", "a", "a", "a"]
```

**Accessing Elements:**
```ruby
fruits = ["apple", "banana", "orange", "grape"]

puts fruits[0]       # apple (first element)
puts fruits[1]       # banana
puts fruits[-1]      # grape (last element)
puts fruits[-2]      # orange (second to last)

# Range of elements
puts fruits[0..2].inspect       # ["apple", "banana", "orange"]
puts fruits[1...3].inspect      # ["banana", "orange"] (... excludes end)

# First and last
puts fruits.first    # apple
puts fruits.last     # grape
```

**Modifying Arrays:**
```ruby
fruits = ["apple", "banana"]

# Add elements
fruits << "orange"           # Add to end
fruits.push("grape")         # Same as <<
fruits.unshift("mango")      # Add to beginning
puts fruits.inspect          # ["mango", "apple", "banana", "orange", "grape"]

# Remove elements
fruits.pop                   # Remove from end ("grape")
fruits.shift                 # Remove from beginning ("mango")
fruits.delete("banana")      # Delete specific element
puts fruits.inspect          # ["apple", "orange"]

# Replace element
fruits[0] = "pineapple"
puts fruits.inspect          # ["pineapple", "orange"]
```

**Array Methods:**
```ruby
numbers = [1, 2, 3, 4, 5, 3, 2, 1]

puts numbers.length          # 8
puts numbers.size            # 8
puts numbers.empty?          # false
puts numbers.include?(3)     # true
puts numbers.index(3)        # 2 (first occurrence)
puts numbers.count(3)        # 2 (how many 3s)

# Unique elements
unique = numbers.uniq
puts unique.inspect          # [1, 2, 3, 4, 5]

# Reverse
puts numbers.reverse.inspect # [1, 2, 3, 5, 4, 3, 2, 1]

# Sort
puts numbers.sort.inspect    # [1, 1, 2, 2, 3, 3, 4, 5]

# Join into string
puts numbers.join(", ")      # 1, 2, 3, 4, 5, 3, 2, 1

# Sum and other operations
puts numbers.sum             # 21
puts numbers.max             # 5
puts numbers.min             # 1
```

**Combining Arrays:**
```ruby
arr1 = [1, 2, 3]
arr2 = [4, 5, 6]

# Concatenate
combined = arr1 + arr2
puts combined.inspect  # [1, 2, 3, 4, 5, 6]

# Flatten nested arrays
nested = [1, [2, 3], [4, [5, 6]]]
flat = nested.flatten
puts flat.inspect      # [1, 2, 3, 4, 5, 6]
```

#### Hashes (key-value pairs)

**Creating Hashes:**
```ruby
# Empty hash
empty = {}

# Hash with elements (old style)
person_old = { :name => "Alice", :age => 25, :city => "NYC" }

# Hash with elements (new style - preferred)
person = { name: "Alice", age: 25, city: "NYC" }

# Hash with string keys
data = { "key1" => "value1", "key2" => "value2" }

# Hash constructor
hash = Hash.new
hash[:a] = 1
hash[:b] = 2
```

**Accessing Hash Values:**
```ruby
person = { name: "Alice", age: 25, city: "NYC" }

puts person[:name]           # Alice
puts person[:age]            # 25
puts person[:country]        # nil (doesn't exist)

# Default value
person_with_default = Hash.new("Unknown")
puts person_with_default[:phone]  # Unknown

# Check if key exists
puts person.key?(:name)      # true
puts person.has_key?(:email) # false
puts person.include?(:age)   # true
```

**Modifying Hashes:**
```ruby
person = { name: "Alice", age: 25 }

# Add or update
person[:age] = 26
person[:city] = "NYC"
puts person.inspect
# {:name=>"Alice", :age=>26, :city=>"NYC"}

# Delete
person.delete(:city)
puts person.inspect          # {:name=>"Alice", :age=>26}

# Merge
additional = { job: "Engineer", country: "USA" }
merged = person.merge(additional)
puts merged.inspect
# {:name=>"Alice", :age=>26, :job=>"Engineer", :country=>"USA"}
```

**Hash Methods:**
```ruby
person = { name: "Alice", age: 25, city: "NYC" }

puts person.length           # 3
puts person.size             # 3
puts person.empty?           # false

puts person.keys.inspect     # [:name, :age, :city]
puts person.values.inspect   # ["Alice", 25, "NYC"]

# Iterate
person.each do |key, value|
  puts "#{key}: #{value}"
end

# Select (filter)
adult = { name: "Alice", age: 25, city: "NYC" }
filtered = adult.select { |key, value| key != :city }
puts filtered.inspect        # {:name=>"Alice", :age=>25}

# Map (transform)
doubled_ages = adult.map { |key, value| value.is_a?(Integer) ? value * 2 : value }
puts doubled_ages.inspect    # ["Alice", 50, "NYC"]
```

#### Nested Collections
```ruby
# Array of hashes (very common!)
users = [
  { name: "Alice", age: 25, email: "alice@example.com" },
  { name: "Bob", age: 30, email: "bob@example.com" },
  { name: "Charlie", age: 35, email: "charlie@example.com" }
]

# Access nested data
puts users[0][:name]         # Alice
puts users[1][:email]        # bob@example.com

# Iterate and access
users.each do |user|
  puts "#{user[:name]} is #{user[:age]} years old"
end

# Hash with array values
departments = {
  engineering: ["Alice", "Bob", "Charlie"],
  sales: ["David", "Emma"],
  hr: ["Frank"]
}

puts departments[:engineering][0]  # Alice
puts departments[:sales].length    # 2
```

#### Practice Exercise 4
```ruby
# Create a program that:
# 1. Stores a list of students with their grades
# 2. Calculates average grade
# 3. Finds students who passed (>= 70)
# 4. Prints results

students = [
  { name: "Alice", grade: 85 },
  { name: "Bob", grade: 92 },
  { name: "Charlie", grade: 68 },
  { name: "David", grade: 78 }
]

# Calculate average
grades = students.map { |student| student[:grade] }
average = grades.sum.to_f / grades.length
puts "Average grade: #{average.round(2)}"

# Find students who passed
passed = students.select { |student| student[:grade] >= 70 }
puts "\nStudents who passed:"
passed.each { |student| puts "#{student[:name]}: #{student[:grade]}" }

# Find top student
top_student = students.max_by { |student| student[:grade] }
puts "\nTop student: #{top_student[:name]} with #{top_student[:grade]}"
```

---

### Day 5: Strings and Methods Introduction

#### String Operations
```ruby
# String concatenation
first = "Hello"
second = "World"

greeting = first + " " + second
puts greeting               # Hello World

# String interpolation (preferred)
name = "Alice"
age = 25
message = "My name is #{name} and I am #{age} years old"
puts message

# String methods
text = "Hello World Ruby"

puts text.length           # 18
puts text.upcase           # HELLO WORLD RUBY
puts text.downcase         # hello world ruby
puts text.capitalize       # Hello world ruby
puts text.reverse          # ybuR dlroW olleH

# Checking strings
puts text.include?("World")      # true
puts text.start_with?("Hello")   # true
puts text.end_with?("Ruby")      # true

# Splitting and joining
words = text.split(" ")
puts words.inspect         # ["Hello", "World", "Ruby"]
puts words.join("-")       # Hello-World-Ruby

# Trimming whitespace
messy = "  hello world  "
puts messy.strip           # "hello world"
puts messy.lstrip          # "hello world  "
puts messy.rstrip          # "  hello world"

# Replacing
text2 = "Hello Hello Hello"
puts text2.replace("Hello", "Hi")  # Hi Hi Hi

# Substring
text3 = "Hello"
puts text3[0]              # H
puts text3[1..3]           # ell
puts text3[-1]             # o
```

#### Introduction to Methods

**Defining Methods:**
```ruby
# Basic method
def greet
  puts "Hello!"
end

greet  # Calling the method

# Method with parameter
def greet_person(name)
  puts "Hello, #{name}!"
end

greet_person("Alice")      # Hello, Alice!

# Method with default parameter
def greet_with_title(name, title = "Friend")
  puts "Hello, #{title} #{name}!"
end

greet_with_title("Bob")                 # Hello, Friend Bob!
greet_with_title("Dr. Alice", "Doctor") # Hello, Doctor Alice!

# Method with return value
def add(a, b)
  a + b  # Last line is returned (no return keyword needed)
end

result = add(5, 3)
puts result  # 8

# Method with explicit return
def subtract(a, b)
  return a - b
end

puts subtract(10, 3)  # 7

# Multiple parameters
def describe_person(name, age, city)
  "#{name} is #{age} years old and lives in #{city}"
end

puts describe_person("Charlie", 30, "LA")
# Charlie is 30 years old and lives in LA

# Method with variable arguments
def print_items(*items)
  items.each { |item| puts item }
end

print_items("apple", "banana", "orange")
# apple
# banana
# orange
```

**Method Naming Conventions:**
```ruby
# Methods that ask a question (return boolean)
def is_adult?(age)
  age >= 18
end

puts is_adult?(25)  # true

# Actually, Ruby style is different:
def adult?(age)    # drop the "is_"
  age >= 18
end

# Methods that perform actions
def send_email(address)
  # send email logic
  puts "Email sent to #{address}"
end

# Method names are lowercase with underscores
def calculate_total_price(price, tax_rate)
  price * (1 + tax_rate)
end
```

**Duck Typing (Ruby Philosophy):**
```ruby
# If it quacks like a duck, it's a duck
def print_length(object)
  puts object.length  # Works for any object with .length method
end

print_length("hello")     # 5
print_length([1, 2, 3])   # 3
print_length({a: 1, b: 2}) # 2

# If it responds to a method, use it
def process(data)
  if data.respond_to?(:each)
    data.each { |item| puts item }
  else
    puts data
  end
end

process([1, 2, 3])    # prints 1, 2, 3
process("hello")      # prints hello
```

#### Practice Exercise 5
```ruby
# Create methods that:
# 1. Convert temperature from Celsius to Fahrenheit
# 2. Check if a number is prime
# 3. Reverse and capitalize a sentence

def celsius_to_fahrenheit(celsius)
  (celsius * 9/5.0) + 32
end

puts celsius_to_fahrenheit(0)    # 32.0
puts celsius_to_fahrenheit(100)  # 212.0

# Method to check if prime
def is_prime?(n)
  return false if n < 2
  (2...n).each { |i| return false if n % i == 0 }
  true
end

puts is_prime?(7)   # true
puts is_prime?(10)  # false

# Reverse and capitalize sentence
def process_sentence(sentence)
  reversed = sentence.reverse
  reversed.capitalize
end

puts process_sentence("hello world")  # Dlrow olleh
```

---

## PHASE 2: OBJECT-ORIENTED PROGRAMMING (Days 6-12)

### Day 6: Classes and Objects

#### Creating Classes

**Basic Class:**
```ruby
# Define a class
class Person
  # Initialize - called when object is created
  def initialize(name, age)
    @name = name   # Instance variable (@ prefix)
    @age = age
  end

  # Instance method
  def greet
    puts "Hello, I'm #{@name} and I'm #{@age} years old"
  end
end

# Create an object (instance)
person1 = Person.new("Alice", 25)
person1.greet  # Hello, I'm Alice and I'm 25 years old

person2 = Person.new("Bob", 30)
person2.greet  # Hello, I'm Bob and I'm 30 years old
```

**Instance Variables vs Local Variables:**
```ruby
class Dog
  def initialize(name)
    @name = name      # Instance variable - persists
    bark_sound = "Woof"  # Local variable - exists only in this method
  end

  def introduce
    puts "My name is #{@name}"  # Can use instance variable
    # puts bark_sound  # ERROR - local variable doesn't exist here
  end
end

dog = Dog.new("Max")
dog.introduce  # My name is Max
```

#### Getters and Setters

**Manual approach:**
```ruby
class BankAccount
  def initialize(balance)
    @balance = balance
  end

  # Getter - read balance
  def balance
    @balance
  end

  # Setter - change balance
  def balance=(new_balance)
    @balance = new_balance
  end

  def deposit(amount)
    @balance += amount
  end
end

account = BankAccount.new(1000)
puts account.balance   # 1000

account.balance = 1500
puts account.balance   # 1500

account.deposit(500)
puts account.balance   # 2000
```

**Using attr_accessor (cleaner):**
```ruby
class Car
  # Create both getter and setter for @brand and @color
  attr_accessor :brand, :color
  
  # Create only getter for @year
  attr_reader :year
  
  # Create only setter for @owner
  attr_writer :owner

  def initialize(brand, color, year)
    @brand = brand
    @color = color
    @year = year
  end
end

car = Car.new("Toyota", "Red", 2023)

puts car.brand        # Toyota
car.brand = "Honda"   # Set using setter
puts car.brand        # Honda

puts car.year         # 2023
# car.year = 2024     # ERROR - only reader, no setter

# car.owner = "John"  # Works but no reader
# puts car.owner      # ERROR - no getter
```

#### Class Variables and Methods

**Class Variables:**
```ruby
class Student
  @@student_count = 0  # Class variable - shared by all instances

  def initialize(name)
    @name = name
    @@student_count += 1
  end

  def self.total_students
    @@student_count
  end
end

puts Student.total_students  # 0

alice = Student.new("Alice")
puts Student.total_students  # 1

bob = Student.new("Bob")
puts Student.total_students  # 2

charlie = Student.new("Charlie")
puts Student.total_students  # 3
```

**Class Methods:**
```ruby
class Math
  # Class method - called on class, not instance
  def self.square(n)
    n * n
  end

  # Instance method
  def cube(n)
    n * n * n
  end
end

# Class method
puts Math.square(5)  # 25

# Instance method
math = Math.new
puts math.cube(3)    # 27
```

**Constants:**
```ruby
class Circle
  PI = 3.14159
  MIN_RADIUS = 0

  def initialize(radius)
    @radius = radius
  end

  def area
    PI * @radius ** 2
  end

  def circumference
    2 * PI * @radius
  end
end

circle = Circle.new(5)
puts circle.area          # 78.54
puts circle.circumference # 31.4159
puts Circle::PI           # 3.14159 (access constant from outside)
```

#### Practice Exercise 6
```ruby
# Create a Bank Account class with:
# 1. Initialize with name and initial balance
# 2. Deposit method
# 3. Withdraw method
# 4. Check balance method
# 5. Account fee (reduce balance by percentage)

class BankAccount
  attr_reader :name, :balance

  def initialize(name, initial_balance)
    @name = name
    @balance = initial_balance
  end

  def deposit(amount)
    if amount > 0
      @balance += amount
      puts "Deposited $#{amount}. New balance: $#{@balance}"
    else
      puts "Invalid amount"
    end
  end

  def withdraw(amount)
    if amount > 0 && amount <= @balance
      @balance -= amount
      puts "Withdrawn $#{amount}. New balance: $#{@balance}"
    else
      puts "Invalid amount or insufficient balance"
    end
  end

  def apply_fee(fee_percentage)
    fee = @balance * (fee_percentage / 100.0)
    @balance -= fee
    puts "Fee of $#{fee.round(2)} applied. New balance: $#{@balance.round(2)}"
  end
end

# Test
account = BankAccount.new("Alice", 1000)
account.deposit(500)        # Deposited $500. New balance: $1500
account.withdraw(200)       # Withdrawn $200. New balance: $1300
account.apply_fee(2)        # Fee of $26.0 applied. New balance: $1274.0
```

### Day 7: Inheritance and Modules

#### Inheritance (IS-A Relationship)

**Basic Inheritance:**
```ruby
# Parent class
class Animal
  def initialize(name)
    @name = name
  end

  def make_sound
    "Some generic sound"
  end

  def introduce
    "I am #{@name}"
  end
end

# Child class (inherits from Animal)
class Dog < Animal
  # Child automatically has @name from parent
  
  # Override parent method
  def make_sound
    "Woof!"
  end

  # Add new method specific to Dog
  def fetch
    "Fetching the ball..."
  end
end

dog = Dog.new("Max")
puts dog.introduce        # I am Max
puts dog.make_sound       # Woof!
puts dog.fetch            # Fetching the ball...

# Another child class
class Cat < Animal
  def make_sound
    "Meow!"
  end

  def scratch
    "Scratching..."
  end
end

cat = Cat.new("Whiskers")
puts cat.make_sound       # Meow!
puts cat.scratch          # Scratching...
```

**Using Super:**
```ruby
class Vehicle
  def initialize(brand)
    @brand = brand
  end

  def describe
    "Brand: #{@brand}"
  end
end

class Car < Vehicle
  def initialize(brand, color)
    super(brand)  # Call parent's initialize
    @color = color
  end

  def describe
    super + " Color: #{@color}"  # Call parent's method and add to it
  end
end

car = Car.new("Toyota", "Red")
puts car.describe  # Brand: Toyota Color: Red
```

**Abstract Methods (not enforced in Ruby, but by convention):**
```ruby
class Shape
  def area
    raise "Subclass must implement area method"
  end
end

class Rectangle < Shape
  def initialize(width, height)
    @width = width
    @height = height
  end

  def area
    @width * @height
  end
end

class Circle < Shape
  def initialize(radius)
    @radius = radius
  end

  def area
    3.14159 * @radius ** 2
  end
end

rect = Rectangle.new(4, 5)
puts rect.area    # 20

circle = Circle.new(3)
puts circle.area  # 28.27...
```

#### Modules (Mix-in / Shared Behavior)

**Basic Module:**
```ruby
# Module acts like a mixin
module Flyable
  def fly
    "Flying..."
  end

  def land
    "Landing..."
  end
end

module Swimmable
  def swim
    "Swimming..."
  end
end

class Bird
  include Flyable  # Mix in the Flyable module
end

class Fish
  include Swimmable
end

class Duck
  include Flyable
  include Swimmable
end

bird = Bird.new
puts bird.fly      # Flying...

fish = Fish.new
puts fish.swim     # Swimming...

duck = Duck.new
puts duck.fly      # Flying...
puts duck.swim     # Swimming...
```

**Modules with Instance Variables:**
```ruby
module Nameable
  def set_name(name)
    @name = name
  end

  def get_name
    @name
  end
end

class Person
  include Nameable
end

person = Person.new
person.set_name("Alice")
puts person.get_name  # Alice
```

**Modules vs Inheritance:**
```
INHERITANCE (IS-A):
├─ Use when: "A is a type of B"
├─ Example: Dog IS-A Animal
└─ Single inheritance only (one parent)

MODULES (HAS-A / Can-Do):
├─ Use when: "A can do B"
├─ Example: Bird CAN-DO fly, CAN-DO sing
└─ Multiple mixins possible
```

#### Practice Exercise 7
```ruby
# Create an inheritance hierarchy for shapes

class Shape
  def initialize(name)
    @name = name
  end

  def describe
    "I am a #{@name}"
  end
end

class Polygon < Shape
  def initialize(name, sides)
    super(name)
    @sides = sides
  end

  def describe
    super + " with #{@sides} sides"
  end
end

class Triangle < Polygon
  def initialize
    super("Triangle", 3)
  end

  def area_formula
    "Area = 0.5 * base * height"
  end
end

class Square < Polygon
  def initialize
    super("Square", 4)
  end

  def area_formula
    "Area = side * side"
  end
end

# Test
triangle = Triangle.new
puts triangle.describe       # I am a Triangle with 3 sides
puts triangle.area_formula   # Area = 0.5 * base * height

square = Square.new
puts square.describe         # I am a Square with 4 sides
puts square.area_formula     # Area = side * side
```

---

### Day 8-12: Advanced OOP Concepts

#### Polymorphism

```ruby
# Different classes, same interface
class CreditCard
  def process_payment(amount)
    "Processing #{amount} via Credit Card"
  end
end

class PayPal
  def process_payment(amount)
    "Processing #{amount} via PayPal"
  end
end

class ApplePay
  def process_payment(amount)
    "Processing #{amount} via Apple Pay"
  end
end

# Use polymorphism
def checkout(payment_method, amount)
  puts payment_method.process_payment(amount)
end

checkout(CreditCard.new, 100)  # Processing 100 via Credit Card
checkout(PayPal.new, 50)       # Processing 50 via PayPal
checkout(ApplePay.new, 75)     # Processing 75 via Apple Pay
```

#### Composition (HAS-A Relationship)

```ruby
class Address
  attr_accessor :street, :city, :zip

  def initialize(street, city, zip)
    @street = street
    @city = city
    @zip = zip
  end

  def full_address
    "#{@street}, #{@city} #{@zip}"
  end
end

class Person
  attr_accessor :name, :address

  def initialize(name, address)
    @name = name
    @address = address
  end

  def info
    "#{@name} lives at #{@address.full_address}"
  end
end

# Usage
address = Address.new("123 Main St", "New York", "10001")
person = Person.new("Alice", address)
puts person.info  # Alice lives at 123 Main St, New York 10001
```

#### Encapsulation (Hiding Internal Details)

```ruby
class Temperature
  attr_reader :celsius

  def initialize(celsius)
    @celsius = celsius
  end

  # Private method - can't call from outside
  private

  def validate_temperature
    @celsius > -273.15  # Absolute zero
  end

  # Public method that uses private method
  public

  def fahrenheit
    (@celsius * 9/5.0) + 32
  end

  def is_valid?
    validate_temperature
  end
end

temp = Temperature.new(20)
puts temp.fahrenheit       # 68.0
puts temp.is_valid?        # true
# temp.validate_temperature  # ERROR - private method
```

#### Class Inheritance Pattern (Real-World Example)

```ruby
class Vehicle
  attr_reader :brand, :year

  def initialize(brand, year)
    @brand = brand
    @year = year
  end

  def info
    "#{@year} #{@brand}"
  end
end

class Car < Vehicle
  attr_accessor :doors

  def initialize(brand, year, doors)
    super(brand, year)
    @doors = doors
  end

  def info
    super + " with #{@doors} doors"
  end
end

class Motorcycle < Vehicle
  attr_accessor :has_sidecar

  def initialize(brand, year, has_sidecar)
    super(brand, year)
    @has_sidecar = has_sidecar
  end

  def info
    sidecar_text = @has_sidecar ? "with sidecar" : "without sidecar"
    super + " #{sidecar_text}"
  end
end

# Usage
car = Car.new("Toyota", 2023, 4)
puts car.info  # 2023 Toyota with 4 doors

motorcycle = Motorcycle.new("Harley", 2023, true)
puts motorcycle.info  # 2023 Harley with sidecar
```

---

## PHASE 3: ADVANCED RUBY FEATURES (Days 13-20)

### Day 13: Blocks, Procs, and Lambdas

#### Blocks

**What are Blocks?**
```ruby
# Block is code between {} or do...end
[1, 2, 3].each { |num| puts num }  # Block with {}

[1, 2, 3].each do |num|
  puts num
end
# Both are blocks

# Defining method that accepts a block
def greet
  yield  # Execute the block
end

greet { puts "Hello from block!" }
# Hello from block!

# Block with parameters
def process_numbers
  yield(5)
  yield(10)
end

process_numbers { |n| puts n * 2 }
# 10
# 20

# Check if block given
def conditional_block
  if block_given?
    yield "Block was given"
  else
    puts "No block given"
  end
end

conditional_block { |msg| puts msg }  # Block was given
conditional_block                      # No block given
```

#### Procs

```ruby
# Proc is an object representing a block
my_proc = Proc.new { |name| puts "Hello, #{name}!" }

my_proc.call("Alice")   # Hello, Alice!
my_proc.call("Bob")     # Hello, Bob!

# Proc with do...end
another_proc = Proc.new do |x|
  puts x * 2
end

another_proc.call(5)    # 10
another_proc.call(10)   # 20

# Pass proc to method
def execute_twice(proc)
  proc.call
  proc.call
end

my_proc = Proc.new { puts "Executing..." }
execute_twice(my_proc)
# Executing...
# Executing...

# Shorthand: &proc
def take_block(&block)
  block.call
end

take_block { puts "This is a block" }  # This is a block
```

#### Lambdas

```ruby
# Lambda is strict proc
# Difference: strict about argument count, implicit return

# Creating lambda
my_lambda = lambda { |x| x * 2 }
puts my_lambda.call(5)  # 10

# Shorthand using ->
my_lambda2 = ->(x) { x * 3 }
puts my_lambda2.call(5)  # 15

# Multiple arguments
add = ->(a, b) { a + b }
puts add.call(3, 4)  # 7

# Multiline lambda
greet = ->(name) do
  message = "Hello, #{name}"
  puts message
end

greet.call("Alice")  # Hello, Alice

# Lambda vs Proc - argument strictness
my_proc = Proc.new { |x| puts x }
my_proc.call(5, 10, 15)  # 5 (ignores extra arguments)

my_lambda = ->(x) { puts x }
# my_lambda.call(5, 10, 15)  # ERROR - wrong number of arguments

# Return behavior
def proc_return
  my_proc = Proc.new { return "Proc returned" }
  my_proc.call
  return "Method end"
end

puts proc_return  # Proc returned

def lambda_return
  my_lambda = ->(){ return "Lambda returned" }
  my_lambda.call
  return "Method end"
end

puts lambda_return  # Method end
```

#### Using Blocks with Built-in Methods

```ruby
# Map
numbers = [1, 2, 3, 4, 5]
doubled = numbers.map { |n| n * 2 }
puts doubled.inspect  # [2, 4, 6, 8, 10]

# Select
evens = numbers.select { |n| n.even? }
puts evens.inspect  # [2, 4]

# Reject
odds = numbers.reject { |n| n.even? }
puts odds.inspect  # [1, 3, 5]

# Each with index
["a", "b", "c"].each_with_index do |letter, index|
  puts "#{index}: #{letter}"
end
# 0: a
# 1: b
# 2: c

# Find
result = numbers.find { |n| n > 3 }
puts result  # 4

# All? / Any?
puts numbers.all? { |n| n > 0 }   # true
puts numbers.any? { |n| n > 4 }   # true

# Sort with block
words = ["apple", "zebra", "banana"]
sorted = words.sort { |a, b| b <=> a }  # Descending
puts sorted.inspect  # ["zebra", "banana", "apple"]
```

#### Practice Exercise (Blocks/Procs/Lambdas)
```ruby
# 1. Create a method that takes a block and calls it 3 times
def repeat_thrice
  3.times { yield }
end

repeat_thrice { puts "Hello!" }

# 2. Create a proc that adds numbers
add = Proc.new { |a, b| a + b }
puts add.call(5, 3)  # 8

# 3. Create lambda that multiplies
multiply = ->(x, y) { x * y }
puts multiply.call(4, 5)  # 20

# 4. Use map to transform array
numbers = [1, 2, 3, 4, 5]
squared = numbers.map { |n| n ** 2 }
puts squared.inspect  # [1, 4, 9, 16, 25]
```

---

### Day 14: Exception Handling

#### Begin/Rescue/End

```ruby
# Handle division by zero
begin
  result = 10 / 0
rescue
  puts "Cannot divide by zero"
end

# Specific error handling
begin
  number = Integer("abc")
rescue ArgumentError
  puts "Invalid number format"
rescue ZeroDivisionError
  puts "Cannot divide by zero"
end

# Accessing error information
begin
  array = [1, 2, 3]
  value = array[10]  # Returns nil, no error here
rescue IndexError => error
  puts "Error: #{error.message}"
end

# Multiple rescue clauses
begin
  # Some code
rescue TypeError => e
  puts "Type error: #{e.message}"
rescue ArgumentError => e
  puts "Argument error: #{e.message}"
rescue => e  # Catch-all for any StandardError
  puts "Unknown error: #{e.message}"
end
```

#### Ensure and Else

```ruby
# Ensure runs regardless of success or failure
begin
  file = File.open("data.txt")
  # Read file
rescue FileNotFoundError
  puts "File not found"
ensure
  file.close if file  # Always close file
end

# Else runs only if no error
begin
  result = 10 / 2
rescue ZeroDivisionError
  puts "Cannot divide by zero"
else
  puts "Result: #{result}"  # This runs
ensure
  puts "Done"  # Always runs
end
```

#### Raise Exceptions

```ruby
# Raise built-in exception
def divide(a, b)
  if b == 0
    raise ZeroDivisionError, "Cannot divide by zero"
  end
  a / b
end

begin
  divide(10, 0)
rescue ZeroDivisionError => e
  puts "Error: #{e.message}"
end

# Custom exception
class InvalidAgeError < StandardError
end

def check_age(age)
  if age < 0
    raise InvalidAgeError, "Age cannot be negative"
  end
end

begin
  check_age(-5)
rescue InvalidAgeError => e
  puts e.message
end
```

#### Custom Exceptions

```ruby
class BankException < StandardError
end

class InsufficientFundsError < BankException
end

class InvalidAccountError < BankException
end

class BankAccount
  def initialize(balance)
    @balance = balance
  end

  def withdraw(amount)
    if amount > @balance
      raise InsufficientFundsError, "Insufficient funds"
    end
    @balance -= amount
  end
end

account = BankAccount.new(100)

begin
  account.withdraw(150)
rescue InsufficientFundsError => e
  puts "Cannot withdraw: #{e.message}"
end
```

---

### Day 15: File I/O and String Manipulation

#### Reading Files

```ruby
# Read entire file
content = File.read("data.txt")
puts content

# Read line by line
File.open("data.txt") do |file|
  file.each_line do |line|
    puts line.strip  # Remove newline
  end
end

# Read all lines into array
lines = File.readlines("data.txt")
lines.each { |line| puts line }

# Read first 5 lines
file = File.open("data.txt")
5.times do
  puts file.gets  # Read one line
end
file.close
```

#### Writing Files

```ruby
# Write content (overwrites if file exists)
File.write("output.txt", "Hello, World!")

# Append to file
File.open("output.txt", "a") do |file|
  file.puts "This is appended"
end

# Write multiple lines
lines = ["Line 1", "Line 2", "Line 3"]
File.open("output.txt", "w") do |file|
  lines.each { |line| file.puts line }
end

# Clear file
File.write("output.txt", "")
```

#### String Manipulation Advanced

```ruby
text = "Hello, World!"

# Case operations
puts text.upcase           # HELLO, WORLD!
puts text.downcase         # hello, world!
puts text.swapcase         # hELLO, wORLD!
puts text.capitalize       # Hello, world!

# Splitting and joining
words = text.split(", ")   # ["Hello", "World!"]
puts words.join(" - ")     # Hello - World!

# Characters
puts text.chars.inspect    # ["H", "e", "l", "l", "o", ",", " ", "W", "o", "r", "l", "d", "!"]

# Count
puts text.count("l")       # 3 (occurrences of 'l')

# Slice/Substring
puts text[0..4]            # Hello
puts text.slice(0, 5)      # Hello

# Regex (regular expressions)
if text.match?(/World/)
  puts "Contains 'World'"
end

# Replace using regex
result = text.gsub(/l/, "L")
puts result                # HeLLo, WorLd!

# Extract using regex
matches = text.scan(/\w+/)  # Extract words
puts matches.inspect       # ["Hello", "World"]
```

---

### Days 16-20: More Advanced Topics

#### Regular Expressions (Regex)

```ruby
# Basic matching
string = "The year is 2024"

if string =~ /\d+/  # Contains digits?
  puts "Contains numbers"
end

# Patterns
puts "cat".match?(/cat/)           # true
puts "The quick brown fox".match?(/qu/)  # true

# Extracting data
email = "alice@example.com"
match = email.match(/(.+)@(.+)/)
if match
  puts "Username: #{match[1]}"     # alice
  puts "Domain: #{match[2]}"       # example.com
end

# Substitution
text = "I like cats and dogs"
new_text = text.gsub(/cat/, "mouse")
puts new_text  # I like mouses and dogs

# Case-insensitive
puts "HELLO".match?(/hello/i)  # true
```

#### Working with JSON

```ruby
require 'json'

# Ruby hash
person = {
  name: "Alice",
  age: 25,
  email: "alice@example.com"
}

# Convert to JSON string
json_string = person.to_json
puts json_string
# {"name":"Alice","age":25,"email":"alice@example.com"}

# Parse JSON back to Ruby
parsed = JSON.parse(json_string)
puts parsed["name"]   # Alice
puts parsed["age"]    # 25

# Parse file
data = JSON.parse(File.read("data.json"))
```

#### Testing (Introduction)

```ruby
# Using built-in assertions
def assert(condition, message)
  raise "Assertion failed: #{message}" unless condition
end

# Test a function
def add(a, b)
  a + b
end

begin
  assert(add(2, 3) == 5, "2 + 3 should equal 5")
  assert(add(10, 20) == 30, "10 + 20 should equal 30")
  puts "All tests passed!"
rescue => e
  puts e.message
end
```

---

## PHASE 4: FUNCTIONAL PROGRAMMING & METAPROGRAMMING (Days 21-28)

### Day 21: Functional Programming

```ruby
# Map - transform elements
numbers = [1, 2, 3, 4, 5]
doubled = numbers.map { |n| n * 2 }

# Select - filter elements
evens = numbers.select { |n| n.even? }

# Reduce - combine elements
sum = numbers.reduce(0) { |acc, n| acc + n }

# Chaining operations
result = numbers
  .select { |n| n > 2 }
  .map { |n| n * 2 }
  .reduce(0) { |acc, n| acc + n }

puts result  # (3*2 + 4*2 + 5*2) = 24

# Immutability (don't modify original)
original = [1, 2, 3]
modified = original.map { |n| n * 2 }  # Returns new array
puts original.inspect   # [1, 2, 3]
puts modified.inspect   # [2, 4, 6]

# Compose functions
double = ->(x) { x * 2 }
add_ten = ->(x) { x + 10 }
compose = ->(f, g) { ->(x) { f.call(g.call(x)) } }

my_func = compose.call(double, add_ten)
puts my_func.call(5)  # (5 + 10) * 2 = 30
```

### Day 22: Metaprogramming (Dynamic Code)

```ruby
# Define methods dynamically
class User
  define_method(:greet) do
    "Hello, I'm #{self.class}"
  end
end

user = User.new
puts user.greet  # Hello, I'm User

# Define multiple methods
class Article
  [:title, :author, :content].each do |attr|
    attr_accessor attr
  end
end

article = Article.new
article.title = "Ruby Guide"
puts article.title  # Ruby Guide

# Respond to missing method
class OpenStruct
  def method_missing(name, *args)
    if name.to_s.end_with?("=")
      attr = name.to_s.chomp("=")
      instance_variable_set("@#{attr}", args.first)
    else
      instance_variable_get("@#{name}")
    end
  end
end

obj = OpenStruct.new
obj.name = "Alice"
puts obj.name  # Alice

# Send - call method dynamically
class Calculator
  def add(a, b)
    a + b
  end

  def multiply(a, b)
    a * b
  end
end

calc = Calculator.new
method_name = "add"
result = calc.send(method_name, 5, 3)
puts result  # 8
```

---

## PHASE 5: RUBY ON RAILS BASICS (Days 29-42)

### Day 29-35: Rails Introduction

#### Installation and Setup

```bash
# Install Rails
gem install rails

# Create new app
rails new my_app
cd my_app

# Start server
rails server  # Visit http://localhost:3000

# Generate model
rails generate model User name:string email:string age:integer

# Generate controller
rails generate controller Pages home about

# Run migrations
rails db:migrate
```

#### Models (Active Record)

```ruby
# app/models/user.rb
class User < ApplicationRecord
  validates :email, presence: true
  validates :age, numericality: { greater_than: 0 }

  has_many :posts
end

# Create user
user = User.new(name: "Alice", email: "alice@example.com", age: 25)
user.save

# Or create directly
user = User.create(name: "Bob", email: "bob@example.com", age: 30)

# Find user
user = User.find(1)
user = User.find_by(email: "alice@example.com")

# Update
user.update(age: 26)

# Delete
user.destroy
```

#### Controllers and Routes

```ruby
# config/routes.rb
Rails.application.routes.draw do
  resources :users          # RESTful routes
  get "pages/home"
  get "pages/about"
end

# app/controllers/users_controller.rb
class UsersController < ApplicationController
  def index
    @users = User.all
  end

  def show
    @user = User.find(params[:id])
  end

  def new
    @user = User.new
  end

  def create
    @user = User.create(user_params)
    redirect_to @user
  end

  private

  def user_params
    params.require(:user).permit(:name, :email, :age)
  end
end
```

#### Views (ERB Templates)

```erb
<!-- app/views/users/index.html.erb -->
<h1>Users</h1>

<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Email</th>
      <th>Age</th>
      <th>Actions</th>
    </tr>
  </thead>
  <tbody>
    <% @users.each do |user| %>
      <tr>
        <td><%= user.name %></td>
        <td><%= user.email %></td>
        <td><%= user.age %></td>
        <td>
          <%= link_to "View", user_path(user) %>
          <%= link_to "Edit", edit_user_path(user) %>
          <%= link_to "Delete", user_path(user), method: :delete %>
        </td>
      </tr>
    <% end %>
  </tbody>
</table>

<%= link_to "New User", new_user_path, class: "btn btn-primary" %>
```

---

## PRACTICE PROJECTS

### Project 1: To-Do List (Beginner)
```ruby
class TodoList
  def initialize
    @tasks = []
  end

  def add_task(task)
    @tasks << { task: task, completed: false }
  end

  def complete_task(index)
    @tasks[index][:completed] = true if @tasks[index]
  end

  def show_tasks
    @tasks.each_with_index do |item, index|
      status = item[:completed] ? "[✓]" : "[ ]"
      puts "#{index + 1}. #{status} #{item[:task]}"
    end
  end

  def remove_task(index)
    @tasks.delete_at(index)
  end
end

# Usage
todo = TodoList.new
todo.add_task("Learn Ruby")
todo.add_task("Build a project")
todo.add_task("Deploy app")
todo.show_tasks
todo.complete_task(0)
todo.show_tasks
```

### Project 2: Simple Bank (Intermediate)
```ruby
class Bank
  attr_reader :accounts

  def initialize
    @accounts = {}
  end

  def create_account(account_number, initial_balance)
    @accounts[account_number] = BankAccount.new(account_number, initial_balance)
  end

  def transfer(from_account, to_account, amount)
    if @accounts[from_account] && @accounts[to_account]
      @accounts[from_account].withdraw(amount)
      @accounts[to_account].deposit(amount)
      puts "Transferred #{amount} from #{from_account} to #{to_account}"
    else
      puts "Invalid account number"
    end
  end

  def check_balance(account_number)
    @accounts[account_number]&.balance || "Account not found"
  end
end

class BankAccount
  attr_reader :number, :balance

  def initialize(number, balance)
    @number = number
    @balance = balance
  end

  def deposit(amount)
    @balance += amount
  end

  def withdraw(amount)
    if amount <= @balance
      @balance -= amount
    else
      puts "Insufficient funds"
    end
  end
end
```

### Project 3: Library System (Advanced)
```ruby
class Library
  def initialize
    @books = []
    @members = []
  end

  def add_book(book)
    @books << book
  end

  def add_member(member)
    @members << member
  end

  def search_by_title(title)
    @books.find { |book| book.title == title }
  end

  def borrow_book(member_name, title)
    book = search_by_title(title)
    member = @members.find { |m| m.name == member_name }

    if book && member && book.available?
      book.borrow(member)
      puts "#{member_name} borrowed #{title}"
    else
      puts "Cannot borrow book"
    end
  end

  def return_book(title)
    book = search_by_title(title)
    if book
      book.return_book
      puts "#{title} returned"
    end
  end
end

class Book
  attr_reader :title, :author

  def initialize(title, author)
    @title = title
    @author = author
    @borrowed_by = nil
  end

  def available?
    @borrowed_by.nil?
  end

  def borrow(member)
    @borrowed_by = member
  end

  def return_book
    @borrowed_by = nil
  end
end

class Member
  attr_reader :name

  def initialize(name)
    @name = name
  end
end
```

---

## ADVANCED TOPICS

### Debugging and Testing

#### Debugging with pry
```ruby
# Install pry
gem install pry

# Use in code
require 'pry'

def calculate(x, y)
  result = x + y
  binding.pry  # Stops here, you can inspect variables
  result * 2
end

# In pry console:
# > x
# > y
# > result
# > exit
```

#### Testing with RSpec
```ruby
# Gemfile
group :test do
  gem 'rspec'
end

# spec/calculator_spec.rb
require 'rspec'
require_relative '../calculator'

describe Calculator do
  let(:calc) { Calculator.new }

  describe '#add' do
    it 'adds two positive numbers' do
      expect(calc.add(2, 3)).to eq(5)
    end

    it 'adds negative numbers' do
      expect(calc.add(-2, 3)).to eq(1)
    end
  end

  describe '#multiply' do
    it 'multiplies two numbers' do
      expect(calc.multiply(3, 4)).to eq(12)
    end
  end
end

# Run tests
rspec spec/calculator_spec.rb
```

### Performance and Optimization

```ruby
# Avoid N+1 queries
# Bad:
users = User.all
users.each do |user|
  puts user.posts  # Query for each user!
end

# Good:
users = User.includes(:posts)  # Load all at once
users.each do |user|
  puts user.posts
end

# Use select for specific columns
users = User.select(:id, :name)  # Faster than User.all

# Batch operations
User.find_in_batches(batch_size: 1000) do |batch|
  batch.each { |user| user.update(active: true) }
end

# Profile code
require 'benchmark'
time = Benchmark.measure do
  1_000_000.times { "string concatenation" + " test" }
end
puts time
```

### Gems and Dependencies

```ruby
# Gemfile
source 'https://rubygems.org'

gem 'rails', '~> 7.0'
gem 'sqlite3'
gem 'puma'

# For JSON APIs
gem 'active_model_serializers'

# For async jobs
gem 'sidekiq'

# For environment variables
gem 'dotenv-rails'

# For pagination
gem 'kaminari'

# For validation
gem 'validates'

# Install gems
bundle install

# Update gems
bundle update
```

### Web Scraping

```ruby
require 'nokogiri'
require 'http'

# Fetch HTML
response = HTTP.get('https://example.com')
html = response.body

# Parse with Nokogiri
doc = Nokogiri::HTML(html)

# Select elements
titles = doc.css('.title')
titles.each { |title| puts title.text }

# Extract specific data
links = doc.css('a').map { |a| a['href'] }
puts links
```

### API Development

```ruby
# config/routes.rb
Rails.application.routes.draw do
  namespace :api do
    namespace :v1 do
      resources :users
      resources :posts
    end
  end
end

# app/controllers/api/v1/users_controller.rb
module Api
  module V1
    class UsersController < ApplicationController
      def index
        @users = User.all
        render json: @users
      end

      def show
        @user = User.find(params[:id])
        render json: @user
      end

      def create
        @user = User.new(user_params)
        if @user.save
          render json: @user, status: :created
        else
          render json: @user.errors, status: :unprocessable_entity
        end
      end

      private

      def user_params
        params.require(:user).permit(:name, :email)
      end
    end
  end
end
```

---

## COMMON MISTAKES TO AVOID

1. **Mutable Default Arguments**
   ```ruby
   # Bad
   def add_item(item, list = [])
     list << item
     list
   end

   # Good
   def add_item(item, list = nil)
     list ||= []
     list << item
     list
   end
   ```

2. **Nil References**
   ```ruby
   # Bad
   person[:name].upcase  # Error if person is nil

   # Good
   person&.[:name]&.upcase  # Safe navigation operator
   ```

3. **String Interpolation vs Concatenation**
   ```ruby
   # Slower
   message = "Hello " + name + " how are you " + status

   # Faster
   message = "Hello #{name} how are you #{status}"
   ```

4. **Unnecessary Instance Variables**
   ```ruby
   # Bad
   class User
     def initialize(name)
       @name = name
     end

     def greet
       puts "Hello #{@name}"
     end
   end

   # Good - if you don't need persistence
   def greet(name)
     puts "Hello #{name}"
   end
   ```

5. **Bare Rescue**
   ```ruby
   # Bad - catches everything including system errors
   begin
     dangerous_operation
   rescue
     # Do something
   end

   # Good - specific exceptions
   begin
     dangerous_operation
   rescue ArgumentError => e
     puts "Invalid argument: #{e.message}"
   end
   ```

---

## LEARNING ROADMAP

### Week 1-2: Fundamentals
- [ ] Variables and data types
- [ ] Control flow (if/else/case)
- [ ] Loops and iteration
- [ ] Arrays and hashes
- [ ] String manipulation
- [ ] Methods introduction

**Goal**: Write simple programs

### Week 3-4: Object-Oriented Programming
- [ ] Classes and objects
- [ ] Inheritance
- [ ] Modules and mixins
- [ ] Encapsulation
- [ ] Polymorphism

**Goal**: Understand OOP principles

### Week 5-6: Advanced Ruby
- [ ] Blocks, procs, lambdas
- [ ] Exception handling
- [ ] File I/O
- [ ] Functional programming
- [ ] Metaprogramming basics

**Goal**: Master Ruby language features

### Week 7-8: Rails Basics
- [ ] Rails setup and structure
- [ ] Models (Active Record)
- [ ] Controllers and routes
- [ ] Views (ERB)
- [ ] Database migrations

**Goal**: Build simple web apps

### Ongoing
- [ ] Testing with RSpec
- [ ] Performance optimization
- [ ] Gems and libraries
- [ ] REST APIs
- [ ] Real-world projects

---

## RESOURCES FOR FURTHER LEARNING

### Official Documentation
- [Ruby Docs](https://ruby-doc.org/)
- [Rails Guides](https://guides.rubyonrails.org/)
- [Bundler](https://bundler.io/)

### Interactive Learning
- [Ruby Koans](https://rubykoans.com/)
- [Codewars](https://www.codewars.com/)
- [LeetCode](https://leetcode.com/)

### Books
- "The Well-Grounded Rubyist" by David A. Black
- "Eloquent Ruby" by Russ Olsen
- "Practical Object-Oriented Design" by Sandi Metz

### Websites
- [RubyGuides](https://www.rubyguides.com/)
- [Ruby Tapas](https://www.rubytapas.com/)
- [GoRails](https://gorails.com/)

---

## CHEAT SHEET

### String Methods
```ruby
str.upcase              # HELLO
str.downcase            # hello
str.capitalize          # Hello
str.reverse             # olleh
str.length              # 5
str.include?("ell")     # true
str.start_with?("He")   # true
str.end_with?("lo")     # true
str.split(" ")          # ["Hello", "World"]
str.chars               # ["H", "e", "l", "l", "o"]
str.gsub(/l/, "L")      # HeLLo
str.strip               # Remove whitespace
```

### Array Methods
```ruby
arr.length              # Size
arr.first               # First element
arr.last                # Last element
arr.push(item)          # Add to end
arr.pop                 # Remove from end
arr.unshift(item)       # Add to beginning
arr.shift               # Remove from beginning
arr.include?(item)      # Contains?
arr.index(item)         # Position
arr.reverse             # Reversed copy
arr.sort                # Sorted copy
arr.uniq                # Remove duplicates
arr.flatten             # Flatten nested
arr.join(", ")          # Convert to string
arr.map { |x| x*2 }     # Transform
arr.select { |x| x>5 }  # Filter
arr.reject { |x| x>5 }  # Opposite filter
arr.reduce(:+)          # Combine
```

### Hash Methods
```ruby
hash.keys               # All keys
hash.values             # All values
hash.length             # Size
hash.empty?             # Empty?
hash.key?(key)          # Has key?
hash.value?(val)        # Has value?
hash.each { |k,v| ... } # Iterate
hash.select { |k,v| ... }
hash.merge(other)       # Combine
hash.delete(key)        # Remove
```

### Useful Methods
```ruby
# Ranges
(1..5).to_a             # [1, 2, 3, 4, 5]
(1...5).to_a            # [1, 2, 3, 4] (excludes end)

# Type conversion
"123".to_i              # 123
"3.14".to_f             # 3.14
123.to_s                # "123"

# Conditionals
a > b ? "yes" : "no"    # Ternary
a && b                  # AND
a || b                  # OR
!a                      # NOT
a.nil?                  # Is nil?
```

---

## NEXT STEPS AFTER LEARNING RUBY

1. **Master Rails** - Build full-stack web applications
2. **Learn Databases** - SQL, PostgreSQL, Redis
3. **DevOps Basics** - Docker, Kubernetes, AWS
4. **Testing** - RSpec, Cucumber, Factory Bot
5. **Performance** - Profiling, caching, optimization
6. **Real Projects** - Build something you can use
7. **Open Source** - Contribute to Ruby projects
8. **Advanced Topics** - Metaprogramming, DSLs, Concurrency

---

## FINAL TIPS

1. **Code Every Day** - Even 30 minutes daily beats one long session
2. **Build Projects** - Theory + Practice = Mastery
3. **Read Others' Code** - Learn from open source
4. **Use IRB** - Experiment interactively
5. **Debug Thoroughly** - Understand errors, don't just fix them
6. **Join Community** - Ruby community is very welcoming
7. **Keep Learning** - Ruby evolves, stay updated
8. **Have Fun** - Ruby is designed to be enjoyable

---

## CONCLUSION

Ruby is a beautiful, expressive language that rewards good practices. This guide covers:

✅ Fundamentals (variables, data types, control flow)
✅ Object-Oriented Programming (classes, inheritance, modules)
✅ Advanced Features (blocks, exceptions, metaprogramming)
✅ Functional Programming (map, select, reduce)
✅ Rails Basics (models, controllers, views)
✅ Real Projects (to-do list, bank, library)

**Your goal now**: Build projects and keep learning!

Good luck on your Ruby journey! 🚀

---

**Last Updated**: Today
**Total Content**: 50+ sections, 100+ code examples, 3+ projects
**Estimated Learning Time**: 4-6 weeks with daily practice
