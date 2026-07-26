# RUBY PRACTICE EXERCISES - Beginner to Advanced

## SECTION 1: BASICS (Days 1-5)

### Exercise 1.1: Variables and Math
**Difficulty**: ⭐

Create a program that:
1. Stores your birth year
2. Calculates your approximate age
3. Calculates when you'll turn 100
4. Prints formatted output

```ruby
# Solution:
birth_year = 1998
current_year = 2024
age = current_year - birth_year
turn_100_year = birth_year + 100

puts "Birth Year: #{birth_year}"
puts "Current Age: #{age}"
puts "Will turn 100 in: #{turn_100_year}"
```

### Exercise 1.2: String Operations
**Difficulty**: ⭐

Create a program that:
1. Takes a sentence as input
2. Converts it to uppercase and lowercase
3. Counts the number of characters
4. Reverses the sentence

```ruby
# Solution:
sentence = "Ruby is awesome"

puts "Original: #{sentence}"
puts "Uppercase: #{sentence.upcase}"
puts "Lowercase: #{sentence.downcase}"
puts "Character count: #{sentence.length}"
puts "Reversed: #{sentence.reverse}"
```

### Exercise 1.3: Control Flow - Grade Calculator
**Difficulty**: ⭐⭐

Create a program that:
1. Takes a score (0-100)
2. Assigns a grade (A, B, C, D, F)
3. Prints feedback for each grade

```ruby
# Solution:
def grade_calculator(score)
  case score
  when 90..100
    grade = "A"
    feedback = "Excellent!"
  when 80..89
    grade = "B"
    feedback = "Good job!"
  when 70..79
    grade = "C"
    feedback = "Average"
  when 60..69
    grade = "D"
    feedback = "Poor"
  else
    grade = "F"
    feedback = "Failed"
  end

  puts "Score: #{score}, Grade: #{grade} - #{feedback}"
end

grade_calculator(85)
grade_calculator(72)
grade_calculator(95)
```

### Exercise 1.4: Loops - Multiplication Table
**Difficulty**: ⭐⭐

Create a program that:
1. Prints multiplication table for a number (1-10)
2. Uses a loop

```ruby
# Solution:
def multiplication_table(num)
  puts "Multiplication Table for #{num}"
  (1..10).each do |i|
    puts "#{num} × #{i} = #{num * i}"
  end
end

multiplication_table(7)
```

### Exercise 1.5: Arrays and Iteration
**Difficulty**: ⭐⭐

Create a program that:
1. Stores names in an array
2. Finds the longest name
3. Counts names with more than 5 characters
4. Prints all names in uppercase

```ruby
# Solution:
names = ["Alice", "Bob", "Christopher", "David", "Elizabeth"]

# Find longest name
longest = names.max_by { |name| name.length }
puts "Longest name: #{longest}"

# Count names with 5+ characters
count = names.count { |name| name.length > 5 }
puts "Names with 5+ characters: #{count}"

# Print uppercase
puts "Names in uppercase:"
names.each { |name| puts name.upcase }
```

---

## SECTION 2: HASHES AND ADVANCED ITERATION (Days 6-8)

### Exercise 2.1: Hash Operations
**Difficulty**: ⭐⭐

Create a program that:
1. Stores student information (name, age, grade)
2. Accesses and modifies values
3. Adds new students
4. Prints formatted output

```ruby
# Solution:
students = {
  "Alice" => { age: 20, grade: "A" },
  "Bob" => { age: 21, grade: "B" },
  "Charlie" => { age: 20, grade: "C" }
}

# Access
puts students["Alice"][:grade]

# Modify
students["Bob"][:grade] = "A"

# Add new
students["David"] = { age: 22, grade: "B" }

# Print all
students.each do |name, info|
  puts "#{name}: Age #{info[:age]}, Grade #{info[:grade]}"
end
```

### Exercise 2.2: Array of Hashes
**Difficulty**: ⭐⭐⭐

Create a program that:
1. Stores employee data (name, salary, department)
2. Calculates average salary
3. Finds employees in specific department
4. Finds highest paid employee

```ruby
# Solution:
employees = [
  { name: "Alice", salary: 60000, department: "Engineering" },
  { name: "Bob", salary: 50000, department: "Sales" },
  { name: "Charlie", salary: 65000, department: "Engineering" },
  { name: "David", salary: 55000, department: "HR" }
]

# Average salary
salaries = employees.map { |e| e[:salary] }
average = salaries.sum / salaries.length
puts "Average Salary: $#{average}"

# Employees in Engineering
engineers = employees.select { |e| e[:department] == "Engineering" }
puts "\nEngineers:"
engineers.each { |e| puts "#{e[:name]}: $#{e[:salary]}" }

# Highest paid
top_paid = employees.max_by { |e| e[:salary] }
puts "\nHighest Paid: #{top_paid[:name]} ($#{top_paid[:salary]})"
```

### Exercise 2.3: Grouping Data
**Difficulty**: ⭐⭐⭐

Create a program that:
1. Groups employees by department
2. Counts employees per department
3. Prints department summary

```ruby
# Solution:
employees = [
  { name: "Alice", department: "Engineering" },
  { name: "Bob", department: "Sales" },
  { name: "Charlie", department: "Engineering" },
  { name: "David", department: "Sales" },
  { name: "Emma", department: "HR" }
]

# Group by department
grouped = employees.group_by { |e| e[:department] }

# Print summary
grouped.each do |dept, emps|
  puts "#{dept}: #{emps.length} employees"
  emps.each { |e| puts "  - #{e[:name]}" }
end
```

---

## SECTION 3: METHODS AND FUNCTIONS (Days 9-10)

### Exercise 3.1: Temperature Converter
**Difficulty**: ⭐⭐

Create methods that:
1. Convert Celsius to Fahrenheit
2. Convert Fahrenheit to Celsius
3. Validate temperature ranges

```ruby
# Solution:
def celsius_to_fahrenheit(celsius)
  (celsius * 9/5.0) + 32
end

def fahrenheit_to_celsius(fahrenheit)
  (fahrenheit - 32) * 5/9.0
end

def validate_temp(celsius)
  celsius > -273.15  # Absolute zero
end

puts celsius_to_fahrenheit(0)      # 32.0
puts celsius_to_fahrenheit(100)    # 212.0
puts fahrenheit_to_celsius(32)     # 0.0
puts fahrenheit_to_celsius(212)    # 100.0
```

### Exercise 3.2: Prime Number Checker
**Difficulty**: ⭐⭐⭐

Create methods that:
1. Check if a number is prime
2. Find all primes up to N
3. Count primes in a range

```ruby
# Solution:
def is_prime?(n)
  return false if n < 2
  (2...n).each { |i| return false if n % i == 0 }
  true
end

def primes_up_to(n)
  (2..n).select { |num| is_prime?(num) }
end

def count_primes(start, end_num)
  (start..end_num).count { |num| is_prime?(num) }
end

puts is_prime?(7)               # true
puts is_prime?(10)              # false
puts primes_up_to(20).inspect   # [2, 3, 5, 7, 11, 13, 17, 19]
puts count_primes(1, 50)        # 15
```

### Exercise 3.3: String Manipulation Library
**Difficulty**: ⭐⭐

Create methods that:
1. Count vowels
2. Remove vowels
3. Palindrome checker
4. Word reversal

```ruby
# Solution:
def count_vowels(str)
  vowels = "aeiouAEIOU"
  str.each_char.count { |char| vowels.include?(char) }
end

def remove_vowels(str)
  vowels = "aeiouAEIOU"
  str.delete(vowels)
end

def is_palindrome?(str)
  clean = str.downcase.gsub(/[^a-z0-9]/, "")
  clean == clean.reverse
end

def reverse_words(str)
  str.split(" ").reverse.join(" ")
end

puts count_vowels("Hello World")    # 3
puts remove_vowels("Hello World")   # "HllWrld"
puts is_palindrome?("A man a plan a canal Panama")  # true
puts reverse_words("Hello World Ruby")  # "Ruby World Hello"
```

---

## SECTION 4: OBJECT-ORIENTED PROGRAMMING (Days 11-15)

### Exercise 4.1: Person Class
**Difficulty**: ⭐⭐

Create a Person class with:
1. Name, age, email
2. Getters and setters
3. Methods to calculate age bracket (child, teen, adult, senior)

```ruby
# Solution:
class Person
  attr_accessor :name, :email
  attr_reader :age

  def initialize(name, age, email)
    @name = name
    @age = age
    @email = email
  end

  def age_bracket
    case @age
    when 0..12
      "Child"
    when 13..19
      "Teen"
    when 20..64
      "Adult"
    else
      "Senior"
    end
  end

  def birthday
    @age += 1
  end

  def info
    "#{@name} (#{@age}) - #{age_bracket} - #{@email}"
  end
end

# Usage
person = Person.new("Alice", 25, "alice@example.com")
puts person.info
person.birthday
puts "After birthday: #{person.age}"
```

### Exercise 4.2: Rectangle and Circle Classes
**Difficulty**: ⭐⭐⭐

Create Rectangle and Circle classes with:
1. Calculate area
2. Calculate perimeter
3. Scale method
4. String representation

```ruby
# Solution:
class Rectangle
  attr_accessor :width, :height

  def initialize(width, height)
    @width = width
    @height = height
  end

  def area
    @width * @height
  end

  def perimeter
    2 * (@width + @height)
  end

  def scale(factor)
    @width *= factor
    @height *= factor
  end

  def to_s
    "Rectangle(#{@width}×#{@height})"
  end
end

class Circle
  attr_accessor :radius

  def initialize(radius)
    @radius = radius
  end

  def area
    Math::PI * @radius ** 2
  end

  def perimeter
    2 * Math::PI * @radius
  end

  def scale(factor)
    @radius *= factor
  end

  def to_s
    "Circle(r=#{@radius})"
  end
end

# Usage
rect = Rectangle.new(4, 5)
puts rect.area        # 20
puts rect.perimeter   # 18
rect.scale(2)
puts rect             # Rectangle(8×10)

circle = Circle.new(3)
puts circle.area.round(2)     # 28.27
circle.scale(0.5)
puts circle                    # Circle(r=1.5)
```

### Exercise 4.3: Inheritance - Animal Hierarchy
**Difficulty**: ⭐⭐⭐

Create:
1. Animal base class
2. Dog and Cat subclasses
3. Override methods
4. Use super

```ruby
# Solution:
class Animal
  attr_reader :name, :age

  def initialize(name, age)
    @name = name
    @age = age
  end

  def speak
    "Some sound"
  end

  def info
    "#{@name} is #{@age} years old"
  end
end

class Dog < Animal
  def speak
    "Woof!"
  end

  def fetch
    "Fetching the ball"
  end

  def info
    super + " - Dog"
  end
end

class Cat < Animal
  def speak
    "Meow!"
  end

  def scratch
    "Scratching"
  end

  def info
    super + " - Cat"
  end
end

# Usage
dog = Dog.new("Max", 3)
puts dog.speak      # Woof!
puts dog.fetch      # Fetching the ball
puts dog.info       # Max is 3 years old - Dog

cat = Cat.new("Whiskers", 2)
puts cat.speak      # Meow!
puts cat.scratch    # Scratching
puts cat.info       # Whiskers is 2 years old - Cat
```

---

## SECTION 5: ADVANCED RUBY (Days 16-20)

### Exercise 5.1: Block and Iterator Mastery
**Difficulty**: ⭐⭐⭐

Create methods that:
1. Accept blocks for custom behavior
2. Use yield
3. Use map/select/reduce

```ruby
# Solution:
def with_prefix(prefix)
  ["Ruby", "Python", "Java"].each do |lang|
    puts "#{prefix} #{lang}"
  end
end

def transform_array(arr)
  result = []
  arr.each { |x| result << yield(x) }
  result
end

def conditional_each(arr)
  arr.each { |x| yield(x) if block_given? }
end

# Usage
with_prefix("Language:") { |lang| puts lang }

numbers = [1, 2, 3, 4, 5]
doubled = transform_array(numbers) { |n| n * 2 }
puts doubled.inspect  # [2, 4, 6, 8, 10]

conditional_each([1, 2, 3]) { |n| puts n }
```

### Exercise 5.2: Exception Handling
**Difficulty**: ⭐⭐⭐

Create a robust program that:
1. Handles multiple exceptions
2. Uses begin/rescue/ensure
3. Raises custom exceptions

```ruby
# Solution:
class InvalidAgeError < StandardError
end

def process_user(name, age)
  if name.nil? || name.empty?
    raise ArgumentError, "Name cannot be empty"
  end

  if age < 0
    raise InvalidAgeError, "Age cannot be negative"
  end

  if age < 18
    raise StandardError, "Must be 18 or older"
  end

  "Welcome, #{name}!"
end

begin
  puts process_user("Alice", 25)
rescue ArgumentError => e
  puts "Argument Error: #{e.message}"
rescue InvalidAgeError => e
  puts "Invalid Age: #{e.message}"
rescue StandardError => e
  puts "Error: #{e.message}"
ensure
  puts "Processing complete"
end
```

### Exercise 5.3: File Operations
**Difficulty**: ⭐⭐⭐

Create a program that:
1. Reads a file
2. Processes lines
3. Writes results to new file
4. Handles errors

```ruby
# Solution:
def process_log_file(input_file, output_file)
  begin
    lines = File.readlines(input_file)
    
    processed = lines.map do |line|
      line.strip.upcase  # Remove whitespace, convert to uppercase
    end

    File.open(output_file, "w") do |file|
      processed.each { |line| file.puts line }
    end

    puts "Processed #{processed.length} lines"
  rescue FileNotFoundError
    puts "File not found: #{input_file}"
  ensure
    puts "Operation complete"
  end
end

# Usage
# Create sample file first
File.write("input.txt", "hello world\nruby programming\nrocks!")
process_log_file("input.txt", "output.txt")

# Read output
puts File.read("output.txt")
```

---

## SECTION 6: MINI PROJECTS

### Project 1: Todo Application
**Difficulty**: ⭐⭐⭐

```ruby
class Todo
  attr_accessor :title, :completed

  def initialize(title)
    @title = title
    @completed = false
  end

  def complete
    @completed = true
  end

  def to_s
    status = @completed ? "[✓]" : "[ ]"
    "#{status} #{@title}"
  end
end

class TodoList
  def initialize
    @todos = []
  end

  def add(title)
    @todos << Todo.new(title)
  end

  def complete(index)
    @todos[index].complete if @todos[index]
  end

  def list
    @todos.each_with_index do |todo, i|
      puts "#{i + 1}. #{todo}"
    end
  end

  def remove(index)
    @todos.delete_at(index)
  end

  def count
    { total: @todos.length, completed: @todos.count(&:completed) }
  end
end

# Usage
todo_list = TodoList.new
todo_list.add("Learn Ruby")
todo_list.add("Build project")
todo_list.add("Deploy")

todo_list.list
todo_list.complete(0)
puts "\nAfter completing first task:"
todo_list.list
puts "\nStats: #{todo_list.count}"
```

### Project 2: Simple Calculator
**Difficulty**: ⭐⭐

```ruby
class Calculator
  def add(a, b)
    a + b
  end

  def subtract(a, b)
    a - b
  end

  def multiply(a, b)
    a * b
  end

  def divide(a, b)
    raise ArgumentError, "Cannot divide by zero" if b == 0
    a.to_f / b
  end

  def power(base, exponent)
    base ** exponent
  end

  def calculate(a, operation, b)
    case operation
    when "+"
      add(a, b)
    when "-"
      subtract(a, b)
    when "*"
      multiply(a, b)
    when "/"
      divide(a, b)
    when "**"
      power(a, b)
    else
      raise ArgumentError, "Unknown operation"
    end
  end
end

# Usage
calc = Calculator.new
puts calc.calculate(10, "+", 5)     # 15
puts calc.calculate(10, "-", 3)     # 7
puts calc.calculate(4, "*", 3)      # 12
puts calc.calculate(10, "/", 2)     # 5.0
puts calc.calculate(2, "**", 8)     # 256
```

### Project 3: Student Grade Manager
**Difficulty**: ⭐⭐⭐

```ruby
class Student
  attr_reader :name, :grades

  def initialize(name)
    @name = name
    @grades = []
  end

  def add_grade(grade)
    if grade < 0 || grade > 100
      raise ArgumentError, "Grade must be between 0 and 100"
    end
    @grades << grade
  end

  def average
    return 0 if @grades.empty?
    @grades.sum.to_f / @grades.length
  end

  def letter_grade
    avg = average
    case avg
    when 90..100
      "A"
    when 80..89
      "B"
    when 70..79
      "C"
    when 60..69
      "D"
    else
      "F"
    end
  end

  def summary
    "#{@name}: Average #{average.round(2)}, Grade: #{letter_grade}"
  end
end

class GradeManager
  def initialize
    @students = []
  end

  def add_student(name)
    @students << Student.new(name)
  end

  def add_grade(student_name, grade)
    student = @students.find { |s| s.name == student_name }
    student&.add_grade(grade)
  end

  def class_average
    return 0 if @students.empty?
    total = @students.sum { |s| s.average }
    total / @students.length
  end

  def top_student
    @students.max_by { |s| s.average }
  end

  def report
    puts "Class Average: #{class_average.round(2)}"
    puts "\nStudent Summaries:"
    @students.each { |s| puts s.summary }
  end
end

# Usage
manager = GradeManager.new

manager.add_student("Alice")
manager.add_student("Bob")
manager.add_student("Charlie")

manager.add_grade("Alice", 85)
manager.add_grade("Alice", 90)
manager.add_grade("Alice", 88)

manager.add_grade("Bob", 75)
manager.add_grade("Bob", 78)
manager.add_grade("Bob", 80)

manager.add_grade("Charlie", 95)
manager.add_grade("Charlie", 92)

manager.report
```

---

## CHALLENGE PROBLEMS

### Challenge 1: FizzBuzz
**Difficulty**: ⭐

```ruby
# Print numbers 1-100
# For multiples of 3: "Fizz"
# For multiples of 5: "Buzz"
# For multiples of both: "FizzBuzz"

(1..100).each do |n|
  output = ""
  output += "Fizz" if n % 3 == 0
  output += "Buzz" if n % 5 == 0
  puts output.empty? ? n : output
end
```

### Challenge 2: Fibonacci Sequence
**Difficulty**: ⭐⭐

```ruby
# Generate first N fibonacci numbers

def fibonacci(n)
  return [] if n == 0
  return [0] if n == 1
  
  sequence = [0, 1]
  (n - 2).times do
    sequence << sequence[-1] + sequence[-2]
  end
  sequence
end

puts fibonacci(10).inspect
```

### Challenge 3: Most Common Word
**Difficulty**: ⭐⭐⭐

```ruby
# Find most common word in text

def most_common_word(text)
  words = text.downcase.split(/\W+/).reject(&:empty?)
  word_count = words.each_with_object(Hash.new(0)) { |word, hash| hash[word] += 1 }
  word_count.max_by { |word, count| count }[0]
end

text = "Ruby is great. Ruby is fun. I love Ruby."
puts most_common_word(text)  # ruby
```

---

**Good luck with your practice!** 🚀

Remember: The best way to learn is by doing. Start with simple exercises and gradually move to harder ones.
