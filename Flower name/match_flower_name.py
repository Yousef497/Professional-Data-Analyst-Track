# Write your code here

# HINT: create a dictionary from flowers.txt
def create_flowerdict(filename):
    flower_dict = {}
    with open(filename) as f:
        for line in f:
            letter = line.split(': ')[0]
            flower = line.split(': ')[1]
            flower_dict[letter] = flower
    
    return flower_dict

#print(create_flowerdict('flowers.txt'))

# HINT: create a function to ask for user's first and last name
def main():
    flower_d = create_flowerdict('flowers.txt')
    full_name = input('Enter your First [space] Last name only: ')
    first_name = full_name.split()[0].title()
    first_letter = first_name[0]
    
    msg = "Unique flower name with the first letter {}".format(flower_d[first_letter])
    
    print(msg)

# print the desired output
main()