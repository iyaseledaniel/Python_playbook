# aligning text using format specifier with print()

# center aligning text
topic = "Learning python"
print("{:^100}".format(topic))

#left align text
python_definition = "Python is a high language programming language"
print("{:<30}".format(python_definition))

# right align text
concluding_part = "It is a great programming language with numerous use-cases"
print("{:>150}".format(concluding_part))
